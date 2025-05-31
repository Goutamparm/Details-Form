from django.shortcuts import render
from django.http import HttpResponse
from.models import Browser

def signup(request):
    if request.method == 'POST':
        Browser.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            residence_type = request.POST['residence_type'],
            month_income = request.POST['month_income'],
            previous_loan = request.POST['previous_loan'] == 'on',
            marital_status = request.POST['marital_status'],
            dependency = request.POST['dependency'],
            city = request.POST['city'],
            state = request.POST['state']
        )
        return HttpResponse('success')
    return render(request, 'signup.html')
    


# Create your views here.
