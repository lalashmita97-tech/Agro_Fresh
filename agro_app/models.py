from django.db import models
from django.utils import timezone
# Create your models here.
## Contact Model ##
class Contact(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    phone=models.CharField(max_length=13,null=False)
    query=models.TextField(default="")
    date=models.DateField(default=timezone.now)

## Feedback Model ##
class Feedback(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    rating=models.CharField(max_length=5,null=False)
    remarks=models.TextField(default="")
    date=models.DateField(default=timezone.now)

### Farmer ###
class Farmer(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    password=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=13,null=False)
    city=models.CharField(max_length=100,null=False)
    address=models.TextField(default="")
    profile_pic=models.FileField(upload_to="farmer_pic/",default="")
    date=models.DateField(default=timezone.now)    
  
## Product ##
class Product(models.Model):
    farmer=models.ForeignKey(Farmer,on_delete=models.DO_NOTHING)
    product_category=models.CharField(max_length=100,null=False)
    product_name=models.CharField(max_length=50,null=False)            
    product_price=models.CharField(max_length=50,null=False)            
    product_pic=models.FileField(upload_to="product_pic/",default="")
    product_status=models.CharField(max_length=100,default="available")            
