from django.contrib import admin
from .models import Fund, Manager, Investor, Investment

# Register your models here.
admin.site.register(Fund)
admin.site.register(Manager)
admin.site.register(Investor)
admin.site.register(Investment)