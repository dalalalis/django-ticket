from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from .serializers import RegistrationSerializer,LoginSerializer

# Create your views here.

class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer

class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self,request):
        my_data = request.data
        serializer = LoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
      
