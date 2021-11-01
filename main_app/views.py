from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Ship

# Create your models and instances here

# Create your views here
def home(request):
 		 return render(request, 'home.html')

def about(request):
				return render(request, 'about.html')

def ships_index(request):
				ships = Ship.objects.all()
				return render(request, 'ships/index.html', {'ships': ships})

def ships_detail(request, ship_id):
				ship = Ship.objects.get(id=ship_id)
				return render(request, 'ships/detail.html', {'ship': ship})	

class ShipCreate(CreateView):
				model=Ship			
				fields='__all__'