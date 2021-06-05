from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('blogs/',views.blogs,name='blogs'),
    re_path(r'^blog(?P<blog_id>\d+)/$',views.blog,name='blog'),
    path('new_blog/',views.new_blog,name='new_blog'),
    re_path(r'^new_comment/(?P<blog_id>\d+)/$',views.new_comment,name='new_comment'),
    re_path(r'^edit_blog/(?P<blog_id>\d+)/$',views.edit_blog,name='edit_blog'),
    re_path(r'^edit_comment/(?P<comment_id>\d+)/$',views.edit_comment,name='edit_comment'),
    path('help/',views.help,name='help'),
]