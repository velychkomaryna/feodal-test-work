from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer, RegistrationSerializer
from rest_framework.views import APIView


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


class UserLoginView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        user = authenticate(
            email=request.data["email"], password=request.data["password"]
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"error": "Invalid credentials"}, status=401)
