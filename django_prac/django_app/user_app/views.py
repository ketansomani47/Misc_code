from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.response import Response
# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework import status


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        token = Token.objects.get_or_create(user=user)
        print(token)
        return Response({"data": serializer.data})
    return Response({"data": serializer.errors})


@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"msg" : "User Logout Successfully"}, status=status.HTTP_200_OK)