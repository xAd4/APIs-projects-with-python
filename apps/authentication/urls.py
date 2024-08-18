from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterUserView

# URL patterns for the authentication API
urlpatterns = [
    # Endpoint for user registration
    path('register/', RegisterUserView.as_view(), name='register'),

    # Endpoint for user login, returns access and refresh tokens
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Endpoint for refreshing the access token using the refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
