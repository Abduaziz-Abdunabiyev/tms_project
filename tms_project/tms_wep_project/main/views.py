from django.shortcuts import render, redirect
from .forms import PlannedLoadForm


def index(request):
    return render(request, 'main/index.html')

def dashboard_view(request):
    return render(request, 'main/index.html')

def loads(request):
    return render(request, 'main/loads.html')

def trips(request):
    return render(request, 'trips.html')

def invoices_view(request):
    return render(request, 'invoices.html')

def expenses_view(request):
    return render(request, 'expenses.html')


def settings_view(request):
    return render(request, 'settings.html')

def switch_eld_view(request):
    return render(request, 'switch_eld.html')

def logout_view(request):
    return render(request, 'logout.html')

def add_planned_load(request):
    if request.method == "POST":
        form = PlannedLoadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main/loads.html')  
    else:
        form = PlannedLoadForm()
    
    return render(request, 'main/add_planned_load.html', {'form': form})


def add_trip(request):
    return render(request, 'add_trip.html')

def add_expenses(request):
    return render(request, 'add_expenses.html')

def add_invoice(request):
    return render(request, 'add_invoice.html')

def add_maintenance(request):
    return render(request, 'add_maintenance.html')

def get_miles(request):
    return render(request, 'get_miles.html')

def advanced_search(request):
    return render(request, 'advanced_search.html')

def profile(request):
    return render(request, 'profile.html')
