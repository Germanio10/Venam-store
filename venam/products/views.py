from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Product, Tag, Category, Size, Brand, TypeCategory
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView



class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'products/index.html', context)
    

class ProductDetailView(DetailView):
    model = Product
    template_name =  'products/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        product_id  = self.kwargs.get('product_id')
        return queryset.filter(product_id=product_id) if product_id else queryset 


class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list/product_list.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        size_id = self.kwargs.get('size_id')
        brand_id = self.kwargs.get('brand_id')
        type_category_id = self.kwargs.get('type_category_id')
        
        if category_id:
            category = Category.objects.get(pk=category_id)
            queryset = queryset.filter(category=category)
        
        if size_id:
            size = Size.objects.get(pk=size_id)
            queryset = queryset.filter(size=size)
        
        if brand_id:
            brand = Brand.objects.get(pk=brand_id)
            queryset = queryset.filter(brand=brand)
        
        if type_category_id:
            type_category = TypeCategory.objects.get(pk=type_category_id)
            queryset = queryset.filter(type_category=type_category)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sizes = Size.objects.all()
        brands = Brand.objects.all()
        context['sizes'] = sizes
        context['brands'] = brands
        return context
    