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
    m = Metric.objects.get(name=settings.VIEW_GITHUB_PRS)
    data = {'pr_list': pr_list}
    m.set_data(data)
    print("fetched github")
