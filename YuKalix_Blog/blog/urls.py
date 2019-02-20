from django.urls import path, include

from .views import Index, AboutMe, Share, MessageView
app_name = 'blog'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about_me/', AboutMe.as_view(), name='about_me'),
    path('share/', Share.as_view(), name='share'),
    path('message/', MessageView.as_view(), name='message'),
]
