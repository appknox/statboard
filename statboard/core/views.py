from django.conf import settings
from django.shortcuts import render

from statboard.core.models import Metric


def github_prs(request):
    metric = Metric.objects.get(name=settings.VIEW_GITHUB_PRS)
    return render(
        request, '%s.html' % settings.VIEW_GITHUB_PRS, {'metric': metric})
