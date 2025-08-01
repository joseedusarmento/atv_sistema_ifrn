from django.contrib import admin
from django.utils.html import format_html
from .models import Aluno, Cidade, Curso, Professor

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_aluno', 'endereco', 'email', 'foto_thumbnail')
    fields = ('nome_aluno', 'endereco', 'email', 'foto', 'cidade', 'curso')
    
    def foto_thumbnail(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover;" />',
                obj.foto.url
            )
        return "Sem foto"
    foto_thumbnail.short_description = 'Foto'

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla_estado',)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf','email', 'telefone', 'data_nascimento', 'especialidade','salario', 'data_contratacao', 'ativo' )
    fields = ('nome', 'cpf','email', 'telefone', 'data_nascimento', 'especialidade','salario', 'data_contratacao', 'ativo' )