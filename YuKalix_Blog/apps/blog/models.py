from django.db import models
from datetime import datetime

# 富文本
# from DjangoUeditor.models import UEditorField
from ckeditor.fields import RichTextField

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
    email = models.EmailField(verbose_name='邮箱', default='dong.guowei@aliyun.com')
    record_tip = models.CharField(verbose_name='点滴语录', max_length=32)
    # article = UEditorField(u'内容',default='',width=1000,height=300,imagePath='goods/images/',filePath='goods/files/')
    add_time = models.DateTimeField(verbose_name='时间', auto_now_add=datetime.now())

    class Meta:
        verbose_name = '关于我信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


# 关于我页面文章
class AboutMeArticle(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=64)
    article = RichTextField(verbose_name='文章')
    class Meta:
        verbose_name = '关于我页面文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 文章标签
class ArticleTag(models.Model):
    tag_name = models.CharField(max_length=10, verbose_name="标签名", null=False, blank=False)

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name

# 文章
class Article(models.Model):
    CLASSIFYS = (
        ('python', 'Python'),
        ('web', '前端'),
        ('diary', '日记'),
        ('linux', 'Linux'),
    )
    image = models.ImageField(verbose_name='文章配图', upload_to='articles/%Y/%m/%d', blank=True)
    title = models.CharField(verbose_name='文章标题', max_length=64)
    author = models.CharField(verbose_name='文章作者', max_length=32, default='YuKalix')
    intro = models.CharField(verbose_name='文章简介', max_length=300, default='')
    tag = models.ManyToManyField(ArticleTag,verbose_name='文章标签',  max_length=10, default='', null=True, blank=True)
    content = RichTextField(verbose_name='文章内容')
    fav_nums = models.PositiveIntegerField(verbose_name='文章点赞量', default=0)
    look_nums = models.PositiveIntegerField(verbose_name='文章浏览量', default=0)
    classify = models.CharField(verbose_name='文章分类', choices=CLASSIFYS, max_length=10)
    is_recommend = models.BooleanField(verbose_name='特别推荐', default=False)
    is_original = models.BooleanField(verbose_name='原创', default=False)
    add_time = models.DateTimeField(verbose_name='时间', auto_now_add=datetime.now())

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 获取总的本站浏览量
    def get_all_look_nums(self):
        all_look_nums = Article.objects.values('look_nums')
        all_look_num = 0
        for i in all_look_nums:
            all_look_num += i['look_nums']
        return all_look_num

# 资源共享
class ShareRecourse(models.Model):
    image = models.ImageField(verbose_name='资源图片', upload_to='resourse/%Y/%m/%d', blank=True)
    name = models.CharField(verbose_name='资源名字', max_length=64)
    intro = models.CharField(verbose_name='资源介绍', max_length=300)
    path = models.URLField(verbose_name='资源链接',default='')
    passwd = models.CharField(verbose_name='资源密码', max_length=10, blank=True)
    add_time = models.DateTimeField(verbose_name='时间', auto_now_add=datetime.now())

    class Meta:
        verbose_name = '资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 留言
class MessageUserPhoto(models.Model):
    user_photo = models.ImageField(verbose_name='用户头像', upload_to='message/users/%Y/%m/%d')
    class Meta:
        verbose_name = '留言头像'
        verbose_name_plural = verbose_name

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

# 友情链接
class Blogroll(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=32)
    url =  models.URLField(verbose_name='链接')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

