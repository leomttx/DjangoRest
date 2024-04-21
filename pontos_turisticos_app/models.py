from django.db import models
from atracoes_app.models import Atracao
from avaliacao_app.models import Avaliacao
from comentario_app.models import Comentario
from endereco_app.models import Endereco

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    avaliacoes = models.ManyToManyField(Avaliacao)
    comentarios = models.ManyToManyField(Comentario)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.nome # Retorna o nome do ponto turístico
