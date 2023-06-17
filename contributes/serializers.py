from rest_framework import serializers
from . models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'userId', 'title', 'body']


class PostCreateSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    title = serializers.CharField(max_length=150)
    body = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance


class PostUpdateSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=150)
    body = serializers.CharField(max_length=1000)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

