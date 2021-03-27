from django.contrib import admin
from .models import Pengguna, Blog

# Register your models here.
admin.site.register(Pengguna)
admin.site.register(Blog)