from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

# Create your views here.
from django.shortcuts import render
from .models import Animal, Protectora, Colaborador



# Create your views here.
def animal_list(request):
   animales = Animal.objects.all()
   return render(request, 'animales/animal_list.html', {"animal_mostrar":animales})

def protectora_list(request):
   protectora = Protectora.objects.all()
   return render(request, 'animales/protectora_list.html', {"protectora_mostrar":protectora})

def colaborador_list(request):
   colaborador = Colaborador.objects.all()
   return render(request, 'animales/colaborador_list.html', {"colaborador_mostrar":colaborador})
