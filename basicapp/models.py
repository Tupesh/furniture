from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class FurnitureItems(models.Model):
    image = models.ImageField(upload_to='images/')
    itemName=models.CharField(max_length=50)
    grade = models.CharField(max_length=1)
    price=models.IntegerField()
    des=models.CharField( max_length=500)

    def __str__(self):
        return self.itemName+" ("+self.grade+")"


class ModularItem(models.Model):
    imageMK = models.ImageField(upload_to='images/', null=True, blank=True)
    name=models.CharField(max_length=50)
    grade = models.CharField(max_length=1)
    des=models.CharField( max_length=500)
    price=models.IntegerField()

    def __str__(self):
        return self.name+" ("+self.grade +")"

class Chaukos(models.Model):
    imageC = models.ImageField(upload_to='images/', null=True, blank=True)
    woodName=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    des=models.CharField( max_length=500)
    def __str__(self):
        return self.woodName

class Booking(models.Model):
    districtChoices=[
        ('Kathmandu',"Kathmandu"),
        ('Bhaktapur','Bhaktapur'),
        ('Lalitpur','Lalitpur')
    ]
    first_name = models.CharField(max_length=200)    
    last_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=10)
    email=models.EmailField()
    district=models.CharField(max_length=50,choices=districtChoices)
    localAddress=models.CharField(max_length=50)
    interested_item = models.CharField(max_length=100,)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

    