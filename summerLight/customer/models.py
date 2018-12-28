from django.db import models
from common.tools import UUIDTools


# Create your models here.
class Customer(models.Model):
    id = models.CharField(primary_key=True, default=UUIDTools.uuid1_hex, editable=False, max_length=32)
    name = models.CharField(max_length=100, null=True, verbose_name='客户简称')
    sub_name = models.CharField(max_length=500, null=True, verbose_name='客户全称')
    logo = models.CharField(max_length=100, null=True, verbose_name='客户logo')
    address = models.CharField(max_length=100, null=True, verbose_name='地址')
    description = models.TextField(null=True, verbose_name='企业描述')
    type = models.CharField(max_length=10, null=True, verbose_name='类型')
    tags = models.CharField(max_length=100, null=True, verbose_name='客户标签')
    contact = models.CharField(max_length=100, null=True, verbose_name='联系人')
    post = models.CharField(max_length=200, null=True, verbose_name='联系人岗位')
    phone = models.CharField(max_length=100, null=True, verbose_name='联系人手机号')
    email = models.CharField(max_length=100, null=True, verbose_name='联系人邮箱')
    web_site = models.CharField(max_length=100, null=True, verbose_name='主页')
    level = models.IntegerField(default=0, verbose_name='客户级别')
    status = models.CharField(max_length=100, null=True, verbose_name='客户状态')
    options = models.TextField(null=True, verbose_name='其它配置')
    add_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='录入时间')
    update_date = models.DateTimeField(auto_now=True, null=True, verbose_name='信息更新时间')

    class Meta:
        ordering = ('update_date',)