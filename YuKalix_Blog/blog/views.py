from django.shortcuts import render, HttpResponse
from django.views.generic import View
# Create your views here.

from .models import Banner, AboutMeInfo

# 博客首页
class Index(View):

    def get(self, request):
        banners = Banner.objects.all().order_by('-id')[:3]
        info = AboutMeInfo.objects.last()
        return render(request, 'index.html',{
            'banners': banners,
            'info': info,
        })


# 留言
class Message(View):

    def get(selfr, request):
        info = AboutMeInfo.objects.first()
        return render(request, 'message.html',{
            'info': info,
        })

    def post(self, request):
        user_photo = request.POST.get('mycall', '')
        user_name = request.POST.get('name')
        messge = request.POST.get('lytext')
        print(user_name)
        print(user_photo)
        print(messge)
        return HttpResponse('OK')

