#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: temp.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-03-18
"""

from statboard.core.config import huey  # NOQA
from statboard.core.tasks import count_beans


if __name__ == '__main__':
    count_beans(5)
    print('Enqueued job to count %s beans' % 5)
