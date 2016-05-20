from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=10, blank= False)
	email= models.EmailField(null= False)
	def __str__(self):
		return(self.name)