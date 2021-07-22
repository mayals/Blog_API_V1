from django.contrib import admin
from django.urls import path
from . import views 

app_name='blog_api'

urlpatterns = [
    path('',views.PostAPIView.as_view(),name='post_api'),

]