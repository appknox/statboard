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

import logging
from django.conf import settings
from importlib import import_module
from statboard.core.models import Metric
from statboard.core.config import huey # NOQA
from huey.contrib.djhuey import crontab, periodic_task

logger = logging.getLogger(__name__)


@periodic_task(crontab(minute='*/1'))
def fetch_metrics():
    for metric_name in settings.METRICS:
        logger.debug('~' * 80)
        try:
            logger.debug("Initializing metrics for: %s" % metric_name)
            metric = Metric.objects.get(name=metric_name)
            metric_module = import_module(
                'statboard.core.metrics.%s' % metric_name)
            logger.debug("Attemting to fetch metrics for: %s" % metric_name)
            metric_module.fetch(metric)
            logger.debug("DONE! fetched metrics for: %s" % metric_name)
        except Exception as e:
            logger.error("FAILED! metrics for: %s \n %s" % (metric_name, e))
