from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserWithTokenSerializer

# View for registering a new user
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()  # Defines the queryset to be used for the view
    permission_classes = [AllowAny]  # Allows any user, authenticated or not, to access this view
    serializer_class = UserWithTokenSerializer  # Specifies the serializer to be used for creating a new user
