from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Post
        fields = ('id','title','author','body','created_at','updated_at',)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)