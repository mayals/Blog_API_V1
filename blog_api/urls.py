from django.contrib import admin
from django.urls import path
from . import views


app_name='blog_api'

urlpatterns = [
    path('post_list_create',views.PostListCreateAPIView.as_view()),
    path('post_retrieve_update_destroy/<int:id>',views.PostRetrieveUpdateDestroyAPIView.as_view()),

    path('user_list_create/', views.UserListCreateAPIView.as_view()),
    path('user_retrieve_update_destroy/<int:pk>/',views.UserRetrieveUpdateDestroyAPIView.as_view()),
]
