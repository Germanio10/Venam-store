from .models import Category, TypeCategory, SubTypeCategory

def departments_context(request):
    categories = Category.objects.all()
    type_categories = TypeCategory.objects.all()
    sub_type_categories = SubTypeCategory.objects.all()
    context = {
        'categories': categories,
        'type_categories': type_categories,
        'sub_type_categories': sub_type_categories,
        }
    
    return context
