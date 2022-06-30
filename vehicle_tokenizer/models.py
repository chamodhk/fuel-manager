from django.db import models


# Create your models here
class UpperCharField(models.CharField):
    def __init__(self,*args,**kwargs):
        super(UpperCharField,self).__init__(*args,**kwargs)
    def get_prep_value(self, value):
        return str(value).upper()

class Type(models.Model):
    name = models.CharField(max_length=20)
    quota = models.IntegerField()

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    reg_number = UpperCharField(max_length=20,unique=True)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)

    usage = models.IntegerField(default=0)

    
    def __str__(self):
        return self.reg_number

 