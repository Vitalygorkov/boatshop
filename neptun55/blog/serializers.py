from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post, CategoryBlog, Tag

class PostSerializer(ModelSerializer):
    views_count = serializers.SerializerMethodField()
    # views = serializers.SlugRelatedField(many=True, read_only=True, slug_field='pk')
    class Meta:
        model = Post
        fields = ['title', 'views_count', 'short_description',
                  'content', 'author', 'created_ad', 'photo',
                  'category', 'tags']
        # fields = '__all__'

    def get_counts_views_simple(self, obj):
        return obj.counter_views_simple()


    def get_views_count(self, obj):
        obj.counter(self.context['request'].META['REMOTE_ADDR'])
        return obj.views.count()

class PostsSerializer(ModelSerializer):
    views_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['title', 'views_count', 'short_description',
                  'author', 'created_ad', 'photo', 'category']

    def get_views_count(self, obj):
        return obj.views.count()

class CategoryBlogSerializer(ModelSerializer):
    class Meta:
        model = CategoryBlog
        fields = "__all__"
        # fields = ["name", "parent"]

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"