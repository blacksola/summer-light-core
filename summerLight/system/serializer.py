from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    login_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    salt = serializers.CharField(max_length=100)
    nick_name = serializers.CharField(max_length=100)
    sex = serializers.CharField(max_length=100)
    phone = serializers.CharField()
    email = serializers.CharField()
    web_site = serializers.CharField()
    register_date = serializers.DateTimeField()
    update_date = serializers.DateTimeField()
    status = serializers.IntegerField(default=0)
