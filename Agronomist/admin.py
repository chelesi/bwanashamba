from django.contrib import admin
from .models import Agronomist

#admin interface
admin.site.site_header = "Bwana Shamba Tz"
admin.site.site_tittle = "Admin Area"
admin.site.site_index  = "Admin Nac Technologies"

# Register your models here.
admin.site.register(Agronomist)