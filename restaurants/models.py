from django.db import models

# Create your models here.
class restaurants(models.Model):
	name = models.CharField(max_length=15)
	description = models.CharField(max_length=20)
	opening_time= models.DateField()
	closing_time= models.DateField()

	def __str__(self):
		return self.name
	
