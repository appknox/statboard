from django.conf import settings
from django.shortcuts import render

from statboard.core.models import Metric


def github_prs(request):
    metric = Metric.objects.get(name=settings.VIEW_GITHUB_PRS)
    return render(
        request, '%s.html' % settings.VIEW_GITHUB_PRS,
        {'pr_list': metric.data_dict['pr_list']})

def github_issues(request):
    metric = Metric.objects.get(name=settings.VIEW_GITHUB_ISSUES)
    return render(
        request, '%s.html' % settings.VIEW_GITHUB_ISSUES,
        {'issue_list': metric.data_dict['issue_list']})

def twitter_widgets(request):
    return render(
        request, 'twitter_widgets.html')        
