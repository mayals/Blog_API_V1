from django.shortcuts import render
from rest_framework import generics
from . serializers import PostSerializer
from blog.models import Post

class PostAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
