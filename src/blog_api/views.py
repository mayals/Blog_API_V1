from django.shortcuts import render
from rest_framework import generics
from . serializers import PostSerializer
from blog.models import Post



class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)




class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    # permission_classes = (permissions.IsAuthenticated,)

