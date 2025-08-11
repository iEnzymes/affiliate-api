from django.contrib import admin

# Register your models here.
from .models import Room, RoomImage, Category, Tag, Product, ProductImage

admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(ProductImage)