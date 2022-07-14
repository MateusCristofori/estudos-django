from django.db import models

class Pessoas(models.Model):
  nome = models.CharField(verbose_name='Digite seu nome', max_length=200)
  email = models.EmailField(max_length=200)
  def __str__(self) -> str:
    return self.nome