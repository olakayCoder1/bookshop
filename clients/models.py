from email.header import Header
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/' , default='astro-a40.jpg')
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Items(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField( blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField( max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)



    def get_url(self):
        return self.image.url


    def __str__(self):
        return f'{self.name}  ----> {self.id}'


class OrderItem(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('delivered', 'delivered'),
        ('cancel', 'cancel')
    )
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUS, default='pending', max_length=10)

    def __str__(self):
        return f"{self.item} {self.quantity}  ----> {self.id}"

    def get_total_item_price(self):
        quantity = self.quantity
        price = self.item.price
        sum = quantity * price
        return sum


class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('delivered', 'delivered'),
        ('cancel', 'cancel')
    )

    item = models.ManyToManyField(OrderItem)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS,default='pending', max_length=10)



    def __str__(self):
        return f" ----> {self.id}"


class TransactionHeader(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('delivered', 'delivered'),
        ('cancel', 'cancel')
    )
    date_created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    shipping_address = models.TextField()
    shipping_contact = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS , default='pending')

    

class Transaction(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('delivered', 'delivered'),
        ('cancel', 'cancel')
    )
    order = models.ManyToManyField(Order)
    date_created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    items_quantity = models.PositiveIntegerField()
    total_price = models.DecimalField( max_digits=100, decimal_places=2)
    header = models.OneToOneField(TransactionHeader, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS , default='pending')