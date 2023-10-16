from django.contrib import admin
from products.models import (SubTypeCategory, Tag, Size, ProductImage,
                             Product, Brand, Category,
                             TypeCategory, Review)
admin.site.register(SubTypeCategory)
admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(TypeCategory)
admin.site.register(Review)
