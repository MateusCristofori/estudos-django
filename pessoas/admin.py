from pyexpat import model
from django.contrib import admin
from pessoas.models import Pessoas


class ListandoPessoa(admin.ModelAdmin):
  list_display = ('id', 'nome', 'email')
  list_display_links = ('id', 'nome')
  search_fields = ('nome', 'email')
  list_per_page = 3
  


admin.site.register(Pessoas, ListandoPessoa)