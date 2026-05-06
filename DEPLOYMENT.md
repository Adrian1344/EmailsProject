# School Email Lookup 📧

Ferramenta para alunos localizarem seus e-mails institucionais de forma fácil e rápida.

## 🚀 Funcionalidades

- ✅ Busca de alunos por nome ou e-mail
- ✅ Interface moderna e responsiva
- ✅ Loading animado durante a busca
- ✅ Página "Not Found" para buscas sem resultado
- ✅ Botão para copiar e-mail automaticamente
- ✅ Segurança: dados dos alunos protegidos (não expostos no repositório)

## 📁 Estrutura do Projeto

```
.
├── api/
│   └── search.js          # Vercel Function para busca de alunos
├── public/
│   ├── index.html         # Página inicial
│   └── search.html        # Página de resultados
├── alunos2.json           # Dados dos alunos (NÃO COMMITADO)
├── .gitignore             # Arquivo para proteger dados sensíveis
├── vercel.json            # Configuração do Vercel
├── package.json           # Dependências do projeto
└── README.md              # Este arquivo
```

## 🔒 Segurança

Os dados dos alunos (`alunos2.json`) **NÃO são commitados** no repositório. O arquivo está incluído no `.gitignore`.

### Para fazer deploy no Vercel:

1. O arquivo `alunos2.json` deve estar no servidor Vercel
2. Você pode fazer upload via:
   - **Opção 1**: Adicionar via Vercel Dashboard (melhor)
   - **Opção 2**: Variável de ambiente (se preferir)
   - **Opção 3**: Upload direto para o servidor antes do deploy

## 🛠️ Instalação Local

```bash
# 1. Clone o repositório
git clone <seu-repositorio>
cd EmailsProject

# 2. Instale as dependências (opcional, apenas para dev)
npm install

# 3. Instale o Vercel CLI
npm install -g vercel

# 4. Execute o projeto localmente
vercel dev
```

## 📤 Deploy no Vercel

### Preparação:

1. **Crie um repositório no GitHub** (sem o arquivo `alunos2.json`)
2. **Faça push do código** (exceto os dados sensíveis)
3. **Acesse o Vercel** (vercel.com) e crie uma nova project

### Deploy via GitHub:

```bash
# 1. Faça push do repositório
git push origin main

# 2. No Vercel Dashboard:
#    - Conecte seu repositório do GitHub
#    - Configure as variáveis de ambiente (se necessário)
#    - Faça deploy automático
```

### Upload do arquivo alunos2.json:

**Método 1: Via Vercel CLI (Recomendado)**
```bash
# Copie o arquivo alunos2.json para a pasta do projeto
# Execute o deploy
vercel --prod
```

**Método 2: Adicionar via Dashboard**
- Vá para Project Settings → Environment Variables
- Crie uma variável `ALUNOS_DATA` com o conteúdo JSON
- Modifique `api/search.js` para ler da variável (vide exemplo abaixo)

### Modificar API para usar variável de ambiente:

Se quiser usar variáveis de ambiente em vez de arquivo:

```javascript
// No api/search.js, substitua a leitura do arquivo por:
const alunos = JSON.parse(process.env.ALUNOS_DATA);
```

## 🎯 Como Usar

1. Abra a aplicação (http://localhost:3000 ou seu domínio Vercel)
2. Informe o nome ou e-mail do aluno
3. Clique em "Buscar E-mail"
4. Veja os resultados e copie o e-mail desejado

## 📊 API Endpoint

### GET `/api/search?query=termo`

**Resposta (200 OK):**
```json
{
  "success": true,
  "query": "termo",
  "total": 5,
  "results": [
    {
      "nome": "JOÃO SILVA",
      "email": "joao.silva@aluno.educacao.pe.gov.br"
    }
  ]
}
```

**Resposta (400 Bad Request):**
```json
{
  "error": "Query parameter is required"
}
```

## 🔧 Troubleshooting

### "Cannot find module 'fs'"
- Isso é normal em browsers. A API `fs` só funciona no servidor (api/search.js)
- Verifique se você está acessando `/api/search` corretamente

### "alunos2.json not found"
- Verifique se o arquivo está na raiz do projeto
- Certifique-se que o arquivo está uploadado no Vercel
- Verifique o path absoluto em `api/search.js`

### Busca retorna "not found" mesmo com alunos existentes
- Verifique se o formato JSON do `alunos2.json` está correto
- Os campos devem ser exatamente `nome` e `email`
- Teste com acentos e caracteres especiais

## 📝 Exemplo de alunos2.json

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

## 🤝 Contribuições

Sinta-se livre para fazer fork e enviar pull requests!

## 📄 Licença

MIT

---

**⚠️ IMPORTANTE**: Nunca comite o arquivo `alunos2.json` ou qualquer dado sensível dos alunos no repositório público!
