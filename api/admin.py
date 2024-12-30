from django.contrib import admin

# Register your models here.
from .models import Product

# Register the Product model with the admin interface
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'user', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('title', 'description', 'user__username')  # Fields to be searchable
    list_filter = ('created_at', 'price')  # Add filters for better admin navigation

# Register your models here.
admin.site.register(Product, ProductAdmin)
