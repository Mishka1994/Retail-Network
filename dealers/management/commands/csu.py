import os

from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""
    def handle(self, *args, **options):
        user = User.objects.create(
            username=os.getenv('SUPERUSER_NAME'),
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(os.getenv('SUPERUSER_PASSWORD'))
        user.save()
