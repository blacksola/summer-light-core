from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
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
    options = serializers.CharField()

class RoleSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=32)
    code = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    sort = serializers.IntegerField()
    status = serializers.IntegerField()
    add_date = serializers.DateTimeField()
    update_date = serializers.DateTimeField()
    remark = serializers.CharField()
    options = serializers.CharField()

class MenuSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=32)
    code = serializers.CharField(max_length=100)
    parent_code = serializers.CharField(max_length=100)
    path = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=100)
    category = serializers.IntegerField()
    sort = serializers.IntegerField()
    status = serializers.IntegerField()
    add_date = serializers.DateTimeField()
    update_date = serializers.DateTimeField()
    remark = serializers.CharField()
    options = serializers.CharField()