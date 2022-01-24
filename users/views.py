from django.shortcuts import render
from rest_framework.generics import GenericAPIView
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import CustomUser
from .serializers import UserSerializer
# http://127.0.0.1:8000/rest-auth/register/
class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer=UserSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer