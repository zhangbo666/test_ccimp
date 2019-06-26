#!/usr/bin/python
#encoding:utf-8


from django.db import models

class UserPermission(models.Model):

      '''用户权限表'''

      permission_chinese_name = models.CharField("权限中文名",max_length=100,null=False)

      permission_english_name = models.CharField("权限英文名",max_length=100,null=False)

      #1:sap超级管理员权限、2:pp项目权限、3:mp:模块权限、4:gp普通权限
      permission_options = models.IntegerField("权限分类",default=4)

      create_time = models.DateTimeField(auto_now=True)

      update_time = models.DateTimeField(null=True)


      def __str__(self):

            return self.permission_chinese_name

