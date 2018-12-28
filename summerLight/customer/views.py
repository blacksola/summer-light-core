from django.shortcuts import render

# Create your views here.
from customer.serializer import CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import Customer


class CustomerList(APIView):

    def get(self, request, format=None):
        print(request.META.get("HTTP_SUMMER_LIGHT_TOKEN"))
        customers = Customer.objects.all()[:10]
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)


class CustomerObj(APIView):

    def get(self, request, format=None):
        print(request.META.get("HTTP_SUMMER_LIGHT_TOKEN"))
        id = request.query_params['id']
        customer = Customer.objects.get(id=str(id))
        serializer = CustomerSerializer(customer, many=False)
        return Response(serializer.data)