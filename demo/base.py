#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import re
import base64
import json
import datetime

# 通常你不应该从django引入任何代码, 但ImproperlyConfigured是个例外
from django.core.exceptions import ImproperlyConfigured

__all__ = ['PWD', 'APP', 'BASE_DIR', 'LOG_FILE', 'get_env_variable']

PWD = os.path.dirname(os.path.abspath(__file__))
APP = os.path.basename(PWD)
BASE_DIR = os.path.dirname(PWD)
LOG_FILE = os.path.abspath(os.path.join(BASE_DIR, "%s.log" % (APP,)))

sys.path.insert(0, os.path.join(BASE_DIR, "libs"))


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)
