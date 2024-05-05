from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        reg_no = request.POST.get("Reg_No")
        dob = request.POST.get("DOB")
        
        # Replace the following URL with the endpoint of Project 1
        api_url = f'http://127.0.0.1:8000/employee/{reg_no}/{dob}/'
        
        response = requests.get(api_url)
        if response.status_code == 200:
            employee_data = response.json()
            return render(request, 'result.html', {'employee_data': employee_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch employee data. Please check the provided details.'})
    
    return render(request, 'index.html')
