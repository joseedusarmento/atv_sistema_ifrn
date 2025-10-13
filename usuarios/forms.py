from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Nome",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Sobrenome",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    cpf = forms.CharField(
        max_length=14,
        required=True,
        label="CPF",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '000.000.000-00'
        })
    )
    
    telefone = forms.CharField(
        max_length=15,
        required=False,
        label="Telefone",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(00) 00000-0000'
        })
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'cpf', 'telefone', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email
    
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf_limpo) != 11:
            raise forms.ValidationError("CPF deve ter 11 dígitos.")
        
        if CustomUser.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está cadastrado.")
        
        return cpf


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome de usuário',
            'id': 'floatingInput'
        })
    )
    
    password = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Senha',
            'id': 'floatingPassword'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de usuário'


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'email', 'telefone',
            'endereco', 'cidade', 'estado', 'cep', 
            'data_nascimento', 'foto_perfil'
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            }),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'RN'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000-000'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control'})
        }
        
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'endereco': 'Endereço',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'cep': 'CEP',
            'data_nascimento': 'Data de Nascimento',
            'foto_perfil': 'Foto de Perfil'
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if hasattr(self, 'instance') and self.instance.pk:
            if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Este e-mail já está em uso.")
        else:
            if CustomUser.objects.filter(email=email).exists():
                raise forms.ValidationError("Este e-mail já está em uso.")
        return email


class CustomUserChangeForm(UserChangeForm):
    endereco = forms.CharField(
        max_length=250,
        required=False,
        label="Endereço",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    cidade = forms.CharField(
        max_length=100,
        required=False,
        label="Cidade",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    estado = forms.CharField(
        max_length=2,
        required=False,
        label="Estado",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'RN'
        })
    )
    
    cep = forms.CharField(
        max_length=9,
        required=False,
        label="CEP",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '00000-000'
        })
    )
    
    data_nascimento = forms.DateField(
        required=False,
        label="Data de Nascimento",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    telefone = forms.CharField(
        max_length=15,
        required=False,
        label="Telefone",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(00) 00000-0000'
        })
    )
    
    class Meta:
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name', 'email', 'cpf', 
            'telefone', 'endereco', 'cidade', 'estado', 'cep', 
            'data_nascimento', 'foto_perfil'
        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            del self.fields['password']
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
