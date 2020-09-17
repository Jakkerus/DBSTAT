from django.contrib import admin

from .models import locations, location_staff, positions, staff

admin.site.register(locations)
admin.site.register(location_staff)
admin.site.register(positions)
admin.site.register(staff)