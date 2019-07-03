from django.shortcuts import render

# Create your views here.
from customer.serializer import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.models import Customer


@api_view(http_method_names=['GET'])
def customers(request):
    customers = Customer.objects.all()[:10]
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def getCustomerById(request):
    id = request.query_params['id']
    customer = Customer.objects.get(id=str(id))
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)
