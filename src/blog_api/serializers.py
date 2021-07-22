from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Post
        fields = ('id','title','author','body','created_at','updated_at',)
