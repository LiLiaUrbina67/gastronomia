from django.urls import path 

#Vista Generica -> para utilizar un archivo como si fuera una vista o view
from django.views.generic import TemplateView

from .views import *

app_name = 'blog'


urlpatterns = [  
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('celebridades', listar_Celebridad, name='listar_Celebridad'),
    path('<uuid:pub>/',ver_Celebridad, name='ver_Celebridad'),
    path('categoria/<int:categoria>/', ver_Celebridad_categoria, name='ver_Celebridad_categoria')
]     