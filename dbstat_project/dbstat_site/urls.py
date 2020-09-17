"""dbstat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from contacts import views as contact_views
from dbstat_site import views as homepage_views

urlpatterns = [
    path('', homepage_views.index, name='homepage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('assets/', include('assets.urls')),
    path('locations/', include('locations.urls')),
    path('profile/', contact_views.profile, name='profile'),
    path('register/', contact_views.register, name='register'),
    path('tickets/', include('tickets.urls'))
]