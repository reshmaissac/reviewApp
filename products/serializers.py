from rest_framework import serializers
from products.models import Product,Category
from datetime import date

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    cost = serializers.FloatField(required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    photo = serializers.URLField(required=True, source='image')
    brand = serializers.CharField(required=False, default='Default Brand')
    release_date = serializers.DateField(default = date.today)
    photo = serializers.ImageField(default = 'default_prod.jpg')

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


   