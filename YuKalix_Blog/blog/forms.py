# **********************OBJ INFO**************************
# Author:Kali Yu
# @Time    : 2019-2-19 23:35
# @Site    : 52ziyu.cn
# @File    : forms.py
# @software: PyCharm
# *********************************************************

from django import forms

# 留言
class MessageForm(forms.Form):
    name = forms.CharField(required=True,min_length=1,max_length=8)
    message = forms.CharField(required=True,min_length=1,max_length=126,
                              error_messages={
                                  'required':'该字段没填哦,谢谢大家多提提建议.'
                              })