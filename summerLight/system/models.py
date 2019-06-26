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
    options = models.TextField(null=True, verbose_name='额外配置')

    class Meta:
        ordering = ('update_date',)

class Role(models.Model):
    id = models.CharField(primary_key=True, default=UUIDTools.uuid1_hex, editable=False, max_length=32)
    code = models.CharField(max_length=100, null=True, verbose_name='角色编号')
    name = models.CharField(max_length=100, null=True, verbose_name='角色名称')
    sort = models.IntegerField(null=True, verbose_name='排序')
    status = models.IntegerField(null=True, verbose_name='角色状态')
    add_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='信息新增时间')
    update_date = models.DateTimeField(auto_now=True, null=True, verbose_name='信息更新时间')
    remark = models.TextField(null=True, verbose_name='备注')
    options = models.TextField(null=True, verbose_name='额外配置')

class Menu(models.Model):
    id = models.CharField(primary_key=True, default=UUIDTools.uuid1_hex, editable=False, max_length=32)
    code = models.CharField(max_length=100, null=True, verbose_name='菜单编号')
    parent_code = models.CharField(max_length=100, null=True, verbose_name='父菜单编号')
    path = models.CharField(max_length=200, null=True, verbose_name='请求地址')
    name = models.CharField(max_length=100, null=True, verbose_name='菜单名称')
    category = models.IntegerField(null=True, verbose_name='菜单类型')
    sort = models.IntegerField(null=True, verbose_name='排序')
    status = models.IntegerField(null=True, verbose_name='菜单状态')
    add_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='信息新增时间')
    update_date = models.DateTimeField(auto_now=True, null=True, verbose_name='信息更新时间')
    remark = models.TextField(null=True, verbose_name='备注')
    options = models.TextField(null=True, verbose_name='额外配置')

class MenuRole(models.Model):
    id = models.CharField(primary_key=True, default=UUIDTools.uuid1_hex, editable=False, max_length=32)
    role_id = models.CharField(null=True, editable=False, max_length=32)
    menu_id = models.CharField(null=True, editable=False, max_length=32)
    add_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='信息新增时间')
    update_date = models.DateTimeField(auto_now=True, null=True, verbose_name='信息更新时间')
    remark = models.TextField(null=True, verbose_name='备注')
    options = models.TextField(null=True, verbose_name='额外配置')