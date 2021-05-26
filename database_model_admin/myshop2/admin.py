from django.contrib import admin
from .models import Customer,Products

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ("created_at",)
    search_fields = ['first_name', 'phone', 'email']

class ProducitsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'catagory')
    list_filter = ('price',)
    search_fields = ['product_name', 'catagory']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Products , ProducitsAdmin)