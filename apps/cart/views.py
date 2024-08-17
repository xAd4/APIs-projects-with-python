from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

#* CATEGORY
class CategoryAPI(viewsets.ModelViewSet):
    #! Define the queryset to be used by this viewset
    queryset = Category.objects.all()
    #! Specify the serializer class for this viewset
    serializer_class = CategorySerializer

#* PRODUCT
class ProductAPI(viewsets.ModelViewSet):
    #! Define the queryset to be used by this viewset
    queryset = Product.objects.all()
    #! Specify the serializer class for this viewset
    serializer_class = ProductSerializer

#* CART AND LOGIC
class CartAPI(viewsets.ModelViewSet):
    #! Define the queryset to be used by this viewset
    queryset = Cart.objects.all()
    #! Specify the serializer class for this viewset
    serializer_class = CartSerializer

class BuyAPI(viewsets.ModelViewSet):
    #! Define the queryset to be used by this viewset
    queryset = Buy.objects.all()
    #! Specify the serializer class for this viewset
    serializer_class = BuySerializer
