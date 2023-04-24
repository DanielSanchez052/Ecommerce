from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string 
from django.utils.html import strip_tags
from celery.utils.log import get_task_logger
from Ecommerce.celery import app

logger = get_task_logger(__name__)


def send_email_single(subject,context, html_template):
    try:
        html_message = render_to_string(html_template, context=context)
        plain_message = strip_tags(html_message) 
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=settings.EMAIL_NOTIFY,
            html_message=html_message
        )
    except Exception as e:
        logger.info(e.__class__)