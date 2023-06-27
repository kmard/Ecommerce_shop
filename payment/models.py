from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShippingAddress(models.Model):

    full_name = models.CharField(max_length=200)

    email = models.EmailField(max_length=255)

    address1 = models.CharField(max_length=300)

    address2 = models.CharField(max_length=300)

    city = models.CharField(max_length=255)

    #Optional
    state = models.CharField(max_length=255, null=True,blank=True)

    zipcode = models.CharField(max_length=255,null=True,blank=True)

    #FK
    #Authenticated / not authenticated users
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:

        verbose_name_plural = 'Shipping Address'


    #ShippingAddress (1)
    #ShippingAddress (2)

    def __str__(self):

        return 'Shipping Address - '+str(self.id)





