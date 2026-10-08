from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from spending.serializers import UserSerializer



# Create your views here.
class SignUpView(APIView):
    def post(self,request):
        form_data=request.data     #request.data contains the data sent by the client.
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            instance=User.objects.create_user(**cleaned_data)   #We use User.objects to interact with the database.
            serializer_instance=UserSerializer(instance)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        

class GetMeView(APIView):
    authentication_classes=[authentication.BasicAuthentication] #Only authenticated users can access this view.
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        auth_user=request.user
        instance=User.objects.get(username=auth_user)  #this searches the User table and gets the user whose username matches auth_user.
        serializer_instance=UserSerializer(instance)  #User object to json data
        return Response(data=serializer_instance.data)
   
