from django.conf.urls import url

from system import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^getUserList$', views.getUserList, name="users-list"),
    url(r'^getUserById$', views.getUserById, name="user-info"),
    url(r'^getRoleList$', views.getRoleList, name="roles-list"),
    url(r'^getRoleByUserId$', views.getRoleByUserId, name="user-roles-list"),
    url(r'^getRoleById$', views.getRoleById, name="role-info"),
    url(r'^getMenuList$', views.getMenuList, name="menus-list"),
    url(r'^getMenuByUserId$', views.getMenuByUserId, name="user-menus-list"),
    url(r'^getMenuById$', views.getMenuById, name="menu-info"),
    # 登陆
    url(r'^userLogin$', views.userLogin, name="user-login"),
    url(r'^getUserMenu$', views.getUserMenu, name="get-user-menu"),
    url(r'^getI18n$', views.getI18n, name="get-i18n"),
]