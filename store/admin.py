from django.contrib import admin

from store.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass
