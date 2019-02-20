from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
# Create your views here.

from .forms import MessageForm

from .models import Banner, AboutMeInfo
from .models import AboutMeArticle
from .models import MessageUserPhoto,Message
# 博客首页
class Index(View):

    def get(self, request):
        banners = Banner.objects.all().order_by('-id')[:3]
        info = AboutMeInfo.objects.last()
        return render(request, 'index.html',{
            'banners': banners,
            'info': info,
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

# 留言
class MessageView(View):

    def get(selfr, request):
        info = AboutMeInfo.objects.first()
        message_form = MessageForm()
        # 获取留言所有头像
        message_photos = MessageUserPhoto.objects.all()
        # 获取所有留言,分页
        messages = Message.objects.all().order_by('-add_time')
        return render(request, 'message.html',{
            'messages': messages,
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

