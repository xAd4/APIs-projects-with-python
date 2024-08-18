from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
#* "Category" model. Allows you to save instances of new categories for products
class Category(models.Model):
    category = models.CharField(max_length=50, unique=True, verbose_name="Product category")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update date") 
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.category

#* "Product" model. Used to create instances of new products
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Product category")
    product = models.CharField(max_length=50, unique=True, verbose_name="Product")
    description = models.CharField(max_length=200, unique=True, verbose_name="Product description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product price")
    stock = models.IntegerField(verbose_name="Product stock")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update date")
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def __str__(self):
        return self.product
    
    def clean(self):
        if self.price < 0:
            raise ValidationError({'price': 'Price cannot be negative.'})
        if self.stock < 0:
            raise ValidationError({'stock': 'Stock cannot be negative.'})
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

#* "Cart" model. Allows a user to create a single cart and put the products they want inside it.
class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update date")
    
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        
    def __str__(self):
        return f"Cart Owner - {self.owner}"
    
#* "Buy" Model. It allows the user to purchase the products they want

class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Purchase user")
    products = models.ManyToManyField(Product, verbose_name="Purchased products")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total price of all products", blank=True, null=True)
    is_paid = models.BooleanField(default=False, verbose_name="Payment verification")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update date")

    class Meta:
        verbose_name = "Buy"
        verbose_name_plural = "Buys"

    def __str__(self):
        return f"Customer Purchase - {self.user}"

    def save(self, *args, **kwargs):
        #TODO: Initially save the instance so that it has an ID
        if self.pk is None:
            super().save(*args, **kwargs)

        #TODO: Calculate the total_price based on the products associated with this purchase
        self.total_price = sum(product.price for product in self.products.all())

        #TODO: Call the parent's save() method to save the instance with the updated total_price
        super().save(*args, **kwargs)
        
        