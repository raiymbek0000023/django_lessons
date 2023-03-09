from django.contrib import admin
from .models import Category, Product
# admin.site.register(Category)
# admin.site.register(Product)
# # Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'created_at', 'updated_at' )
    list_display_links=('id', 'title')
    search_fields=('title', )
    list_filter=('title', )

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display=('id', 'title','price', 'category', 'created_at', 'updated_at' )
    list_display_links=('id', 'title')
    search_fields=('title', )
    list_filter = ('title', )

    
