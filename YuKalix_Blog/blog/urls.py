from django.urls import path, include

from .views import Index, MessageView
app_name = 'blog'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('message/', MessageView.as_view(), name='message'),
]
