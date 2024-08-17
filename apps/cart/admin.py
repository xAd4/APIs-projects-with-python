from django.contrib import admin
from .models import *

# Register your models here.

#* Config ReadOnlyFields
class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    
#* Model Register
admin.site.register(Category, ReadOnlyFields)
admin.site.register(Product, ReadOnlyFields)
admin.site.register(Cart, ReadOnlyFields)

#* Config and register model Buy
class BuyAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "total_price")

admin.site.register(Buy, BuyAdmin)
