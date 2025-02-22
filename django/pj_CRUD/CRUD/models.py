from django.db import models

# Create your models here.
class CRUD(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    criada = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_Entrega = models.DateTimeField(null=False, blank=False)
    finalizada = models.DateTimeField(null=True)