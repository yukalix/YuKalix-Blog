from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.db.models import Q
# Create your views here.

from .forms import MessageForm

from .models import Banner, AboutMeInfo
from .models import AboutMeArticle, Article, ShareRecourse
from .models import MessageUserPhoto,Message, Blogroll

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# 博客首页
class Index(View):

    def get(self, request):
        banners = Banner.objects.all().order_by('-id')[:3]
        info = AboutMeInfo.objects.last()
        blogrolls = Blogroll.objects.all()
        articles = Article.objects.all()
        # 特别推荐列表
        # classifys = Article.CLASSIFYS
        recommend_articles = articles.filter(is_recommend=True)[:6]
        # 最新文章
        new_articles = articles.order_by('-add_time')
        # 点击最高文章
        click_articles = articles.order_by('-look_nums')[:5]
        return render(request, 'index.html',{
            'banners': banners,
            'info': info,
            # 'classifys': classifys,
            'blogrolls': blogrolls,
            'recommend_articles': recommend_articles,
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
class Study(View):

    def get(self, request):
        classifies = Article.CLASSIFYS
        classify = request.GET.get('classify','python')
        same_as_articles = Article.objects.filter(classify=classify)

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(same_as_articles, 4)
        messages = p.page(page)


        # 本栏推荐
        recommend_articles = same_as_articles.filter(is_recommend=True)
        # 点击排行
        click_articles = same_as_articles.order_by('-look_nums')[:5]

        return render(request, 'study.html', {
            'classifies': classifies,
            'same_as_articles': same_as_articles,
            'messages': messages,
            'recommend_articles': recommend_articles,
            'click_articles': click_articles,
        })

# 资源共享
class Share(View):

    def get(self, request):
        recourses = ShareRecourse.objects.all().order_by('-add_time')
        return render(request, 'share.html', {
            'recourses': recourses,
        })

# 文章页
class ArticleView(View):

    def get(self, request, classify, id):
        article = Article.objects.filter(id=id)
        # 浏览量
        look_num = article[0].look_nums
        article.update(look_nums = look_num + 1)
        # 类似篇
        same_as_articles = Article.objects.filter(classify=classify)


        # BUG 未能完成获取分类里面上下篇操作
        # print(same_as_articles.filter(id__lt=id).first())
        # 构建一个空的
        none = {
            'classify': '#',
            'id': 0,
            'title': '',
        }
        up_article = same_as_articles.filter(id__lt=id).first()
        if not up_article:
            up_article = none
        down_article = same_as_articles.filter(id__gt=id).first()
        print(down_article)
        if not down_article:
            print('ok')
            down_article = none

        # 特别推荐列表
        # classifys = Article.CLASSIFYS
        recommend_articles = Article.objects.filter(is_recommend=True)[:6]
        # 点击最高文章
        click_articles = Article.objects.all().order_by('look_nums')[:5]


        # 获取文章标签
        # print(article.tag.all())
        return  render(request, 'article.html',{
            'article': article[0],
            'click_articles': click_articles,
            'recommend_articles': recommend_articles,
            'same_as_articles': same_as_articles,
            'up_article': up_article,
            'down_article': down_article,
        })

# 点赞
class ClickFav(View):
    def get(self, request):
        article_id = request.GET.get('article_id')
        click_fav = Article.objects.filter(id=article_id)
        fav_num = click_fav[0].fav_nums
        click_fav.update(fav_nums=fav_num+1)
        return HttpResponse('OK')

# 搜索
class Search(View):

    def get(self, request):
        keyboard = request.GET.get('keyboard')

        all_articles = Article.objects.all()

        if keyboard:
            articles = all_articles.filter(Q(title__contains=keyboard)|Q(author__icontains=keyboard)\
            |Q(classify__icontains=keyboard)|Q(content__in=keyboard))
        else:
            return HttpResponse('未找到')

        return render(request,'search.html', {'articles': articles})

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





def page404(request):
    return render(request, '404.html', status=404)