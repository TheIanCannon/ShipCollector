from django.forms import ModelForm
from .models import Resupply

class ResupplyForm(ModelForm):
		class Meta:
				model=Resupply
				fields=['date', 'supply']