from django.conf import settings
from django.core.management.base import BaseCommand

from statboard.core.models import Metric


class Command(BaseCommand):
    help = "Seed the database with initial value"

    def handle(self, *args, **options):
        Metric.objects.get_or_create(name=settings.VIEW_GITHUB_PRS)
