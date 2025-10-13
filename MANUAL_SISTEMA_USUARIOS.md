# Manual do Sistema de Usuários - Sistema IFRN

## Visão Geral

Este manual descreve como usar o Sistema de Usuários implementado no Sistema IFRN. O sistema permite gerenciar usuários com informações personalizadas, controle de acesso e autenticação segura.

## Funcionalidades Implementadas

### 1. Modelo de Usuário Customizado

O sistema utiliza um modelo de usuário personalizado que estende o modelo padrão do Django com os seguintes campos adicionais:

- **CPF**: Campo único e obrigatório
- **Telefone**: Campo opcional para contato
- **Endereço**: Endereço completo do usuário
- **Cidade**: Cidade onde reside
- **Estado**: Sigla do estado (ex: RN, SP, RJ)
- **CEP**: Código postal
- **Data de Nascimento**: Data de nascimento do usuário
- **Foto de Perfil**: Imagem do usuário
- **Campos de Controle**: Data de criação, última atualização e status ativo

### 2. Sistema de Autenticação

#### 2.1 Login de Usuários
- **URL**: `/usuarios/login/`
- **Template**: `usuarios/login.html`
- **Funcionalidades**:
  - Login com nome de usuário e senha
  - Mensagens de feedback para sucesso/erro
  - Redirecionamento automático após login
  - Link para criar nova conta

#### 2.2 Logout de Usuários
- **URL**: `/usuarios/logout/`
- **Funcionalidades**:
  - Logout automático
  - Mensagem de confirmação
  - Redirecionamento para página de login

#### 2.3 Registro de Novos Usuários
- **URL**: `/usuarios/registro/`
- **Template**: `usuarios/registro.html`
- **Campos Obrigatórios**:
  - Nome de usuário
  - Nome e sobrenome
  - E-mail (único)
  - CPF (único, validado)
  - Senha (com confirmação)
- **Campos Opcionais**:
  - Telefone

### 3. Gerenciamento de Perfil

#### 3.1 Visualizar Perfil
- **URL**: `/usuarios/perfil/`
- **Template**: `usuarios/perfil.html`
- **Funcionalidades**:
  - Visualização de todas as informações do usuário
  - Foto de perfil (se disponível)
  - Informações pessoais e de contato
  - Endereço completo
  - Ações rápidas para navegação

#### 3.2 Editar Perfil
- **URL**: `/usuarios/perfil/editar/`
- **Template**: `usuarios/editar_perfil.html`
- **Campos Editáveis**:
  - Nome e sobrenome
  - E-mail
  - Telefone
  - Data de nascimento
  - Foto de perfil
  - Endereço completo (rua, cidade, estado, CEP)

### 4. Dashboard Personalizado

#### 4.1 Dashboard do Usuário
- **URL**: `/usuarios/dashboard/`
- **Template**: `usuarios/dashboard.html`
- **Funcionalidades para Usuários Comuns**:
  - Visualização resumida do perfil
  - Ações rápidas (editar perfil, ver alunos, etc.)
  - Informações da conta

#### 4.2 Dashboard Administrativo
- **Funcionalidades para Staff**:
  - Estatísticas do sistema (total de usuários, ativos/inativos)
  - Links de gerenciamento
  - Acesso ao painel administrativo

### 5. Gerenciamento de Usuários (Apenas Staff)

#### 5.1 Listar Usuários
- **URL**: `/usuarios/listar/`
- **Template**: `usuarios/listar_usuarios.html`
- **Funcionalidades**:
  - Lista paginada de todos os usuários
  - Informações básicas (nome, e-mail, CPF, status)
  - Identificação de administradores
  - Ações de gerenciamento

#### 5.2 Ativar/Desativar Usuários
- **URL**: `/usuarios/ativar-desativar/<id>/`
- **Funcionalidades**:
  - Alternância do status ativo/inativo
  - Proteção contra auto-desativação
  - Confirmação de ação

### 6. Controle de Acesso

O sistema implementa diferentes níveis de acesso:

#### 6.1 Usuários Não Autenticados
- Podem acessar apenas páginas de login e registro
- Redirecionamento automático para login ao tentar acessar páginas protegidas

#### 6.2 Usuários Autenticados
- Acesso a todas as funcionalidades básicas do sistema
- Podem gerenciar seu próprio perfil
- Acesso a alunos, professores, cursos e cidades

#### 6.3 Usuários Staff
- Todos os acessos de usuários comuns
- Gerenciamento de outros usuários
- Acesso ao dashboard administrativo
- Acesso ao painel admin do Django

## Como Usar o Sistema

### 1. Primeiro Acesso

1. **Criar Superusuário** (via terminal):
   ```bash
   python manage.py createsuperuser
   ```

2. **Acessar o Sistema**:
   - Navegue para `http://localhost:8000/usuarios/login/`
   - Faça login com as credenciais do superusuário

### 2. Cadastrar Novos Usuários

1. **Via Interface Web**:
   - Acesse `/usuarios/registro/`
   - Preencha o formulário com as informações obrigatórias
   - Clique em "Criar Conta"

2. **Via Admin Django** (apenas para staff):
   - Acesse `/admin/`
   - Vá em "Usuários" → "Adicionar"

### 3. Gerenciar Usuários (Staff)

1. **Listar Usuários**:
   - Acesse "Usuários" no menu lateral (visível apenas para staff)
   - Ou navegue para `/usuarios/listar/`

2. **Ativar/Desativar Usuário**:
   - Na lista de usuários, clique no botão de ativar/desativar
   - Confirme a ação

### 4. Gerenciar Perfil Pessoal

1. **Visualizar Perfil**:
   - Clique no seu nome no menu superior
   - Selecione "Meu Perfil"

2. **Editar Perfil**:
   - No perfil, clique em "Editar Perfil"
   - Atualize as informações desejadas
   - Clique em "Salvar Alterações"

## Configurações Importantes

### 1. Configurações no settings.py

```python
# Modelo de usuário customizado
AUTH_USER_MODEL = 'usuarios.CustomUser'

# URLs de redirecionamento
LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/usuarios/login/'
```

### 2. Dependências

- **Pillow**: Necessário para upload de imagens
- **Django**: Framework principal
- **Bootstrap**: Para interface responsiva

### 3. Estrutura de Arquivos

```
sistema_ifrn/
├── usuarios/
│   ├── models.py          # Modelo CustomUser
│   ├── forms.py           # Formulários de usuário
│   ├── views.py           # Views de autenticação
│   ├── urls.py            # URLs da aplicação
│   └── admin.py           # Configuração do admin
├── aluno/templates/usuarios/  # Templates dos usuários
│   ├── login.html
│   ├── registro.html
│   ├── perfil.html
│   ├── editar_perfil.html
│   ├── dashboard.html
│   └── listar_usuarios.html
└── templates/
    └── base.html          # Template base atualizado
```

## Segurança

### 1. Validações Implementadas

- **CPF**: Validação de formato e unicidade
- **E-mail**: Validação de formato e unicidade
- **Senhas**: Validação padrão do Django
- **Acesso**: Decoradores de autenticação em todas as views protegidas

### 2. Proteções

- **CSRF**: Proteção automática em todos os formulários
- **Login Required**: Todas as views protegidas exigem autenticação
- **Staff Required**: Funcionalidades administrativas restritas

## Troubleshooting

### 1. Problemas Comuns

**Erro: "No module named 'Pillow'"**
- Solução: `pip install Pillow`

**Erro: "AUTH_USER_MODEL refers to model 'usuarios.CustomUser' that has not been installed"**
- Solução: Execute `python manage.py migrate`

**Usuários não conseguem fazer upload de imagens**
- Verifique se MEDIA_URL e MEDIA_ROOT estão configurados
- Verifique se o Pillow está instalado

### 2. Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations usuarios

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

## Extensões Futuras

O sistema foi projetado para ser facilmente extensível. Possíveis melhorias:

1. **Grupos de Usuários**: Sistema de permissões mais granular
2. **Reset de Senha**: Funcionalidade de recuperação por e-mail
3. **Perfis Sociais**: Integração com redes sociais
4. **Auditoria**: Log de ações dos usuários
5. **API REST**: Endpoints para integração com outras aplicações

## Suporte

Para dúvidas ou problemas:
1. Consulte a documentação do Django
2. Verifique os logs do sistema
3. Entre em contato com o administrador do sistema

---

**Versão do Manual**: 1.0
**Última Atualização**: Outubro 2025
**Sistema**: Django 5.2