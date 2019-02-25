from django.db import models

# Create your models here.
from django.utils import timezone


# 单日阅读量
class DayLookNumber(models.Model):
    day=models.DateField(verbose_name='日期',default=timezone.now)
    count=models.IntegerField(verbose_name='总阅读量',default=0) #网站访问总次数
    class Meta:
        verbose_name = '单日总阅读量'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)

    # 获取今天阅读量
    def get_today_look_nums(self):
        try:
            today_look_nums =DayLookNumber.objects.filter(day=timezone.now().date())
            today_look_nums = today_look_nums[0].count
            return today_look_nums
        except:
            return 0

#访问网站的ip地址和次数
class Userip(models.Model):
    ip=models.CharField(verbose_name='IP地址',max_length=30)    #ip地址
    count=models.IntegerField(verbose_name='访问次数',default=0) #该ip访问次数
    class Meta:
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip

#网站总访问次数
class VisitNumber(models.Model):
    count=models.IntegerField(verbose_name='网站访问总次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = '网站访问总次数'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)

    def get_all_visit_nums(self):
        all_visit_nums = VisitNumber.objects.all()
        all_visit_nums = all_visit_nums[0].count
        print(all_visit_nums)
        return all_visit_nums

#单日访问量统计
class DayNumber(models.Model):
    day=models.DateField(verbose_name='日期',default=timezone.now)
    count=models.IntegerField(verbose_name='网站访问次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = '网站日访问量统计'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.day)

    def get_day_visit_nums(self):
        today_visit_nums =DayNumber.objects.filter(day=timezone.now().date())
        today_visit_nums = today_visit_nums[0].count
        return today_visit_nums

