from django.conf.urls import url

from system.views import UserList
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'users/$', UserList.as_view(), name="users-list")
]