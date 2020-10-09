from django.shortcuts import render

from .models import *


def listar_Celebridad(request):
    news = Celebridad.objects.all().order_by('-f_pub')
    return render(request, './post/index.html', {'Celebridad':Celebridad})

def ver_Celebridad(request, pub):
    celebridad = Celebridad.objects.get(id = pub)
    return render(request, './post/ver.html', {'Celebridad':celebridad})

def ver_Celebridad_categoria(request, categoria):
    categoria = Categoria.objects.get(id = categoria)
    return render(request, './post/index.html', {'categoria':categoria})
 