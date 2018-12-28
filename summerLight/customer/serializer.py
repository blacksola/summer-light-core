from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    sub_name = serializers.CharField(max_length=500)
    logo = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=10000)
    tags = serializers.CharField(max_length=100)
    contact = serializers.CharField(max_length=100)
    post = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    web_site = serializers.CharField(max_length=100)
    level = serializers.IntegerField()
    status = serializers.CharField(default=10)
    options = serializers.CharField(max_length=10000)
    add_date = serializers.DateTimeField()
    update_date = serializers.DateTimeField()