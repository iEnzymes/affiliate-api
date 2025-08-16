from django.contrib import admin

# Register your models here.
from .models import  Category, SubCategory, Tag, Product, ProductImage

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(ProductImage)