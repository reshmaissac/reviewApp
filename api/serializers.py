from rest_framework import serializers
from products.models import Product,Category
from datetime import date

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    cost = serializers.FloatField(required=False)
    category = serializers.CharField(required=False)
    photo = serializers.URLField(required=False, source='image',read_only=True)
    brand = serializers.CharField(required=False, default='Default Brand')
    release_date = serializers.DateField(default = date.today)

    class Meta:
        model = Product
        fields = '__all__'
    
    def create(self, validated_data):
        category_name = validated_data.pop('category')
        category = Category.objects.get_or_create(name=category_name)[0]
        product = Product.objects.create(category=category, **validated_data)
        return product

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        category_name = validated_data.get('category')
        if category_name:
            category = Category.objects.get_or_create(name=category_name)[0]
            instance.category = category
        instance.save()
        return instance


   