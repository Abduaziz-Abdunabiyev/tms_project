from django.shortcuts import render
def index(request):
    return render(request, 'main/index.html')

def dashboard_view(request):
    return render(request, 'main/index.html')

def loads_trips_view(request):
    return render(request, 'loads_trips.html')

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
    return render(request, 'add_planned_load.html')

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
