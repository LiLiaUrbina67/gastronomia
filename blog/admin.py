from django.contrib import admin
from .models import *


#admin.site.register(nombre_de_su_modelo)


class CelebridadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'autor', 'f_pub')
    readonly_fields = ['f_pub']
    ordering = ['-f_pub']

admin.site.register(Categoria)
admin.site.register(Celebridad, CelebridadAdmin)

