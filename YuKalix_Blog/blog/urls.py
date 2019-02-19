from django.urls import path, include

from .views import Index, Message
app_name = 'blog'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('message/', Message.as_view(), name='message'),
]
