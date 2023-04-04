from rest_framework import serializers
from products.models import Product
from datetime import date

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

   