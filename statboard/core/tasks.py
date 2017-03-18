#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: tasks.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-03-18
"""

import os
from github import Github
from django.conf import settings
from statboard.core.models import Metric
from statboard.core.config import huey # NOQA
from huey.contrib.djhuey import crontab, periodic_task

g = Github(os.environ['STATBOARD_GITHUB_TOKEN'])


@periodic_task(crontab(minute='*/1'))
def fetch_metrics():
    # Code to get data
    print("getting github")
    u = g.get_user('appknox')
    r = u.get_repo('mycroft')
    prs = r.get_pulls()
    pr_list = []
    for pr in prs:
        pr_list.append(pr.title)
    gh_prs = Metric.objects.get(name=settings.VIEW_GITHUB_PRS)
    pr_data = {'pr_list': pr_list}
    gh_prs.set_data(pr_data)

    issues = r.get_issues()
    issue_list =[]
    for issue in issues:
        issue_list.append(issue.title)
    gh_issues = Metric.objects.get(name=settings.VIEW_GITHUB_ISSUES)
    issue_data = {'issue_list': issue_list}
    gh_issues.set_data(issue_data)

    print("fetched github")
