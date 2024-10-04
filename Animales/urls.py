from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    #path('animal', views.animal_list, name='animal_list'),
    path("__debug__/", include("debug_toolbar.urls")),
    path('protectora/', views.protectora_list, name='protectora_list'),
    path('colaborador/', views.colaborador_list, name='colaborador_list'),
    
    
]


