from rest_framework import serializers

from core.models import Product, ProductImage
from category.serializers import CategorySerializer
from tag.serializers import TagSerializer
from subcategory.serializers import SubCategorySerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'uploaded_at']


class ProductSerializerList(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductListFilteredResponseSerializer(serializers.Serializer):
    products = ProductSerializerList(many=True)


class ProductSerializerDetailed(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'