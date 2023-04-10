from django.db import models

# Create your models here.

class Department(models.Model):
      name= models.CharField(max_length=120,null=False)
      
      def __str__(self) -> str:
            return self.name
      


class Role(models.Model):
      name= models.CharField(max_length=120,null=False)
      def __str__(self) -> str:
            return self.name
      


class Year(models.Model):
      year = models.CharField(max_length=100,null=False)
      def __str__(self) -> str:
            return self.year


     




class Person(models.Model):
      first_name = models.CharField(max_length=150,null=False)
      last_name = models.CharField(max_length=150)
      dept = models.ForeignKey(Department, on_delete=models.CASCADE)
      year = models.ForeignKey(Year,on_delete=models.CASCADE)
      role =models.ForeignKey(Role, on_delete=models.CASCADE )
      phone =models.BigIntegerField(default=0)

      def __str__(self) -> str:
            return "%s %s "%(self.first_name,self.last_name)