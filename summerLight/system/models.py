from django.db import models
from common.tools import UUIDTools


# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, default=UUIDTools.uuid1_hex, editable=False, max_length=32)
    login_name = models.CharField(max_length=100, null=True, verbose_name='登录名')
    password = models.CharField(max_length=100, null=True, verbose_name='密码')
    salt = models.CharField(max_length=100, null=True, verbose_name='二次加密盐')
    nick_name = models.CharField(max_length=100, null=True, verbose_name='昵称')
    sex = models.CharField(max_length=100, null=True, verbose_name='性别')
    phone = models.CharField(max_length=100, null=True, verbose_name='手机号')
    email = models.CharField(max_length=100, null=True, verbose_name='邮箱')
    web_site = models.CharField(max_length=100, null=True, verbose_name='主页')
    register_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='注册时间')
    update_date = models.DateTimeField(auto_now=True, null=True, verbose_name='信息更新时间')
    status = models.CharField(null=True, max_length=100, verbose_name='用户状态')

    class Meta:
        ordering = ('update_date',)
