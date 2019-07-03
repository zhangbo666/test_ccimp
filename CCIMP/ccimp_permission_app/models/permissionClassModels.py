#!/usr/bin/python
#encoding:utf-8

from time import strftime, localtime, time
from dateutil import parser

from django.db import models

class PermissionClass(models.Model):

      '''权限分类表'''

      # 转换为str类型
      current_now_time = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))

      # 转换为datetime.datetime类型
      current_now_time= parser.parse(current_now_time)


      permission_chinese_name = models.CharField("权限中文名",max_length=100,null=False)

      permission_english_name = models.CharField("权限英文名",max_length=100,null=False)

      #1:sap超级管理员权限、2:pp项目管理权限、3:mp:模块管理权限、4:gp普通权限
      permission_options = models.IntegerField("权限分类",default=4)

      create_time = models.DateTimeField()

      update_time = models.DateTimeField(null=True)

      def __str__(self):

            return self.permission_chinese_name

