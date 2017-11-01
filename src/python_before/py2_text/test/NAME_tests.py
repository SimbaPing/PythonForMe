# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-10-10 22:23:35
# @Last Modified by:   Administrator
# @Last Modified time: 2016-10-10 22:25:36
from nose.tools import *
import NAME


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_basic():
    print "I RAN!"
