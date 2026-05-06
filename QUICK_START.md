# ⚡ QUICK START - School Email Lookup

## 🎯 Em 2 Minutos

### Passo 1: Inicie o Servidor Local
```bash
python dev_server.py 8000
```

Você verá:
```
🚀 Servidor rodando em http://localhost:8000
📂 Servindo arquivos de: .../public
🔍 API: http://localhost:8000/api/search?query=termo
```

### Passo 2: Abra o navegador
```
http://localhost:8000
```

### Passo 3: Teste a busca
1. Informe um nome (ex: BEATRIZ)
2. Clique em "Buscar E-mail"
3. Veja os resultados aparecer!

---

## 📤 Deploy no Vercel (5 Minutos)

### Opção A: Automático (Recomendado)

1. **Criar repositório no GitHub**
   ```bash
   git init
   git add .
   git commit -m "School Email Lookup"
   git remote add origin https://github.com/SEU_USER/SEU_REPO.git
   git push origin main
   ```

2. **Acessar Vercel**
   - Vá para https://vercel.com
   - Clique em "New Project"
   - Selecione seu repositório
   - Clique em "Import"

3. **Adicionar dados**
   - No Vercel Dashboard
   - Vá para "Settings" → "Environment Variables"
   - Upload do arquivo `alunos2.json`

4. **Pronto! 🎉**
   - Seu site está publicado
   - Compartilhe a URL

### Opção B: CLI

```bash
# Instalar Vercel CLI
npm install -g vercel

# Fazer deploy
vercel --prod
```

---

## 🔍 Testar a API

### Teste Simples (Curl)
```bash
curl "http://localhost:8000/api/search?query=BEATRIZ"
```

### Resultado Esperado
```json
{
  "success": true,
  "query": "BEATRIZ",
  "total": 1,
  "results": [
    {
      "nome": "BEATRIZ SOLARY GOMES DA COSTA beatriz.sgcost",
      "email": "beatriz.sgcosta@aluno.educacao.pe.gov.br"
    }
  ]
}
```

---

## 📁 Arquivos Importantes

| Arquivo | O quê |
|---------|-------|
| `public/index.html` | Página de busca |
| `public/search.html` | Página de resultados |
| `api/search.js` | API de busca |
| `alunos2.json` | Dados (NÃO COMMITADO) |
| `.gitignore` | Proteção de dados |
| `vercel.json` | Config Vercel |

---

## ⚙️ Customização Rápida

### Mudar Título
```html
<!-- Em public/index.html -->
<h1 class="...">Seu Título Aqui</h1>
```

### Mudar Cor Principal
```javascript
// Em public/index.html ou public/search.html
"primary-container": "#SEU_COR",  // Altere a cor aqui
```

### Mudar Campo de Busca
Edit `api/search.js` para adicionar novos campos além de `nome` e `email`.

---

## 🐛 Problemas Comuns

### ❌ "Porta 8000 em uso"
```bash
python dev_server.py 9000  # Use porta 9000
```

### ❌ "alunos2.json not found"
- Coloque o arquivo na **raiz** do projeto
- No mesmo nível de `package.json`

### ❌ "Nenhum resultado encontrado"
- Verifique o formato JSON do arquivo
- Campos devem ser: `nome` e `email`

### ❌ "CORS error"
- Recarregue a página (F5)
- Limpe o cache (Ctrl+Shift+Delete)

---

## 📚 Documentação Completa

- 📖 **README.md** - Documentação principal
- 📖 **DEPLOYMENT.md** - Guia de deploy detalhado
- 📖 **SETUP_GUIDE.md** - Guia de setup
- 📖 **PROJECT_SUMMARY.md** - Resumo do projeto

---

## ✅ Checklist

- [ ] Servidor local rodando (`python dev_server.py 8000`)
- [ ] Teste a busca no navegador
- [ ] Repositório criado no GitHub
- [ ] Projeto importado no Vercel
- [ ] Dados uploadados no Vercel
- [ ] Site publicado e funcionando
- [ ] URL compartilhada com usuários

---

## 🎉 Parabéns!

Seu site de busca de e-mails está 100% pronto para uso! 🚀

**Próximas melhorias (opcional):**
- [ ] Adicionar autenticação
- [ ] Adicionar paginação
- [ ] Adicionar filtros
- [ ] Adicionar analytics
- [ ] Adicionar histórico

---

**Dúvidas?** Consulte os arquivos `.md` de documentação! 📖
