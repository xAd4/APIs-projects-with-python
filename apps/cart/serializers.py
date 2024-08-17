from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        #TODO Include all fields from the Category model in the serialized representation
        fields = "__all__"
        
class ProductSerializer(serializers.ModelSerializer):
    #TODO Replace the category ID with the category name using StringRelatedField
    category = serializers.StringRelatedField() 

    class Meta:
        model = Product
        #TODO Include all fields from the Product model in the serialized representation
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    #TODO Nest ProductSerializer to include detailed product information
    products = ProductSerializer(many=True)
    #TODO Replace the owner ID with the owner's username using StringRelatedField
    owner = serializers.StringRelatedField()
    
    class Meta:
        model = Cart
        #TODO Include all fields from the Cart model in the serialized representation
        fields = "__all__"

class BuySerializer(serializers.ModelSerializer):
    #TODO Nest ProductSerializer to include detailed product information for each purchase
    products = ProductSerializer(many=True)  

    class Meta:
        model = Buy
        #TODO Include all fields from the Buy model in the serialized representation
        fields = "__all__"
