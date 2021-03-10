from django.contrib import admin
from .models import Pessoa

# Register your models here.
class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Pessoa, ListandoPessoas)
