from django.conf.urls import url

from customer.views import CustomerList, CustomerObj
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'customers/$', CustomerList.as_view(), name="customers-list"),
    url(r'getCustomerById/$', CustomerObj.as_view(), name="customer-form")
]