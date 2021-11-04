from django.urls import reverse
from django.db import models
from datetime import date
from django.contrib.auth.models import User

SUPPLIES=(('F', 'Fuel Pellets'),
('W', 'Water'),
('O', 'Oxygen'),
('M', 'Food/Medicines/Filters/Tools'),)

# Create your models here.
class Equipment(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=150)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('equipment_detail', kwargs={'pk': self.id})

class Ship(models.Model):  # Note that parens are optional if not inheriting from another class
		name = models.CharField(max_length=100)
		ship_type = models.CharField(max_length=100)
		registry = models.CharField(max_length=100)
		length = models.IntegerField()				
		description = models.TextField(max_length=250)
		equipment = models.ManyToManyField(Equipment)
		user = models.ForeignKey(User, on_delete=models.CASCADE)

		def __str__(self):
			return f'({self.id}) - {self.name}'

		def get_absolute_url(self):
				return reverse('detail', kwargs={'ship_id': self.id})

		def resupplied_for_today(self):
			 return self.resupply_set.filter(date=date.today()).count() >= len(SUPPLIES)  

class Resupply(models.Model):
		date=models.DateField('Resupply Date')
		supply = models.CharField(
			'Resupply Type', 
			max_length=1, 
			choices=SUPPLIES, 
			default=SUPPLIES[0][0])

		ship = models.ForeignKey(Ship, on_delete=models.CASCADE)

		def __str__(self):
				return f"{self.get_supply_display()} on {self.date}"

		class Meta:
				ordering = ['-date']

class Photo(models.Model):
		url=models.CharField(max_length=200)
		ship=models.ForeignKey(Ship, on_delete=models.CASCADE)

		def __str__(self):
				return f"Photo for ship_id:{self.ship_id}@{self.url}"