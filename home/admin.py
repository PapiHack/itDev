from django.contrib import admin
from .models import Visiteur
# Register your models here.

class VisiteurAdmin(admin.ModelAdmin):
    list_display = ('mel', 'date')
    list_filter = ('date',)
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('date',)

admin.site.register(Visiteur, VisiteurAdmin)
