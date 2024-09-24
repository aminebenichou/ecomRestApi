from rest_framework import serializers
from .models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Seller
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields='__all__'

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model= Paiement
        fields='__all__'




