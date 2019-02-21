from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
# Create your views here.

from .forms import MessageForm

from .models import Banner, AboutMeInfo
from .models import AboutMeArticle, Article
from .models import MessageUserPhoto,Message, Blogroll

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# 博客首页
class Index(View):

    def get(self, request):
        banners = Banner.objects.all().order_by('-id')[:3]
        info = AboutMeInfo.objects.last()
        blogrolls = Blogroll.objects.all()
        articles = Article.objects.all()
        # 最新文章
        new_articles = articles.order_by('-add_time')
        # 点击最高文章
        click_articles = articles.order_by('look_nums')[:5]
        return render(request, 'index.html',{
            'banners': banners,
            'info': info,
            'blogrolls': blogrolls,
            'new_articles': new_articles,
            'click_articles': click_articles,
        })

# 关于我页面
class AboutMe(View):

    def get(self, request):
        article = AboutMeArticle.objects.last()
        info = AboutMeInfo.objects.last()
        return render(request, 'about.html',{
            'article': article,
            'info': info,
        })

# 学无止境页面
class Share(View):

    def get(self, request):
        return render(request, 'share.html')

# 文章页
class ArticleView(View):

    def get(self, request, classify, id):
        article = Article.objects.filter(id=id)
        same_as_articles = Article.objects.filter(classify=classify)
        # 点击最高文章
        click_articles = Article.objects.all().order_by('look_nums')[:5]

        # BUG 未能完成获取分类里面上下篇操作
        up_article = same_as_articles[0]
        print(up_article)
        down_article = same_as_articles[0]
        print(down_article)


        # 获取文章标签
        # print(article.tag.all())
        return  render(request, 'article.html',{
            'article': article[0],
            'click_articles': click_articles,
            'same_as_articles': same_as_articles,
            'up_article': up_article,
            'down_article': down_article,
        })

# 留言
class MessageView(View):

    def get(selfr, request):
        info = AboutMeInfo.objects.first()
        message_form = MessageForm()
        # 获取留言所有头像
        message_photos = MessageUserPhoto.objects.all()

        # 获取所有留言,分页
        messages = Message.objects.all().order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(messages, 6, request=request)
        all_message_page = p.page(page)

        return render(request, 'message.html',{
            'all_message_page': all_message_page,
            # 'messages': messages,
            'message_photos': message_photos,
            'message_form': message_form,
            'info': info,
        })

    def post(self, request):
        message_form = MessageForm(request.POST)
        print(message_form.errors)
        if message_form.is_valid():
            # 获取留言所有头像
            message_photos = MessageUserPhoto.objects.all()
            user_photo = request.POST.get('mycall', '/media/message/users/2019/02/20/tx2.jpg')
            user_name = request.POST.get('name')
            message = request.POST.get('message')
            message_info = Message.objects.create(user_photo=user_photo, user_name=user_name, message=message)
            message_info.save()
            return redirect('/message/')

        else:
            errors_obj = message_form.errors
            # 获取留言所有头像
            message_photos = MessageUserPhoto.objects.all()
            return render(request, 'message.html', {
                'message_photos': message_photos,
                'message_form': message_form,
                'errors_obj':errors_obj,
            })

