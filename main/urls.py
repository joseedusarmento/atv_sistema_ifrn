
from django.contrib import admin
from django.urls import path, include
from aluno.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # URLs da app de usuários
    path('',index,name='index'),
    path('aluno/',aluno_criar,name='aluno_criar'),
    path('aluno/editar/<int:id>/',aluno_editar, name='aluno_editar'),
    path('aluno/remover/<int:id>/',aluno_remover,name='aluno_remover'),
    path('aluno/listar/',aluno_listar,name='aluno_listar'),
    path('curso/listar/', curso_listar, name='curso_listar'),
    path('curso/criar/', curso_criar, name='curso_criar'),
    path('curso/remover/<int:id>/',curso_remover,name='curso_remover'),
    path('curso/editar/<int:id>/',curso_editar,name='curso_editar'),
    path('cidade/criar/', cidade_criar, name = 'cidade_criar'),
    path('cidade/listar/', cidade_listar, name = 'cidade_listar'),
    path('cidade/remover/<int:id>/', cidade_remover, name='cidade_remover'),
    path('cidade/editar/<int:id>/',cidade_editar, name='cidade_editar'),
    path('professor/listar/',professor_listar,name='professor_listar'),
    path('professor/criar/',professor_criar,name='professor_criar'),
    path('professor/editar/<int:id>/',professor_editar, name='professor_editar'),
    path('professor/remover/<int:id>/',professor_remover, name='professor_remover'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


