from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    re_path(r'post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit')
]
