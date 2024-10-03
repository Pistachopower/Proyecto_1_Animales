from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

# Create your views here.
from django.shortcuts import render




# Create your views here.
def post_list(request):
   animales = Animal.objects.all()
   return render(request, 'blog/post_list.html', {"posts_mostrar":animales})

def post_list2(request):
   protectora = Protectora.objects.all()
   return render(request, 'blog/post_list.html', {"posts_mostrar":protectora})

def post_list3(request):
   colaborador = Colaborador.objects.all()
   return render(request, 'blog/post_list.html', {"posts_mostrar":colaborador})