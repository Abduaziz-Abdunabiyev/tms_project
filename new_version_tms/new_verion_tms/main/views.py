from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def planned_loads(request):
    return render(request, 'main/planned_loads.html')
