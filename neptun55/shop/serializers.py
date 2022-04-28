from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from shop.models import Product, Category, Boat, Photo_product, VideosProducts, Color, Manufacturer


class ProductsSerializer(ModelSerializer):
    product_abs_url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'image','manufacturer', 'price', 'product_abs_url', 'sale', 'color', 'category', 'slug']
    def get_product_abs_url(self, obj):
        return obj.get_absolute_url()

class VideoSerializer(ModelSerializer):
    class Meta:
        model = VideosProducts
        fields = ['video']

class Photo_productSerializer(ModelSerializer):
    class Meta:
        model = Photo_product
        fields = ['image']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    product_abs_url = serializers.SerializerMethodField()
    prodimg = Photo_productSerializer(many=True, read_only=True)
    prodvideos = VideoSerializer(many=True, read_only=True)
    color = ColorSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['name', 'image', 'short_description', 'description', 'manufacturer', 'price',
                  'sale', 'color', 'recommendations', 'accessories', 'category', 'slug',
                  'product_abs_url', 'prodimg','prodvideos']
    def get_product_abs_url(self, obj):
        return obj.get_absolute_url()

class BoatSerializer(ModelSerializer):
    product_abs_url = serializers.SerializerMethodField()
    class Meta:
        model = Boat
        fields = '__all__'
    def get_product_abs_url(self, obj):
        return obj.get_absolute_url()

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
