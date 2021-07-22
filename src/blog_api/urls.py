from django.contrib import admin
from django.urls import path
from . import views 

app_name='blog_api'

urlpatterns = [
    path('',views.PostListCreateAPIView.as_view()),
    path('post/<int:id>',views.PostRetrieveUpdateDestroyAPIView.as_view()),
]