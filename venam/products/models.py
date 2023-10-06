from django.db import models
from django.core.validators import MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images')

    def __str__(self):
        return self.name
    
    def get_product_count(self):
        return self.products.all().count()

class TypeCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return f"{', '.join(category.name for category in self.category.all())}: {self.name}"



class SubTypeCategory(models.Model):
    name = models.CharField(max_length=100)
    type_category = models.ManyToManyField(TypeCategory, related_name='type_categories')

    def __str__(self):
        return f"{', '.join(type_category.name for type_category in self.type_category.all())}: {self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name


class Size(models.Model):
    cloth_size = models.CharField(max_length=50, blank=True)
    shoes_size = models.CharField(max_length=20, blank=True)
    
    def __str__(self) -> str:
        return self.cloth_size if self.cloth_size else self.shoes_size

class Brand(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(default=0, 
                                              blank=True, 
                                              null=True,
                                              validators=[MaxValueValidator(5)])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    size = models.ManyToManyField(Size, blank=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    tag = models.ManyToManyField(Tag, related_name='products')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    type_category = models.ForeignKey(TypeCategory, on_delete=models.CASCADE, related_name='products')
    sub_type_category = models.ForeignKey(SubTypeCategory, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name 
    
    def get_main_image(self):
        return ProductImage.objects.filter(product=self, is_thumbnail=False).first()
    
    
    def get_thumbnail_images(self):
        return ProductImage.objects.filter(product=self, is_thumbnail=True)
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')
    is_thumbnail = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.product.name + "Image"
