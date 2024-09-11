from django.db import models
from datetime import date
# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField()
    phoneNo= models.IntegerField()
    adress= models.TextField(max_length=500)
    help= models.CharField(max_length=50)
    
    def __str__ (self):
        return self.name
    

class Products(models.Model):
    product_Name= models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcatagory = models.CharField(max_length=100)
    price =models.IntegerField(default=0)
    desc = models.CharField(max_length=100)
    images = models.ImageField(upload_to="images/images")

    def __str__(self):
        return self.product_Name
    
class Placed_orders(models.Model):
    order_id= models.IntegerField()
    product_name= models.CharField(max_length=30)
    product_price= models.IntegerField()
    product_qty= models.IntegerField()
    product_total_price= models.IntegerField()
    delivery_status=models.CharField(max_length=50,null=True,default="processing")
    orderplaced_date=models.DateField(default=date.today())
    delevired_date=models.DateField(null=True)
    
    def __str__(self):
        return self.product_name
    
    
    
  