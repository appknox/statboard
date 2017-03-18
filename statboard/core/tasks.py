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

from statboard.core.config import huey


@huey.task()
def count_beans(num):
    print("FOFAOFOAFO")
    print('-- counted %s beans --' % num)
