from django.db import models
# Create your models here.
class Category(models.Model):
    C_name = models.CharField(max_length=100)
    class Meta:
        db_table = "Category"
def str(self):
    return self.name
class Product(models.Model):
    P_CategoryID= models.ForeignKey(Category, on_delete=models.CASCADE)
    P_name = models.CharField(max_length=100)
    P_price = models.IntegerField()
    P_amount = models.IntegerField()
    P_description = models.CharField(max_length=100)
    P_image = models.ImageField(upload_to = 'upload/', blank = True, null = True )
    P_date = models.DateField()
    class Meta:
        db_table = "Product"
def str(self):
    return self.name
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    phoneNumber =models.IntegerField()
    class Meta:
        db_table = "User"
def str(self):
    return self.name
class Bill(models.Model):
    ProductID = models.ForeignKey(Product, on_delete= models.CASCADE)
    UserID = models.ForeignKey(User, on_delete= models.CASCADE)
    Date = models.DateField()
    class Meta:
        db_table = "Bill"
def str(self):
    return self.name
