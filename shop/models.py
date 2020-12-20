from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('author name', max_length=15)
    dob = models.DateField('author\'s date of birth')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('title', max_length=15)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    img = models.ImageField('book photo')
    price = models.PositiveSmallIntegerField('price')

    def __str__(self):
        return self.title

    def get_details(self):
        return 'product-detail/' + str(self.id)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('name', max_length=50)
    email = models.EmailField('email')


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    recepientName = models.CharField(max_length=60, null=True, default="")
    complete = models.BooleanField('complete', default=False)
    number = models.CharField(max_length=12, null=True, default=None)
    address = models.CharField(max_length=80, null=True, default=None)
    zipCode = models.CharField(max_length=8, null=True, default=None)
    comment = models.TextField(null=True, default=None)





class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField('quantity', default=0)
