#!/usr/bin/python
#encoding:utf-8


from django.db import models

class User(models.Model):

      '''用户表'''

      user_name = models.CharField("账户",max_length=50,null=False)

      password = models.CharField("密码",max_length=50,null=False)

      real_name = models.CharField("姓名",max_length=50,null=False)

      mail = models.EmailField("邮箱",max_length=200,null=False)

      #1:sap超级管理员权限、2:pp项目权限、3:mp:模块权限、4:gp普通权限
      permission_options = models.IntegerField("权限分类",default=4)

      create_time = models.DateTimeField(auto_now=True)

      update_time = models.DateTimeField(null=True)

      def __str__(self):

            return self.user_name

