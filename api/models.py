from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Quiz(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    option_1=models.CharField(max_length=100)    
    option_2=models.CharField(max_length=100)
    option_3=models.CharField(max_length=100,blank=True,null=True)
    option_4=models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return str(self.question)