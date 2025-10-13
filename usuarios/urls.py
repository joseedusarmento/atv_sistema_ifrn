from django.urls import path
from . import views

urlpatterns = [
    # Autenticação
    path('login/', views.CustomLoginView.as_view(), name='usuario_login'),
    path('logout/', views.CustomLogoutView.as_view(), name='usuario_logout'),
    path('registro/', views.registro_usuario, name='usuario_registro'),
    
    # Perfil do usuário
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('dashboard/', views.dashboard_usuario, name='dashboard_usuario'),
    
    # Gerenciamento de usuários (apenas para staff)
    path('listar/', views.listar_usuarios, name='listar_usuarios'),
    path('ativar-desativar/<int:user_id>/', views.ativar_desativar_usuario, name='ativar_desativar_usuario'),
]