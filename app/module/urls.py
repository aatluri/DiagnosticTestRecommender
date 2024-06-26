from django.urls import path
from . import views

# This urls.py is a file we created specifically for this module app.
# We create a url pattern for the module app that tells Django which view to call for a particular url pattern related to this module app.
# But we also need to include all the module app urls in the main apps urls.py i.e app/urls.py
urlpatterns= [
# We are telling Django that for a /module/diagnostictestquestionaire url pattern, it should call the returndiagnostictestquestionaire view.
    path('diagnostictestquestionaire', views.returndiagnostictestquestionaire),
    path('patientinformation', views.collectpatientinformation),
    path('displaydiagnostictests', views.displaydiagnostictests),
]