from django.urls import path, re_path

from .views import Index, AboutMe, Study, Share, ArticleView, MessageView
from .views import Search, ClickFav

app_name = 'blog'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about_me/', AboutMe.as_view(), name='about_me'),
    path('study/', Study.as_view(), name='study'),
    path('share/', Share.as_view(), name='share'),
    path('article/<str:classify>/<int:id>/', ArticleView.as_view(), name='article'),
    path('click_fav/', ClickFav.as_view(), name='click_fav'),
    path('search/', Search.as_view(), name='search'),
    path('message/', MessageView.as_view(), name='message'),
]
