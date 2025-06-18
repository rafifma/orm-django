from django.core.validators import MinValueValidator
from django.db import models
#membuat entity dan atributnya

#relation many to many Promotion and Product
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    #products

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
    #'+' to tells django not to create reverse relationship
    
    def __str__(self) -> str:
        return self.title
    #--> to set all collection table to string
    
    class Meta:
        ordering = ['title']

class Product(models.Model):
    title = models.CharField(max_length=255) #varchar 255
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators= [MinValueValidator(1)]
        )
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    #sku (sama seperti id) = models.CharField(max_length=10, primary_key=True) (primary key) 
    # tidak apa apa jika tidak menulis sku karena django otomatis membuatkan id primary key
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion, blank=True) #blank is for in page, but null is for database
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']

#choices field    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    #kenapa tidak 'B' saja? karena jika kedepannya misal ada B lagi jadi tidak campur, bahaya jika hanya menggunakan 1 huruf untuk menyingkat, jadi di inisialisasikan
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
    
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    #kenapa menggunakan PROTECT? karena jika cutomer terhapus maka ordernya akan tetap ada, jika menggunakan cascade maka semua ordernya akan hilang

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    
#one to one relationship
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #kenapa ada customer juga disini? karena jika tidak ada customer maka tidak ada juga address, lalu ketika customer on delete maka adressnya juga akan terhapus (fungsi CASCADE)
    #kenapa harus menulis jug aprimary key? karena jika tidak maka django akan otomatis membuat (id) di setiap adress, maka itu tidak menjadi one to one field
    
    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    