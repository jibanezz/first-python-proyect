from django.db import models

# Create your models here.


class Fruit(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Student (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_number = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Alumni(models.Model):
    # get name from stundent and add passing year
    name = models.ForeignKey(Student, on_delete= models.CASCADE)
    passing_year = models.IntegerField()
    
    def __str__(self):
        return str(self.passing_year)
    