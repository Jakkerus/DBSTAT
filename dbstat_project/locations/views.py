from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .forms import LocationForm
from .models import locations

class LocationListView(LoginRequiredMixin, generic.ListView):
    model = locations
    context_object_name = 'locations'
    ordering = ['name']

class LocationDetailView(LoginRequiredMixin, generic.DetailView):
    model = locations
    context_object_name = 'location'

class LocationCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'locations/locations_form.html'
    form_class = LocationForm
    
class LocationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = locations
    context_object_name = 'location'
    fields = ['name', 'address', 'phone_number', 'website', 'opened']