#!/usr/bin/python
#encoding:utf-8

from django.db import models

from ccimp_user_app.models.userModels import User

class Project(models.Model):

      '''

      项目表

      '''

      user = models.ForeignKey(User,on_delete=models.CASCADE)

      name = models.CharField("名称",max_length=50,null=False)

      describe = models.TextField("描述",default="",max_length=50)

      status = models.IntegerField("状态",default=0)#禁用0 开启1 进行中2 已完成3 暂停4

      create_time = models.DateTimeField(null=False)

      update_time = models.DateTimeField(null=True)


      def __str__(self):

            return self.name

