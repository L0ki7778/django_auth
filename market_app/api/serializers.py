from rest_framework import serializers
from market_app.models import Manufacturer, ManufacturerUser, Product


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'description', 'net_worth']

class ManufacturerUserSerializer(serializers.ModelSerializer):
    user_name = serializers.PrimaryKeyRelatedField(source='user.username', read_only=True)
    class Meta:
        model = ManufacturerUser
        fields = ['manufacturer', 'user_name', 'role', 'joined_date']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'manufacturer', 'name', 'description', 'price']
