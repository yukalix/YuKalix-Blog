from django.urls import path

from .views import Index, AboutMe, Share, ArticleView, MessageView
app_name = 'blog'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about_me/', AboutMe.as_view(), name='about_me'),
    path('share/', Share.as_view(), name='share'),
    path('article/<str:classify>/<int:id>/', ArticleView.as_view(), name='article'),
    path('message/', MessageView.as_view(), name='message'),
]
