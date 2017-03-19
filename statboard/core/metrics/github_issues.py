#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: github_issues.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-03-19
"""

import os
from github import Github

g = Github(os.environ['STATBOARD_GITHUB_TOKEN'])


def fetch(metric):
    u = g.get_user('appknox')
    r = u.get_repo('mycroft')
    issues = r.get_issues()
    issue_list = []
    for issue in issues:
        issue_list.append({'url': issue.html_url, 'title': issue.title})
    issue_data = {'issue_list': issue_list}
    metric.set_data(issue_data)
