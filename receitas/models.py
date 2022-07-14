from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from pessoas.models import Pessoas



class Receita(models.Model):
  pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE) # relacionando o models de pessoa com o models de receita!! Dentro da foreign key vamos passar a classe que queremos relacionar com a classe de receita!
  nome_receita = models.CharField(max_length=200)
  ingredientes = models.TextField()
  modo_preparo = models.TextField()
  tempo_preparo = models.IntegerField()
  rendimento = models.CharField(max_length=100)
  categoria = models.CharField(max_length=100)
  data_receita = models.DateTimeField(default=datetime.now, blank=True)