from django.shortcuts import get_object_or_404, render
from .models import Product, Tag, Category, Size, Brand, TypeCategory, Review
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import ReviewForm, PriceFilterForm
from django.http import HttpResponseRedirect


class IndexView(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'products/index.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(product=self.object)
        context['tags'] = Tag.objects.all()
        context['form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            product_id = kwargs['pk']
            product = get_object_or_404(Product, pk=product_id)
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
        else:
            form = ReviewForm()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.kwargs.get('product_id')
        return queryset.filter(product_id=product_id) if product_id else queryset


class ProductListView(ListView):
    model = Product
    template_name = 'products_list/product_list.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        size_id = self.kwargs.get('size_id')
        brand_id = self.kwargs.get('brand_id')
        type_category_id = self.kwargs.get('type_category_id')
        query = self.request.GET.get('query')
        form = PriceFilterForm(self.request.GET)

        if category_id:
            category = Category.objects.get(pk=category_id)
            queryset = queryset.filter(category=category)

        if query:
            queryset = queryset.filter(name__icontains=query)

        if size_id:
            size = Size.objects.get(pk=size_id)
            queryset = queryset.filter(size=size)

        if brand_id:
            brand = Brand.objects.get(pk=brand_id)
            queryset = queryset.filter(brand=brand)

        if type_category_id:
            type_category = TypeCategory.objects.get(pk=type_category_id)
            queryset = queryset.filter(type_category=type_category)

        if form.is_valid():
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sizes = Size.objects.all()
        brands = Brand.objects.all()
        context['sizes'] = sizes
        context['brands'] = brands
        context['price_filter_form'] = PriceFilterForm(self.request.GET)
        return context
