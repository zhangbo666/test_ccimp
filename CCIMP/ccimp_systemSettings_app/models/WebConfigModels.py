#!/usr/bin/python
#encoding:utf-8

from django.db import models

class WebConfig(models.Model):

      '''
      
      web配置表

      '''

      nameConfig = models.CharField("配置名称",max_length=50,null=False)

      keyConfig = models.CharField("配置Key",max_length=200,null=False)

      valueConfig = models.CharField("配置Value",max_length=200,null=False)

      describeConfig = models.TextField("配置描述",default="",max_length=200)

      create_time = models.DateTimeField(null=False)

      update_time = models.DateTimeField(null=True)


      def __str__(self):

            return self.nameConfig

