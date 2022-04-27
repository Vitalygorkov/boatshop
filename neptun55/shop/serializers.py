from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from shop.models import Product, Category, Boat


class ProductSerializer(ModelSerializer):
    product_abs_url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['name', 'image','manufacturer', 'price', 'sale', 'color', 'recommendations', 'accessories', 'category', 'slug']
        # fields = '__all__'
    def get_product_abs_url(self, obj):
        return obj.get_absolute_url()

class BoatSerializer(ModelSerializer):
    product_abs_url = serializers.SerializerMethodField()
    class Meta:
        model = Boat
        # fields = ['name', 'image', 'price', 'slug']
        fields = '__all__'
    def get_product_abs_url(self, obj):
        return obj.get_absolute_url()

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        # fields = ['name', 'image', 'price', 'slug']
        fields = '__all__'