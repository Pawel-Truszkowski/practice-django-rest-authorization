from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class SecureView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payload = request.auth.payload
        return Response({'message': 'This is a secure view!', 'token_payload': payload})