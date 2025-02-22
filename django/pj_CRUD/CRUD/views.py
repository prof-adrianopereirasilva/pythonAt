from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   # return HttpResponse('<h1>A Vaga é minha!!!!</h1>')
   return render(request, "CRUD/home.html")