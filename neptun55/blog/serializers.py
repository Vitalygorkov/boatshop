from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post, CategoryBlog, Tag

class PostSerializer(ModelSerializer):
    views_count = serializers.SerializerMethodField()
    counts_views_simple = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    # views = serializers.SlugRelatedField(many=True, read_only=True, slug_field='pk')
    class Meta:
        model = Post
        fields = ['id', 'title', 'views_count', 'counts_views_simple', 'short_description',
                  'content', 'author', 'author_name', 'created_ad', 'photo',
                  'category', 'tags']
        # fields = '__all__'

    def get_counts_views_simple(self, obj):
        return obj.counter_views_simple()


    def get_views_count(self, obj):
        obj.counter(self.context['request'].META['REMOTE_ADDR'])
        return obj.views.count()

    def get_author_name(self, obj):
        return obj.author.username

class PostsSerializer(ModelSerializer):
    views_count = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','title', 'views_count', 'views_simple', 'short_description',
                  'author', 'author_name', 'created_ad', 'photo', 'category', 'tags']

    def get_views_count(self, obj):
        return obj.views.count()
    def get_author_name(self, obj):
        return obj.author.username

class CategoryBlogSerializer(ModelSerializer):
    class Meta:
        model = CategoryBlog
        fields = "__all__"
        # fields = ["name", "parent"]

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"