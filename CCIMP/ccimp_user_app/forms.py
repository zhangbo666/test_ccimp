#!/usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'


from django import forms
from django.forms import fields,widgets
from ccimp_user_app.models.userModels import User


class UserLoginForm(forms.Form):

      user_name = fields.CharField(min_length=5,max_length=50)

      # password = fields.CharField(min_length=6,max_length=50)
      # 密码密文*输出
      password = fields.Field(widget=widgets.PasswordInput())

class UserRegisterForm(forms.Form):

      user_name = fields.CharField(min_length=5, max_length=50)

      # password = fields.CharField(min_length=6, max_length=50)
      # 密码密文*输出
      password = fields.Field(widget=widgets.PasswordInput())

      real_name = fields.CharField(min_length=2,max_length=50)

      mail = fields.EmailField(min_length=6,max_length=50)

      # ap:管理员权限、pp:项目权限、mp:模块权限、gp:普通权限
      # permission = fields.CharField(max_length=50)
      # permission = forms.ChoiceField(label="选择框",choices=(("ap","管理员权限"),
      #                                                      ("pp","项目权限"),
      #                                                      ("mp","模块权限"),
      #                                                      ("gp","普通权限"),))




# class UserLoginForm(forms.ModelForm):
#
#     class Meta:
#
#         model = User
#
#         fields = ['user_name', 'password',]


# class UserRegisterForm(forms.ModelForm):
#
#     class Meta:
#
#         model = User
#
#         fields = ['user_name', 'password', 'real_name', 'mail']