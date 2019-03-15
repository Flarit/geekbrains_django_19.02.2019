from django.dispatch import receiver
from django.db.models import signals
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import ShopUser


@receiver(signals.post_save, sender=ShopUser)
def test(instance: ShopUser, created=False, **kwargs):
    if created:
        email = instance.email if instance.email else 'default@mail.ru'
        html = render_to_string('mainapp/email_templates/email.html', context={'name': 'Иван'})
        send_mail('Тестовое письмо', 'Привет! Мы тестируем письмо, не обращай внимания',
                  'Скорочтец <{}>'.format(settings.SENDER_EMAIL), [email], html_message=html)
