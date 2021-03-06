from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class ProductList(models.Model):
    product_id = models.AutoField(primary_key=True,blank=True,null=False)
    product_name = models.CharField(max_length=100,default='') 
    category = models.CharField(max_length=50,default='')
    desc1 = models.CharField(max_length=300,default='') 
    desc2 = models.CharField(max_length=3000,default='') 
    exp_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="user/images",default="")
    discount = models.IntegerField(default=0)
    features = models.CharField(max_length=1000,default="")
    use = models.CharField(max_length=1000,default="")
    Quantity = models.IntegerField(default=0)   

    def __str__(self):
        return self.product_name

class Cart_Data(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    product = models.ForeignKey(ProductList,on_delete=models.CASCADE,default=0)
    quantity = models.PositiveIntegerField(default=0)
    cart_id = models.AutoField(primary_key=True)

class Order_Table(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=500)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=1110)
    city = models.CharField(max_length=110)
    state = models.CharField(max_length=110)
    zip_code = models.CharField(max_length=110)
    phone = models.CharField(max_length=110,default="")

class OrderUpd(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."