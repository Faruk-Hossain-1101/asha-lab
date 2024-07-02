
from django.urls import path
from lab.views import invoice, console, customer, agent

urlpatterns = [
    path('', console.index, name='home'),
    path('customer/', customer.customer, name='customer'),
    path('doctor/', agent.doctor, name='doctor'),
    path('invoice/', invoice.invoice , name='console_invoice')
]