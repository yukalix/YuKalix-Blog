from django.db import models
from datetime import datetime
# Create your models here.

"""
主页midels
"""
# Banner
class Banner(models.Model):
    banner_imamge = models.ImageField(verbose_name='图片', upload_to='banners/%Y/%m', blank=True)
    baner_describe = models.CharField(verbose_name='图片描述', max_length=32, default='广告位招租')
    add_time = models.DateTimeField(verbose_name='时间', auto_now_add=datetime.now())

    class Meta:
        verbose_name = '主页Banner'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.baner_describe

# 关于我信息
class AboutMeInfo(models.Model):
    head_portrait = models.ImageField(verbose_name='头像', upload_to='about_me/', blank=True)
    nick_name = models.CharField(verbose_name='昵称', max_length=32, default='YuKalix')
    name = models.CharField(verbose_name='姓名', max_length=32, default='羽')
    work = models.CharField(verbose_name='工作', max_length=32, default='Python全栈开发工程师')
    place = models.CharField(verbose_name='地点', max_length=32, default='杭州')
    email = models.EmailField(verbose_name='邮箱')
    record_tip = models.CharField(verbose_name='点滴语录', max_length=32)
    add_time = models.DateTimeField(verbose_name='时间', auto_now_add=datetime.now())

    class Meta:
        verbose_name = '关于我信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name



# 留言
class MessageUserPhoto(models.Model):
    user_photo = models.ImageField(verbose_name='用户头像', upload_to='message/users/%Y/%m/%d')
    class Meta:
        verbose_name = '留言头像'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id

class Message(models.Model):
    user_photo = models.URLField(verbose_name='用户头像',default='/media/message/users/2019/02/20/tx2.jpg')
    user_name = models.CharField(verbose_name='用户名', max_length=32)
    message = models.CharField(verbose_name='留言', max_length=126)
    add_time = models.DateTimeField(verbose_name='时间', auto_now_add=datetime.now())

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message