import base64
import importlib
import re

import requests
from django.conf import settings
from django.core.files import File

from zs_utils.api.services import ApiRequestLogService
from zs_utils.email_notification import models
from zs_utils.exceptions import CustomException
from zs_utils.json_utils import pretty_json


class EmailServiceException(CustomException):
    pass


class Unisender:
    API_URL = "https://go1.unisender.ru/ru/transactional/api/v1/"
    FROM_EMAIL = "noreply@id.kokocgroup.ru"

    @classmethod
    def send_email(
            cls,
            receivers: list,
            sender: str,
            subject: str,
            message: str,
            files: dict = None,
            message_format: str = "plaintext",
            **kwargs,
    ):
        data = {
            "message": {
                "recipients": [{"email": email} for email in receivers],
                "body": {message_format: message},
                "subject": subject,
                "from_email": cls.FROM_EMAIL,
                "from_name": sender,
                "skip_unsubscribe": 1,
                "attachments": [
                    {"name": name, "content": value, "type": "application/octet-stream"}
                    for name, value in files.items()
                ]
                if files
                else None,
            }
        }

        response = requests.post(
            url=cls.API_URL + "email/send.json",
            headers={"X-API-KEY": getattr(settings, "UNISENDER_API_KEY")},
            json=data,
        )
        ApiRequestLogService.save_api_request_log_by_response(response=response, save_if_is_success=False)
        if not response.ok:
            raise EmailServiceException(pretty_json(response.json()))

        return response.json()

    @classmethod
    def send_html_email(cls, **kwargs):
        return cls.send_email(message_format="html", **kwargs)


class EmailService(Unisender):
    """
    Сервис для отправки писем по шаблону через Unisender
    """

    # ------------------------------ Генерация полного HTML шаблона ------------------------------
    @classmethod
    def get_template_file(cls, template_name: str):
        """
        Получение файла с частями шаблона
        """
        template_package = getattr(settings, "EMAIL_TEMPLATE_PACKAGE")
        if not template_package:
            raise EmailServiceException("Не указан базовый пакет шаблонов в настройках")

        full_template_module = f"{template_package}.{template_name}"

        try:
            template_module = importlib.import_module(full_template_module)
        except ModuleNotFoundError:
            raise EmailServiceException(f"Шаблон {template_name} не найден")

        return template_module

    @classmethod
    def get_template_languages(cls, template_name: str) -> list:
        """
        Получение всех языков шаблона
        """
        template_file = cls.get_template_file(template_name=template_name)
        languages = list()
        for part in dir(template_file):
            if "body" in part:
                languages.append(part.split("_")[-1])
        return languages

    @classmethod
    def validate_template_params(cls, html_template: str, template_params: dict):
        """
        Валидация параметров шаблона
        """
        params = re.findall(pattern=r"{(.*?)}", string=html_template)
        required_params = [template_param.replace("{", "") for template_param in params]

        errors = dict()
        required_params = list(set(required_params))
        for required_param in required_params:
            if required_param not in template_params:
                errors[f"template_params.{required_param}"] = "Обязательное поле."
        if errors:
            raise EmailServiceException(message_dict=errors)

    @classmethod
    def get_template_data(cls, template_name: str, language: str, template_params: dict) -> dict:
        """
        Получение данных шаблона
        """
        # Базовая информация: файл шаблона с частями и url со статикой
        template_file = cls.get_template_file(template_name=template_name)
        static_url = getattr(settings, "EMAIL_STATIC_FOLDER_URL", "https://storage.yandexcloud.net/zs-static/email/")
        if not hasattr(template_file, f"body_{language}"):
            raise EmailServiceException(
                message_dict={"language": f"Для данного шаблона не определён язык '{language}'"}
            )

        # Костыль для шаблона zonesmart.order
        if "items" in template_params:
            items = ""
            item_template = getattr(template_file, f"items_{language}", getattr(template_file, "items", None))
            for item in template_params["items"]:
                items += item_template.format(**item)
            template_params["items"] = items

        # Переносим части шаблона в словарь
        title = getattr(template_file, f"title_{language}")
        template_data = {
            "title": title,
            "subject": getattr(template_file, f"subject_{language}", title).format(**template_params),
            "body": getattr(template_file, f"body_{language}"),
            "cheers": getattr(template_file, f"cheers_{language}", ""),
            "footer": getattr(template_file, f"footer_{language}", ""),
            "logo": template_file.base.logo,
            "email_icon": getattr(template_file, "icon", ""),
            "static_url": static_url,
        }

        # Составление полного шаблона из частей
        base_template = template_file.base.base_template
        template_data["html"] = base_template.format(**template_data)
        cls.validate_template_params(html_template=template_data["html"], template_params=template_params)
        template_data["html"] = template_data["html"].format(**template_params)
        return template_data

    @classmethod
    def create_email_notification(
        cls,
        sender: str,
        receivers: list,
        template_name: str,
        language: str = "ru",
        is_urgent: bool = False,
        params: dict = None,
        files: list = None,
    ) -> models.EmailNotification:
        """
        Создание объекта email уведомления
        """
        email_notification = models.EmailNotification.objects.create(
            sender=sender,
            receivers=receivers,
            language=language,
            template_name=template_name,
            template_params=params,
            is_urgent=is_urgent,
        )
        if files:
            for file in files:
                models.EmailNotificationFile.objects.create(
                    email_notification=email_notification, name=file.name, file=File(file)
                )
        return email_notification

    # ------------------------------ Отправка email письма ------------------------------

    @classmethod
    def send_email_notification(cls, email_notification: models.EmailNotification, force: bool = False, **kwargs):
        """
        Отправка email-уведомления по объекту email_notification
        """
        if email_notification.is_sent and not force:
            raise EmailServiceException("Уведомление уже было отправлено.")

        files = dict()
        for file in email_notification.files.all():
            files[file.name] = base64.b64encode(file.file.read()).decode()

        results = cls.send_template_email(
            sender=email_notification.sender,
            receivers=email_notification.receivers,
            template_name=email_notification.template_name,
            language=email_notification.language,
            params=email_notification.template_params,
            files=files,
            **kwargs,
        )

        email_notification.is_sent = True
        email_notification.save(update_fields=["is_sent"])
        return results

    @classmethod
    def send_template_email(
        cls,
        template_name: str,
        language: str,
        sender: str,
        receivers: list,
        params: dict,
        files: dict = None,
        **kwargs,
    ):
        """
        Отправка email-уведомления по шаблону
        """
        language = language if language == "ru" else "en"
        template_data = cls.get_template_data(template_name=template_name, language=language, template_params=params)
        return cls.send_html_email(
            sender=sender,
            receivers=receivers,
            subject=template_data["subject"],
            message=template_data["html"],
            files=files,
        )
