from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, GrupoUsuario

class CustomUserAdmin(UserAdmin):
    """
    Configuração do admin para o modelo de usuário customizado
    """
    model = CustomUser
    
    # Campos a serem exibidos na lista de usuários
    list_display = [
        'username', 'email', 'first_name', 'last_name', 
        'cpf', 'telefone', 'cidade', 'is_active', 'date_joined'
    ]
    
    # Campos pelos quais é possível filtrar
    list_filter = [
        'is_active', 'is_staff', 'is_superuser', 
        'groups', 'cidade', 'estado', 'date_joined'
    ]
    
    # Campos de busca
    search_fields = ['username', 'email', 'first_name', 'last_name', 'cpf']
    
    # Campos editáveis inline
    list_editable = ['is_active']
    
    # Configuração dos fieldsets para o formulário de edição
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Pessoais Adicionais', {
            'fields': (
                'cpf', 'telefone', 'data_nascimento', 'foto_perfil'
            )
        }),
        ('Endereço', {
            'fields': (
                'endereco', 'cidade', 'estado', 'cep'
            )
        }),
        ('Configurações Adicionais', {
            'fields': (
                'ativo',
            )
        }),
    )
    
    # Campos para o formulário de criação de usuário
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Pessoais', {
            'fields': (
                'first_name', 'last_name', 'email', 'cpf', 'telefone'
            )
        }),
    )


@admin.register(GrupoUsuario)
class GrupoUsuarioAdmin(admin.ModelAdmin):
    """
    Configuração do admin para grupos de usuários personalizados
    """
    list_display = ['nome', 'descricao', 'ativo', 'quantidade_usuarios']
    list_filter = ['ativo']
    search_fields = ['nome', 'descricao']
    filter_horizontal = ['usuarios']
    
    def quantidade_usuarios(self, obj):
        """Retorna a quantidade de usuários no grupo"""
        return obj.usuarios.count()
    quantidade_usuarios.short_description = 'Qtd. Usuários'


# Registrar o modelo customizado
admin.site.register(CustomUser, CustomUserAdmin)
