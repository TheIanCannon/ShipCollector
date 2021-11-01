from django.db import models
from django.urls import reverse

# Create your models here.
class Ship(models.Model):  # Note that parens are optional if not inheriting from another class
	name = models.CharField(max_length=100)
	ship_type = models.CharField(max_length=100)
	registry = models.CharField(max_length=100)
	length = models.IntegerField()				
	description = models.TextField(max_length=250)
					
	def __str__(self):
		return f'({self.id}) - {self.name}'

def get_absolute_url(self):
		return reverse('detail', kwargs={'ship_id': self.id})