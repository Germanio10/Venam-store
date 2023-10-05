from django.contrib import admin
from .models import *
admin.site.register(SubTypeCategory)
admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(Brand)


class SubTypeCategoryInline(admin.TabularInline):
    model = SubTypeCategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubTypeCategoryInline]

@admin.register(TypeCategory)
class TypeCategoryAdmin(admin.ModelAdmin):
    inlines = [SubTypeCategoryInline]

