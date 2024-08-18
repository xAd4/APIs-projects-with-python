from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken

# Serializer for User model, which handles user creation and validation
class UserSerializer(serializers.ModelSerializer):
    # Custom fields for password and password confirmation
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User  # The model that this serializer is based on
        fields = ["id", "username", "email", "password", "password2"]  # Fields to include in the serialized output
        extra_kwargs = {
            "username": {"required": True},  # Make the username required
            "email": {"required": True},  # Make the email required
            "password": {"write_only": True},  # Make the password write-only (not included in serialized output)
        }

    # Validate method to ensure that password and password2 match
    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})  # Raise error if passwords don't match
        return attrs  # Return validated data if passwords match

    # Create method to handle the creation of a new user
    def create(self, validated_data):
        validated_data.pop("password2")  # Remove password2 from validated_data since it's not needed for user creation

        # Create a new user using the validated data
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user  # Return the newly created user

# Serializer that extends UserSerializer to include JWT token generation
class UserWithTokenSerializer(UserSerializer):
    token = serializers.SerializerMethodField()  # Add a token field to the serializer output

    class Meta(UserSerializer.Meta):  # Extend the Meta class from UserSerializer
        fields = UserSerializer.Meta.fields + ["token"]  # Include the token field in the serialized output

    # Method to generate JWT tokens for the user
    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)  # Generate a refresh token for the user
        return {
            'refresh': str(refresh),  # Return the refresh token as a string
            'access': str(refresh.access_token),  # Return the access token as a string
        }
