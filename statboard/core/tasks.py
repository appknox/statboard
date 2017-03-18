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

from statboard.core.config import huey # NOQA
from huey.contrib.djhuey import crontab, periodic_task


@periodic_task(crontab(minute='*/1'))
def fetch_metrics():
    # Code to get data
    print('Every five minutes this will be printed by the consumer')
