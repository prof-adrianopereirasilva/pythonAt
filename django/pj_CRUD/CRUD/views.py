from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import CRUD

#def crud_list(request):
   # nome = " Professor Adriano Pereira"
   # alunos = ["Carla", "Andre", "Ariel", "Bruna", "Geovana", "Lorena", "Roberval", "Lena"]
   # crud = CRUD.objects.all()
   # return render(request, "CRUD/crud_list.html",{"crud":crud})

class CRUDListView(ListView):
    model = CRUD
    
class CRUDCreateView(CreateView):
    model = CRUD
    fields = ["titulo", "data_Entrega"]