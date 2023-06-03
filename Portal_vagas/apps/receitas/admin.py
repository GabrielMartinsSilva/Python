from django.contrib import admin

from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'titulo_vaga', 'publicada')
    list_display_links = ('id', 'titulo_vaga')
    search_fields = ('titulo_vaga',)
    list_filter = ('titulo_vaga',)
    list_editable = ('publicada',)
    list_per_page = 2

admin.site.register(Receita, ListandoReceitas)


