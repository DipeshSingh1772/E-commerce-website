from django.db import models

# Create your models here.
class product(models.Model):
      product_id=models.AutoField
      product_name=models.CharField(max_length=50)
      product_price=models.IntegerField()

def __str__(self):
   return self.product_name
         
     


