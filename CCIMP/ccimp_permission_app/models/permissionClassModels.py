#!/usr/bin/python
#encoding:utf-8

from django.db import models


class PermissionClass(models.Model):

      '''权限分类表'''

      permission_chinese_name = models.CharField("权限中文名",max_length=100,null=False)

      permission_english_name = models.CharField("权限英文名",max_length=100,null=False)

      #1:sap超级管理员权限、2:pp项目管理权限、3:gp普通权限
      permission_options = models.IntegerField("权限分类",default=2)

      create_time = models.DateTimeField(null=False)

      update_time = models.DateTimeField(null=True)

      def __str__(self):

            return self.permission_chinese_name

