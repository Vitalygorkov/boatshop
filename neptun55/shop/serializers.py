from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from shop.models import Product, Category, Boat, Photo_product, VideosProducts, Color, Manufacturer

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class ProductsSerializer(ModelSerializer):
    product_abs_url = serializers.SerializerMethodField()
    manufacturer = ManufacturerSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'manufacturer', 'price', 'product_abs_url', 'sale', 'color', 'category', 'slug']
    def get_product_abs_url(self, obj):
        return obj.get_absolute_url()

class BoatsSerializer(ModelSerializer):
    product_abs_url = serializers.SerializerMethodField()
    manufacturer = ManufacturerSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    class Meta:
        model = Boat
        fields = fields = ['id', 'name', 'image', 'length', 'width', 'cockpit_length', 'cockpit_width', 'cylinder_diameter', 'fabric_thickness_bottom', 'fabric_thickness_side', 'inflatable_compartments', 'load_capacity', 'passenger_capacity', 'maximum_motor_power', 'boat_weight', 'complete_set_weight', 'bulwark', 'keel', 'upak', 'manufacturer', 'price', 'product_abs_url', 'sale', 'color', 'category', 'slug']
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
    prodimg = Photo_productSerializer(many=True, read_only=True)
    prodvideos = VideoSerializer(many=True, read_only=True)
    color = ColorSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)
    class Meta:
        model = Boat
        fields = ["id", "name", "image" ,"short_description", "description", "price", "sale", "slug", "length",
                  "width", "cockpit_length", "cockpit_width", "cylinder_diameter", "fabric_thickness_bottom",
                  "fabric_thickness_side", "inflatable_compartments", "load_capacity", "passenger_capacity",
                  "maximum_motor_power", "boat_weight", "complete_set_weight", "bulwark", "keel", "upak",
                  "manufacturer", "color", "category", "recommendations", "accessories", 'prodimg', 'prodvideos',
                  'color', 'manufacturer', 'product_abs_url']
    def get_product_abs_url(self, obj):
        return obj.get_absolute_url()

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
