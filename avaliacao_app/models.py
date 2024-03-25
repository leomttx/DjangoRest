from django.db import models
from django.contrib.auth.models import User


class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Relacionamento com a tabela User
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.usuario.username
