from django.shortcuts import render
from statboard.core.models import Metric


def github(request):
    metric = Metric.objects.get(name='GITHUB')
    return render(request, 'github.html', {'metric': metric})
