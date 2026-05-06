# 📧 School Email Lookup

Uma ferramenta moderna para alunos localizarem seus e-mails institucionais rapidamente, com interface responsiva, busca funcional, e proteção de dados sensíveis.

## ✨ Funcionalidades

- 🔍 **Busca Inteligente**: Procure por nome ou e-mail (case-insensitive, sem acentos)
- ⚡ **Loading Animado**: Feedback visual durante a busca
- ❌ **Not Found Page**: Página amigável quando nenhum resultado é encontrado
- 📋 **Copy to Clipboard**: Botão para copiar e-mail com confirmação visual
- 🎨 **Design Responsivo**: Funciona perfeitamente em mobile e desktop
- 🔒 **Dados Protegidos**: Arquivo de alunos não é exposto no repositório público
- 🚀 **Deploy Facilitado**: Pronto para Vercel com um clique

## 🏗️ Arquitetura

```
School Email Lookup
├── Frontend (HTML/JavaScript + Tailwind CSS)
│   ├── index.html (Landing page - busca)
│   └── search.html (Resultados - com loading/not found)
│
├── Backend (Vercel Functions - Node.js)
│   └── api/search.js (API de busca segura)
│
└── Dados (Protegido)
    └── alunos2.json (Não commitado - .gitignore)
```

## 🚀 Quick Start (Local)

### 1. Executar com Servidor Python

```bash
# Na pasta do projeto
python dev_server.py 8000

# Abra no navegador
http://localhost:8000
```

### 2. Testar a API

```bash
# Terminal (Git Bash, WSL ou similar)
curl "http://localhost:8000/api/search?query=BEATRIZ"
```

## 📦 Deploy no Vercel

### Pré-requisitos:
- Conta no [Vercel](https://vercel.com) (grátis)
- Repositório no [GitHub](https://github.com) (público)

### Passo 1: Preparar repositório

```bash
# 1. Crie um repositório Git
git init
git add .
git commit -m "Initial commit - School Email Lookup"

# 2. Crie repositório no GitHub e faça push
git remote add origin https://github.com/SEU_USER/SEU_REPO.git
git branch -M main
git push -u origin main
```

### Passo 2: Deploy no Vercel

**Opção A: Automático (Recomendado)**
1. Acesse [vercel.com](https://vercel.com)
2. Clique em "New Project"
3. Selecione seu repositório do GitHub
4. Clique em "Import"
5. Vercel detectará automaticamente a configuração

**Opção B: CLI**

```bash
# Instalar Vercel CLI
npm install -g vercel

# Fazer deploy
cd /caminho/do/projeto
vercel --prod
```

### Passo 3: Adicionar dados dos alunos

Após o deploy, você precisa adicionar o arquivo `alunos2.json`:

**Via Vercel Dashboard (Recomendado):**
1. Vá para seu projeto no Vercel
2. Settings → Environment Variables
3. Crie uma nova variável ou upload do arquivo
4. Reinicie o deployment

**Ou copie o arquivo direto para a pasta raiz do servidor Vercel**

## 🔐 Segurança & Privacidade

### O que NÃO é commitado (está em `.gitignore`):
- ❌ `alunos2.json` - Dados dos alunos
- ❌ `alunos.json` - Dados auxiliares
- ❌ `alunosLeft.json` - Dados temporários
- ❌ `.env` e `.env.local` - Variáveis sensíveis

### Como os dados são protegidos:
1. **Arquivo ignorado no Git**: Não aparece no repositório público
2. **API no servidor**: Requisições são processadas no backend (não no cliente)
3. **Sem cache público**: Headers HTTP impedem caching de dados sensíveis
4. **CORS configurado**: Apenas o próprio domínio pode fazer requisições

## 📊 API Reference

### Endpoint: GET `/api/search`

**Parâmetros:**
- `query` (string, obrigatório) - Termo de busca (nome ou e-mail)

**Exemplo:**
```bash
GET /api/search?query=joão silva
```

**Resposta (200 OK):**
```json
{
  "success": true,
  "query": "joão silva",
  "total": 2,
  "results": [
    {
      "nome": "JOÃO SILVA SANTOS",
      "email": "joao.silva@aluno.educacao.pe.gov.br"
    }
  ]
}
```

## 📋 Formato do arquivo `alunos2.json`

```json
[
  {
    "nome": "JOÃO SILVA SANTOS",
    "email": "joao.silva@aluno.educacao.pe.gov.br"
  },
  {
    "nome": "MARIA OLIVEIRA",
    "email": "maria.oliveira@aluno.educacao.pe.gov.br"
  }
]
```

## 🛠️ Estrutura de Pastas

```
EmailsProject/
├── public/                 # Arquivos estáticos (front-end)
│   ├── index.html         # Página inicial
│   └── search.html        # Página de resultados
│
├── api/                    # Vercel Functions (back-end)
│   └── search.js          # API de busca
│
├── alunos2.json           # ⚠️ NÃO COMMITADO (dados sensíveis)
├── .gitignore             # Arquivos a ignorar no Git
├── vercel.json            # Configuração do Vercel
├── package.json           # Dependências do projeto
├── dev_server.py          # Servidor de desenvolvimento local
├── DEPLOYMENT.md          # Guia detalhado de deployment
└── README.md              # Este arquivo
```

## 🧪 Testando Localmente

### 1. Iniciar servidor de desenvolvimento

```bash
python dev_server.py 8000
```

### 2. Acessar a aplicação

- **Página inicial**: http://localhost:8000
- **Buscar**: Clique no campo de busca e informe um nome

## 🔄 Fluxo de Busca

```
1. Usuário acessa index.html
   ↓
2. Preenche o formulário com nome/email
   ↓
3. Clica em "Buscar E-mail"
   ↓
4. Redireciona para search.html?q=termo
   ↓
5. JavaScript faz GET /api/search?query=termo
   ↓
6. Backend busca em alunos2.json e retorna resultados
   ↓
7. Exibir:
   - LOADING (enquanto busca)
   - RESULTS (se encontrou)
   - NOT FOUND (se não encontrou)
```

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| "Nenhum aluno encontrado" mesmo com alunos existentes | Verifique o formato JSON dos dados |
| Servidor não inicia | Certifique-se que porta 8000 está disponível |
| Erro "alunos2.json not found" | Coloque o arquivo na raiz do projeto |
| CORS error no browser | Verifique se a API está configurada corretamente |

## 📄 Licença

MIT

---

**⚠️ LEMBRETE IMPORTANTE**: Nunca comite arquivos com dados sensíveis dos alunos!
