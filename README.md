# Sistema de Gestão Acadêmica IFRN

Sistema completo de gestão acadêmica desenvolvido em Django com sistema de usuários customizado, controle de acesso e interface moderna.

## Funcionalidades Principais

### Sistema de Usuários Customizado
- Registro de usuários com campos personalizados (CPF, telefone, endereço, etc.)
- Login/Logout com autenticação segura
- Perfil de usuário editável
- Grupos de usuários e controle de acesso
- Dashboard personalizado para diferentes tipos de usuários

### Gestão Acadêmica
- Cadastro de Alunos com foto e informações completas
- Gestão de Professores
- Controle de Cursos
- Cadastro de Cidades
- Relatórios e estatísticas

### Interface Moderna
- Bootstrap 5.3 responsivo
- Font Awesome para ícones
- Dashboard interativo
- Design profissional

## Pré-requisitos

- Python 3.8 ou superior
- Django 5.2
- Pillow (para upload de imagens)
- SQLite (padrão) ou PostgreSQL

## Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/joseedusarmento/atv_sistema_ifrn.git
cd atv_sistema_ifrn
```

### 2. Crie e ative o ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário
```bash
python manage.py createsuperuser
```
**Nota**: O CPF é opcional para superusuários. Você pode deixar em branco durante a criação.

### 5.1 Há um superusuário pré-definido chamado teste, sendo a senha teste123

### 6. Execute o servidor
```bash
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000`

## Manual do Usuário

### Sistema de Autenticação

#### Fazer Login
1. Acesse `http://127.0.0.1:8000/usuarios/login/`
2. Insira seu nome de usuário e senha
3. Clique em "Entrar"

#### Criar Nova Conta
1. Na tela de login, clique em "Criar nova conta"
2. Preencha os campos obrigatórios:
   - Nome de usuário: único no sistema
   - Email: será usado para comunicações
   - Nome e Sobrenome: seu nome completo
   - CPF: documento único (formato: 000.000.000-00)
   - Telefone: opcional (formato: (00) 00000-0000)
   - Senha: mínimo 8 caracteres
3. Clique em "Criar Conta"

#### Editar Perfil
1. Faça login no sistema
2. Clique no seu nome no canto superior direito
3. Selecione "Meu Perfil"
4. Clique em "Editar Perfil"
5. Atualize as informações:
   - Dados pessoais
   - Endereço completo
   - Foto de perfil
   - Data de nascimento
6. Clique em "Salvar"

### Dashboard

#### Dashboard do Usuário
- Estatísticas pessoais
- Atalhos rápidos
- Informações do perfil

#### Dashboard Administrativo (apenas para staff)
- Total de usuários cadastrados
- Usuários ativos/inativos
- Ferramentas de gerenciamento

### Gestão Acadêmica

#### Gerenciar Alunos
1. No menu lateral, clique em "Alunos"
2. Listar: Visualize todos os alunos cadastrados
3. Adicionar: Clique em "Novo Aluno" no menu lateral
4. Editar: Clique no ícone de edição na lista
5. Excluir: Clique no ícone de exclusão (ação irreversível)

#### Gerenciar Professores
1. Acesse "Professores" no menu lateral
2. Funcionalidades similares aos alunos
3. Campos específicos para professores

#### Gerenciar Cursos
1. Clique em "Cursos" no menu lateral
2. Adicionar curso: Nome, descrição, carga horária
3. Vincular professores aos cursos

#### Gerenciar Cidades
1. Acesse "Cidades" no menu
2. Cadastre cidades para usar nos endereços
3. Organize por estado

## Funcionalidades Administrativas

### Painel de Administração Django
Acesse: `http://127.0.0.1:8000/admin/`

Funcionalidades disponíveis:
- Gestão completa de usuários
- Configuração de grupos e permissões
- Backup e restauração de dados
- Logs do sistema

### Gerenciamento de Usuários (Staff)

#### Listar Usuários
1. No menu, clique em "Gerenciar Usuários"
2. Visualize todos os usuários com:
   - Nome completo
   - Email
   - Status (ativo/inativo)
   - Data de cadastro

#### Ativar/Desativar Usuários
1. Na lista de usuários
2. Clique no botão "Ativar/Desativar"
3. Não é possível desativar sua própria conta

#### Controle de Acesso
- Usuários normais: Acesso limitado às funcionalidades básicas
- Staff: Acesso a ferramentas administrativas
- Superusuários: Acesso total ao sistema

## Segurança e Validações

### Validações Implementadas
- CPF único: Não permite CPFs duplicados
- Email único: Cada email só pode ser usado uma vez
- Senhas seguras: Validação de complexidade
- Upload seguro: Validação de arquivos de imagem

### Controle de Acesso
- Login obrigatório: Páginas protegidas requerem autenticação
- Decoradores de segurança: @login_required, @user_passes_test
- Validação de permissões: Verificação de staff para funções administrativas

## Interface Responsiva

O sistema foi desenvolvido com Bootstrap 5 e é totalmente responsivo:

- Desktop: Layout completo com sidebar
- Tablet: Menu colapsável
- Mobile: Interface otimizada para toque

## Personalização

### Temas e Cores
- Cores principais: Azul IFRN (#007bff)
- CSS customizado: `static/css/dashboard.css`
- Ícones: Font Awesome 6.4.0

### Templates
- Base: `templates/base.html`
- Usuários: `aluno/templates/usuarios/`
- Estrutura modular e extensível

## Fluxo de Trabalho Típico

### Para Novos Usuários:
1. Criar conta no sistema
2. Confirmar email (se implementado)
3. Fazer primeiro login
4. Completar perfil
5. Explorar funcionalidades

### Para Administradores:
1. Fazer login como staff
2. Acessar dashboard administrativo
3. Gerenciar usuários e permissões
4. Cadastrar dados acadêmicos
5. Monitorar estatísticas

## Troubleshooting

### Problemas Comuns

#### Erro: "UNIQUE constraint failed: usuarios_customuser.cpf"
- Causa: Tentativa de criar usuário com CPF duplicado
- Solução: Verifique se o CPF já está cadastrado ou deixe em branco para superusuários

#### CSS não carregando
- Solução: Execute `python manage.py collectstatic` (se em produção)
- Verifique: Configuração `STATIC_URL` no `settings.py`

#### Erro de permissão
- Causa: Usuário sem permissões adequadas
- Solução: Verifique se o usuário é staff/superuser no admin

#### Imagens não aparecem
- Verifique: Configuração `MEDIA_URL` e `MEDIA_ROOT`
- Solução: Confirme que o Pillow está instalado

### Logs e Debug
- Debug mode: Definido em `settings.py`
- Logs: Verifique o terminal onde o servidor está rodando
- Banco de dados: SQLite localizado na raiz do projeto

## Estrutura do Projeto

```
atv_sistema_ifrn/
├── aluno/                  # App principal do sistema acadêmico
│   ├── migrations/         # Migrações do banco
│   ├── templates/          # Templates HTML
│   │   ├── aluno/         # Templates de alunos
│   │   ├── usuarios/      # Templates de usuários
│   │   ├── curso/         # Templates de cursos
│   │   └── cidade/        # Templates de cidades
│   ├── models.py          # Modelos do sistema acadêmico
│   ├── views.py           # Views do sistema acadêmico
│   └── forms.py           # Formulários
├── usuarios/              # App do sistema de usuários
│   ├── migrations/        # Migrações de usuários
│   ├── models.py         # Modelo CustomUser
│   ├── views.py          # Views de autenticação
│   ├── forms.py          # Formulários de usuários
│   └── admin.py          # Configuração do admin
├── main/                 # Configurações do projeto
│   ├── settings.py       # Configurações principais
│   ├── urls.py           # URLs principais
│   └── wsgi.py           # WSGI config
├── static/               # Arquivos estáticos
│   └── css/
│       └── dashboard.css # CSS personalizado
├── templates/            # Templates globais
│   └── base.html         # Template base
├── media/                # Uploads de usuários
└── requirements.txt      # Dependências
```

## Contribuição

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto é desenvolvido para fins educacionais no IFRN.

## Suporte

Para dúvidas ou problemas:
- Email: silvioebis2005@gmail.com
- GitHub: [joseedusarmento](https://github.com/joseedusarmento)

---

Desenvolvido para o IFRN


Sistema de Gestão Acadêmica - Versão 1.0
