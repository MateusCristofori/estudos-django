from django.contrib import admin
from .models import Receita


class ListandoReceita(admin.ModelAdmin):
  list_display= ('id', 'nome_receita', 'categoria', 'data_receita')
  list_display_links = ('id', 'nome_receita')
  search_fields = ('nome_receita',)
  list_filter = ('categoria',)
  list_per_page = 3

admin.site.register(Receita, ListandoReceita)