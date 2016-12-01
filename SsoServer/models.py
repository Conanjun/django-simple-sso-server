# coding:utf-8

from django.db import models
from django.contrib.auth.hashers import (
    check_password, make_password,
)


class TestUser(models.Model):

    username = models.CharField(max_length=40, verbose_name=u'用户名')
    password = models.CharField(max_length=128, verbose_name=u'密码')

    class Meta:
        verbose_name_plural = u'用户'
        verbose_name = u'用户'
