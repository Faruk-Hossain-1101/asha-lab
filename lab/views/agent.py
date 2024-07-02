from django.http import JsonResponse
from lab.forms.doctor import DoctorForm

def doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save()

            # Prepare a JSON serializable response
            if doctor.discount:
                discount = {'id':doctor.discount.id, 'name':doctor.discount.name, 'type':doctor.discount.type}
            else:
                discount = ""

            doctor_data = {
                'id': doctor.id,
                'name': doctor.name,
                'expaties': doctor.expaties,
                'degree': doctor.degree,
                'address': doctor.address,
                'discount': discount,
            }
            return JsonResponse({'success': True, 'message':'Doctor added successfully!', 'doctor': doctor_data})
        else:
            return JsonResponse({'error': True, 'message':'Something went wrong!'})

    else:
        data = {
            'name': 'John Doe',
            'age': 30,
            'city': 'New York',
        }
        return JsonResponse(data)
    

    
    