from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

# Create your views here.
from django.shortcuts import render




# Create your views here.
def animal_list(request):
   animales = Animal.objects.all()
   return render(request, 'animales/post_list.html', {"animal_mostrar":animales})

def protectora_list(request):
   protectora = Protectora.objects.all()
   return render(request, 'animales/post_list.html', {"protectora_mostrar":protectora})

def colaborador_list(request):
   colaborador = Colaborador.objects.all()
   return render(request, 'animales/post_list.html', {"colaborador_mostrar":colaborador})