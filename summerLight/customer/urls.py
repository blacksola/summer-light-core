from django.conf.urls import url

from customer import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'customers/$', views.customers, name="customers-list"),
    url(r'getCustomerById/$', views.getCustomerById, name="customer-form")
]