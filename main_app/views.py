from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import os
import boto3 
from .models import Ship, Equipment, Photo
from .forms import ResupplyForm

# Create your models and instances here

# Create your views here
def home(request):
 		 return render(request, 'home.html')

def about(request):
				return render(request, 'about.html')

@login_required
def ships_index(request):
				ships = Ship.objects.all()
				return render(request, 'ships/index.html', {'ships': ships})

@login_required
def ships_detail(request, ship_id):
				ship = Ship.objects.get(id=ship_id)
				equipment_ship_doesnt_have=Equipment.objects.exclude(id__in=ship.equipment.all().values_list('id'))
				resupply_form=ResupplyForm()
				return render(request, 'ships/detail.html', {'ship': ship, 'resupply_form': resupply_form, 'equipment': equipment_ship_doesnt_have})	

@login_required
def assoc_equipment(request, ship_id, equipment_id):
				Ship.objects.get(id=ship_id).equipment.add(equipment_id)
				return redirect('detail', ship_id=ship_id)

@login_required
def unassoc_equipment(request, ship_id, equipment_id):
				Ship.objects.get(id=ship_id).equipment.remove(equipment_id)
				return redirect('detail', ship_id=ship_id)


class ShipCreate(LoginRequiredMixin, CreateView):
				model=Ship			
				fields=['name', 'ship_type', 'registry', 'length', 'description']

				def form_valid(self, form):
						form.instance.user=self.request.user
						return super().form_valid(form)

class ShipUpdate(LoginRequiredMixin, UpdateView):
				model=Ship			
				fields='__all__'

class ShipDelete(LoginRequiredMixin, DeleteView):
				model=Ship			
				success_url='/ships/'

@login_required
def add_resupply(request, ship_id):
				form=ResupplyForm(request.POST)
				if form.is_valid():
								new_resupply=form.save(commit=False)
								new_resupply.ship_id=ship_id				
								new_resupply.save()
				return redirect('detail', ship_id=ship_id)

@login_required
def add_photo(request, ship_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, ship_id=ship_id)
    except Exception as e:
      print('An error occured uploading file to S3', e)
  return redirect('detail', ship_id=ship_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class EquipmentList(LoginRequiredMixin, ListView):
  model = Equipment

class EquipmentDetail(LoginRequiredMixin, DetailView):
  model = Equipment

class EquipmentCreate(LoginRequiredMixin, CreateView):
  model = Equipment
  fields = '__all__'

class EquipmentUpdate(LoginRequiredMixin, UpdateView):
  model = Equipment
  fields = ['name', 'description']

class EquipmentDelete(LoginRequiredMixin, DeleteView):
  model = Equipment
  success_url = '/equipment/'