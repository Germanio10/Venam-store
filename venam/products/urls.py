from django.urls import path
from .views import ProductDetailView, ProductListView

app_name = 'products'

urlpatterns = [
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('category/product_list/<int:category_id>/', ProductListView.as_view(), name='product_list_category'),
    path('size/product_list/<int:size_id>/', ProductListView.as_view(), name='product_list_size'),
    path('sub_type/product_list/<int:sub_type_category_id>/', ProductListView.as_view(), name='product_list_sub_type'),
    path('brand/product_list/<int:brand_id>/', ProductListView.as_view(), name='product_list_brand'),
    path('type_category/product_list/<int:brand_id>/', ProductListView.as_view(), name='product_list_type'),
]