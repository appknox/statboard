#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: github_prs.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-03-19
"""

import os
from github import Github

g = Github(os.environ['STATBOARD_GITHUB_TOKEN'])


def fetch(metric):
    u = g.get_user('appknox')
    r = u.get_repo('mycroft')
    prs = r.get_pulls()
    pr_list = []
    for pr in prs:
        pr_list.append({'url': pr.html_url, 'title': pr.title})
    pr_data = {'pr_list': pr_list}
    metric.set_data(pr_data)
