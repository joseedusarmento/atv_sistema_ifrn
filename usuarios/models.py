from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    cpf = models.CharField(
        max_length=14, 
        unique=True, 
        blank=True,
        null=True,
        verbose_name="CPF",
        help_text="CPF no formato 000.000.000-00"
    )
    
    telefone = models.CharField(
        max_length=15, 
        blank=True, 
        null=True,
        verbose_name="Telefone",
        help_text="Telefone no formato (00) 00000-0000"
    )
    
    endereco = models.CharField(
        max_length=250, 
        blank=True, 
        null=True,
        verbose_name="Endereço"
    )
    
    cidade = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        verbose_name="Cidade"
    )
    
    estado = models.CharField(
        max_length=2, 
        blank=True, 
        null=True,
        verbose_name="Estado",
        help_text="Sigla do estado (ex: RN, SP, RJ)"
    )
    
    cep = models.CharField(
        max_length=9, 
        blank=True, 
        null=True,
        verbose_name="CEP",
        help_text="CEP no formato 00000-000"
    )
    
    data_nascimento = models.DateField(
        blank=True, 
        null=True,
        verbose_name="Data de Nascimento"
    )
    
    foto_perfil = models.ImageField(
        upload_to='fotos_usuarios/', 
        blank=True, 
        null=True,
        verbose_name="Foto de Perfil"
    )
    

    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de Criação"
    )
    
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name="Última Atualização"
    )
    
    ativo = models.BooleanField(
        default=True,
        verbose_name="Usuário Ativo"
    )
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['first_name', 'last_name']
    
    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    def get_nome_completo(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    def get_endereco_completo(self):
        endereco_parts = []
        if self.endereco:
            endereco_parts.append(self.endereco)
        if self.cidade:
            endereco_parts.append(self.cidade)
        if self.estado:
            endereco_parts.append(self.estado)
        if self.cep:
            endereco_parts.append(f"CEP: {self.cep}")
        
        return ", ".join(endereco_parts) if endereco_parts else "Endereço não informado"


class GrupoUsuario(models.Model):
  
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Grupo")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    usuarios = models.ManyToManyField(
        CustomUser, 
        blank=True, 
        related_name='grupos_personalizados',
        verbose_name="Usuários"
    )
    ativo = models.BooleanField(default=True, verbose_name="Grupo Ativo")
    
    class Meta:
        verbose_name = "Grupo de Usuário"
        verbose_name_plural = "Grupos de Usuários"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
