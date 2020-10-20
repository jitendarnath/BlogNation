from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header="BlogNation Admin"
admin.site.site_title="BlogNation Admin Panel"
admin.site.index_title="Welcome to BlogNation Admin Panel"

urlpatterns = [ 
   path('', views.blogHome, name='blogHome'), 
   path('<str:slug>', views.blogPost, name='blogPost'), 
]