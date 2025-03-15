from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    # path("about", views.about),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('loads/', views.loads, name='loads'),
    path('trips/', views.trips, name='trips'),
    path('invoices/', views.invoices_view, name='invoices_view'),
    path('expenses/', views.expenses_view, name='expenses_view'),
    path('settings/', views.settings_view, name='settings_view'),
    path('switch-eld/', views.switch_eld_view, name='switch_eld_view'),
    path('logout/', views.logout_view, name='logout'),
    path('add-planned-load/', views.add_planned_load, name='add_planned_load'),
    path('add-trip/', views.add_trip, name='add_trip'),
    path('add-expenses/', views.add_expenses, name='add_expenses'),
    path('add-invoice/', views.add_invoice, name='add_invoice'),
    path('add-maintenance/', views.add_maintenance, name='add_maintenance'),
    path('get-miles/', views.get_miles, name='get_miles'),
    path('advanced-search/', views.advanced_search, name='advanced_search'),
    path('profile/', views.profile, name='profile'),
]