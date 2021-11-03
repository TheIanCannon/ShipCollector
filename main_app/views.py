from django.forms.models import fields_for_model
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Ship, Equipment
from .forms import ResupplyForm

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
				equipment_ship_doesnt_have=Equipment.objects.exclude(id__in=ship.equipment.all().values_list('id'))
				resupply_form=ResupplyForm()
				return render(request, 'ships/detail.html', {'ship': ship, 'resupply_form': resupply_form, 'equipment': equipment_ship_doesnt_have})	

def assoc_equipment(request, ship_id, equipment_id):
				Ship.objects.get(id=ship_id).equipment.add(equipment_id)
				return redirect('detail', ship_id=ship_id)


class ShipCreate(CreateView):
				model=Ship			
				fields='__all__'

class ShipUpdate(UpdateView):
				model=Ship			
				fields='__all__'

class ShipDelete(DeleteView):
				model=Ship			
				success_url='/ships/'

def add_resupply(request, ship_id):
				form=ResupplyForm(request.POST)
				if form.is_valid():
								new_resupply=form.save(commit=False)
								new_resupply.ship_id=ship_id				
								new_resupply.save()
				return redirect('detail', ship_id=ship_id)

class EquipmentList(ListView):
  model = Equipment

class EquipmentDetail(DetailView):
  model = Equipment

class EquipmentCreate(CreateView):
  model = Equipment
  fields = '__all__'

class EquipmentUpdate(UpdateView):
  model = Equipment
  fields = ['name', 'description']

class EquipmentDelete(DeleteView):
  model = Equipment
  success_url = '/equipment/'