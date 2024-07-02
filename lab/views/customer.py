from django.http import JsonResponse
from lab.forms.customer import CustomerForm

def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()

            # Prepare a JSON serializable response
            customer_data = {
                'id': customer.id,
                'name': customer.name,
                'phone': customer.phone,
                'gender': customer.gender,
                'address': customer.address,
                'id_type': customer.id_type,
                'id_number': customer.id_number,
            }
            return JsonResponse({'success': True, 'message':'Customer added successfully!', 'customer': customer_data})
        else:
            return JsonResponse({'error': True, 'message':'Something went wrong!'})

    else:
        data = {
            'name': 'John Doe',
            'age': 30,
            'city': 'New York',
        }
        return JsonResponse(data)
    

    
    