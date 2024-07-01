
from django.urls import path
from lab.views import invoice, console, customer

urlpatterns = [
    path('', console.index, name='home'),
    path('customer/', customer.customer, name='customer'),
    path('invoice/', invoice.invoice , name='console_invoice')
]