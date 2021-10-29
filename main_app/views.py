from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your models and instances here
class Ship:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, registry, description):
    self.name = name
    self.type = type
    self.registry = registry
    self.description = description

ships = [
  Ship('Rocinante', 'Corvette-class light frigate', 'Tycho (Independent)', 'A Legitimate Salvage'),
  Ship('Tynan', 'Cutter-class gunship', 'Medina Station (OPAN)', 'Captain: by Klaes Ashford'),
  Ship('Kittur Chennama', 'Morrigan-class patrol destroyer', 'Mars (MCRN)', 'Destroyed in engagement with UN Navy')
]

# Create your views here
def home(request):
				return HttpResponse('<h1>Wa koming gut, beltalowda!</h1>')

def about(request):
				return render(request, 'about.html')

def ships_index(request):
  return render(request, 'ships/index.html', {'ships': ships})
