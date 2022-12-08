from django.shortcuts import render
from .models import CategoryBlog, Tag, Post
from rest_framework.viewsets import ModelViewSet
from blog.serializers import PostSerializer, PostsSerializer, CategoryBlogSerializer, TagSerializer

class PostsView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    http_method_names = ['get']

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get']



class CategoryBlogView(ModelViewSet):
    queryset = CategoryBlog.objects.all()
    serializer_class = CategoryBlogSerializer
    http_method_names = ['get']

class TagView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names = ['get']