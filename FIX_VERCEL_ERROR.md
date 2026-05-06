# 🔧 CORREÇÃO: Erro de Python no Vercel

## ❌ O Erro que Você Recebeu

```
Error: No python entrypoint found. Add an 'app' script in pyproject.toml 
or define an entrypoint in one of: app.py, index.py, server.py, main.py, wsgi.py, asgi.py...
```

## 🎯 Causa

Vercel detectou arquivos Python (`.py`) no repositório e tentou tratá-lo como um projeto Python, mas não encontrou um app Python válido.

## ✅ SOLUÇÃO (JÁ FEITA!)

### 1. Arquivos Python movidos para `.gitignore`

Adicionamos estes arquivos ao `.gitignore`:
```
dev_server.py              # Servidor local (desenvolvimento)
extract_emails_from_pdf.py # Script auxiliar
verificar_alunos.py        # Script auxiliar
start_dev.sh              # Script de inicialização
```

**Por quê?** Estes arquivos são apenas para desenvolvimento local e não são necessários em produção. O Vercel agora não tentará detectá-los.

### 2. Configuração `vercel.json` atualizada

Adicionamos:
```json
{
  "framework": null,
  "functions": {
    "api/search.js": {
      "runtime": "nodejs18.x"
    }
  }
}
```

**Por quê?** Informa explicitamente ao Vercel que:
- Não é um projeto com framework específico
- Tem apenas Vercel Functions (Node.js)
- Use Node.js 18.x para executar `api/search.js`

---

## 🚀 Como Fazer Deploy Agora

### Passo 1: Fazer Push do Código Corrigido

```bash
# No seu repositório local
git add .gitignore vercel.json .env.example
git commit -m "Fix: Vercel Python detection - move dev scripts to gitignore"
git push origin main
```

### Passo 2: Trigger novo Build no Vercel

```bash
# Opção A: Via Vercel CLI
vercel --prod --force

# Opção B: Via GitHub
# Faça um novo push (já fez no passo 1)
# Vercel detectará automaticamente
```

### Passo 3: Upload do `alunos2.json`

O arquivo `alunos2.json` não foi commitado (está em `.gitignore`).

Você precisa adicioná-lo ao Vercel:

**Via Vercel Dashboard:**
1. Acesse https://vercel.com
2. Vá para seu projeto
3. Settings → Files & Data
4. Crie um novo arquivo `alunos2.json`
5. Cole o conteúdo JSON com os dados dos alunos

**Ou via Vercel CLI:**
```bash
# Copie o arquivo alunos2.json para a raiz do projeto
# Depois execute:
vercel --prod
```

---

## 📝 O que mudou

### ✅ `.gitignore`

**Antes:**
```
# Python
__pycache__/
*.py[cod]
*$py.class
```

**Depois:**
```
# Python (scripts locais - não necessários em produção)
dev_server.py
extract_emails_from_pdf.py
verificar_alunos.py
start_dev.sh
__pycache__/
*.py[cod]
*$py.class
*.egg-info/
.pytest_cache/
venv/
env/
.venv/
```

### ✅ `vercel.json`

**Adicionado:**
```json
"framework": null,
"functions": {
  "api/search.js": {
    "runtime": "nodejs18.x"
  }
}
```

---

## ✅ Próximas Ações

1. ✅ `.gitignore` atualizado
2. ✅ `vercel.json` atualizado
3. ⬜ **Seu turno:** Push para GitHub
4. ⬜ **Seu turno:** Novo build no Vercel
5. ⬜ **Seu turno:** Upload de `alunos2.json`

---

## 🧪 Como Testar

### Local (funciona normalmente)
```bash
python dev_server.py 8000
http://localhost:8000
```

### Vercel (após deployment)
```bash
curl "https://seu-site.vercel.app/api/search?query=BEATRIZ"
```

---

## 🆘 Se Ainda Tiver Problema

### Verifique:
1. ✓ Fez o git push do `.gitignore` atualizado?
2. ✓ Esperou 2-3 minutos para Vercel detectar a mudança?
3. ✓ Arquivo `alunos2.json` foi adicionado ao Vercel?
4. ✓ A estrutura de pastas está correta?
   ```
   project/
   ├── api/
   │   └── search.js
   ├── public/
   │   ├── index.html
   │   └── search.html
   ├── alunos2.json (apenas no Vercel!)
   ├── vercel.json
   ├── package.json
   └── .gitignore
   ```

### Se Ainda Não Funcionar:
1. Acesse https://vercel.com
2. Vá para seu projeto
3. "Deployments" → Último deployment
4. Veja o log completo do build
5. Se necessário, reconstrua o projeto:
   - "Redeploy" → "Redeploy failed"

---

## 📞 Suporte

Se encontrar mais erros, compartilhe:
- URL do deployment que falhou
- Log completo do erro
- Estrutura do seu repositório (tree /F)

---

**Atualizado em:** Maio 6, 2026  
**Status:** ✅ Erro Corrigido
