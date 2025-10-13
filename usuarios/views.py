from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import CustomUser
from .forms import (
    CustomUserCreationForm, CustomLoginForm, PerfilUsuarioForm
)


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        messages.success(self.request, f'Bem-vindo, {form.get_user().get_nome_completo()}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Nome de usuário ou senha incorretos.')
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('usuario_login')
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Você foi desconectado com sucesso.')
        return super().dispatch(request, *args, **kwargs)


def registro_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}! Você já pode fazer login.')
            return redirect('usuario_login')
        else:
            messages.error(request, 'Erro ao criar conta. Verifique os dados informados.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})


@login_required
def perfil_usuario(request):
    context = {
        'usuario': request.user
    }
    return render(request, 'usuarios/perfil.html', context)


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil_usuario')
        else:
            messages.error(request, 'Erro ao atualizar perfil. Verifique os dados informados.')
    else:
        form = PerfilUsuarioForm(instance=request.user)
    
    return render(request, 'usuarios/editar_perfil.html', {'form': form})


def is_staff_user(user):
    return user.is_staff or user.is_superuser


@user_passes_test(is_staff_user)
def listar_usuarios(request):
    usuarios_list = CustomUser.objects.all().order_by('date_joined')
    
    paginator = Paginator(usuarios_list, 10)
    page_number = request.GET.get('page')
    usuarios = paginator.get_page(page_number)
    
    context = {
        'usuarios': usuarios,
        'total_usuarios': usuarios_list.count()
    }
    return render(request, 'usuarios/listar_usuarios.html', context)


@user_passes_test(is_staff_user)
def ativar_desativar_usuario(request, user_id):
    usuario = get_object_or_404(CustomUser, id=user_id)
    
    if usuario == request.user:
        messages.error(request, 'Você não pode desativar sua própria conta.')
        return redirect('listar_usuarios')
    
    usuario.is_active = not usuario.is_active
    usuario.save()
    
    status = "ativado" if usuario.is_active else "desativado"
    messages.success(request, f'Usuário {usuario.get_nome_completo()} {status} com sucesso!')
    
    return redirect('listar_usuarios')


@login_required
def dashboard_usuario(request):
    if request.user.is_staff:
        total_usuarios = CustomUser.objects.count()
        usuarios_ativos = CustomUser.objects.filter(is_active=True).count()
        
        context = {
            'total_usuarios': total_usuarios,
            'usuarios_ativos': usuarios_ativos,
            'usuarios_inativos': total_usuarios - usuarios_ativos,
            'is_staff_dashboard': True
        }
    else:
        context = {
            'usuario': request.user,
            'is_staff_dashboard': False
        }
    
    return render(request, 'usuarios/dashboard.html', context)
