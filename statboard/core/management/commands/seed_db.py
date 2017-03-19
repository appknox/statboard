from django.conf import settings
from django.core.management.base import BaseCommand

from statboard.core.models import Metric


class Command(BaseCommand):
    help = "Seed the database with initial value"

    def handle(self, *args, **options):
        for metric_name in settings.METRICS:
            metric, _ = Metric.objects.get_or_create(name=metric_name)
            metric.set_data({})
            print("Created: %s" % metric)
