from django.db import models

class First(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.TextField()
    Ph_Num=models.IntegerField()
    Resume=models.FileField()
    Date_of_joining=models.DateTimeField()
    website=models.URLField(default="https:www.google.com")
    Email=models.EmailField(default="abc@gmail.com")
    password=models.IntegerField
    
    def __str__(self):
        return self.Name
    
class Replica(models.Model):
    firstdetails = models.OneToOneField(First,on_delete=models.CASCADE)
    age = models.CharField(max_length=20,null=True)
    