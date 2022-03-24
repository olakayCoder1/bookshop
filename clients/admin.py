from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'phone', 'joined_date']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'user_id', 'quantity']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price','created_at']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'quantity', 'status','created_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Order,OrderAdmin)