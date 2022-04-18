from rest_framework.serializers import ModelSerializer

from shop.models import Product, Category


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        # fields = ['name', 'image', 'price', 'slug']
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        # fields = ['name', 'image', 'price', 'slug']
        fields = '__all__'