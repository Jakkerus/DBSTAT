from django.urls import path

from . import views

app_name = 'locations'
urlpatterns = [
    path('', views.LocationListView.as_view(), name='locations-home'),
    path('new/', views.LocationCreateView.as_view(), name='locations-create'),
    path('<int:pk>/', views.LocationDetailView.as_view(), name='locations-detail'),
    path('<int:pk>/update', views.LocationUpdateView.as_view(), name='locations-update'),
]