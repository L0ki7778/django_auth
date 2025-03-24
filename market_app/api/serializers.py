from rest_framework import serializers
from market_app.models import Manufacturer, ManufacturerUser, Product


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'description', 'net_worth']

class ManufacturerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturerUser
        fields = ['manufacturer', 'user', 'role', 'joined_date']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'manufacturer', 'name', 'description', 'price']