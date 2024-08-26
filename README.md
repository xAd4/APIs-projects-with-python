# Authentication API

## Description

Django REST Framework Authentication API
This API provides user registration, login, and token management functionalities using Django REST Framework and Simple JWT. Follow the steps below to use the authentication features of this API.

Endpoints
1. User Registration
Endpoint: /register/
Method: POST

Use this endpoint to register a new user. Upon successful registration, the API will return the user details along with the JWT tokens (access and refresh).

Request Body:
``{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password",
  "password2": "your_password_confirmation"
}``

Response:
``{
  "id": 1,
  "username": "your_username",
  "email": "your_email@example.com",
  "token": {
    "refresh": "your_refresh_token",
    "access": "your_access_token"
  }
}``

2. User Login
Endpoint: /login/
Method: POST

Use this endpoint to log in with an existing user. The API will return a pair of JWT tokens (access and refresh) if the credentials are correct.

Request Body:
``{
  "username": "your_username",
  "password": "your_password"
}``

Response:
``{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}``

3. Token Refresh
Endpoint: /token/refresh/
Method: POST

Use this endpoint to refresh your access token using a valid refresh token.

Request Body:
``{
  "refresh": "your_refresh_token"
}``

Response:
``{
  "access": "your_new_access_token"
}``

How to Use
Register a New User:
Send a POST request to /register/ with the required fields (username, email, password, password2). If the registration is successful, you will receive a response with the user information and the JWT tokens.

Log In:
Send a POST request to /login/ with your username and password. On successful login, you will receive the access and refresh tokens.

Refresh Token:
To refresh your access token, send a POST request to /token/refresh/ with the refresh token received during login or registration. You will receive a new access token in the response.

Example Using cURL

Register a New User
``curl -X POST http://your-domain.com/register/ \
-H "Content-Type: application/json" \
-d '{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password",
  "password2": "your_password_confirmation"
}'``


Log In
``curl -X POST http://your-domain.com/login/ \
-H "Content-Type: application/json" \
-d '{
  "username": "your_username",
  "password": "your_password"
}'``

Refresh Token
``curl -X POST http://your-domain.com/token/refresh/ \
-H "Content-Type: application/json" \
-d '{
  "refresh": "your_refresh_token"
}'``
