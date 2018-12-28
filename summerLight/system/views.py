from django.shortcuts import render

# Create your views here.
from system.serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from system.models import User


class UserList(APIView):

    def get(self, request, format=None):
        print(request.META.get("HTTP_SUMMER_LIGHT_TOKEN"))
        users = User.objects.all()[:10]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)