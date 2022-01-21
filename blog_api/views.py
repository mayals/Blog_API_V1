from django.shortcuts import render
from rest_framework import generics
from . serializers import PostSerializer,UserSerializer
from blog.models import Post
from django.contrib.auth.models import User


class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    # permission_classes = (permissions.IsAuthenticated,)


class UserListCreateAPIView(generics.ListCreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer