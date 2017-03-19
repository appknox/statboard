from django.conf import settings
from django.shortcuts import render, redirect

from statboard.core.models import Metric


def index(request):
    """
    docstring for index
    """
    last_url = request.GET.get('last_url')
    if last_url not in settings.METRICS:
        last_url = settings.METRICS[-1]
    if last_url == settings.METRICS[-1]:
        next_url = settings.METRICS[0]
    else:
        idx = settings.METRICS.index(last_url)
        next_url = settings.METRICS[idx + 1]
    return redirect(next_url)


def metric_view(request):
    """
    docstring for metric_view
    """
    metric_name = request.resolver_match.url_name
    metric = Metric.objects.get(name=metric_name)
    return render(
        request, '%s.html' % metric_name,
        {'metric': metric, 'timeout': settings.NEXT_METRIC_TIMEOUT_MS})
