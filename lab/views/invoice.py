from django.shortcuts import render
from lab.forms.customer import CustomerForm
from lab.forms.doctor import DoctorForm
from lab.models.customer import Customer
from lab.models.agent import Doctor


def invoice(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        return render(request, 'lab/invoice.html')
    else:
        c_form = CustomerForm()
        d_form = DoctorForm()
        customers = Customer.objects.order_by('-id').all()
        doctors = Doctor.objects.order_by('-id').all()

        context={
            'c_form': c_form, 
            'd_form': d_form,
            'customers': customers,
            'doctors': doctors,
        }
        return render(request, 'lab/invoice.html', context)
    
