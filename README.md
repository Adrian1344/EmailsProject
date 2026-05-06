# Extrator de Emails de PDF para JSON

Este script Python extrai nomes e emails institucionais de um arquivo PDF e os salva em um arquivo JSON.

## Instalação

1. Certifique-se de ter Python 3.7+ instalado

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

### Modo Interativo (Recomendado)
```bash
python extract_emails_from_pdf.py
```

O script solicitará:
- Caminho do arquivo PDF
- Caminho de saída para o arquivo JSON

### Exemplo Prático

Se você tem um arquivo `listagem.pdf` com dados de alunos:

```bash
python extract_emails_from_pdf.py
```

Depois digite:
- `listagem.pdf`
- `alunos.json`

## Saída Esperada

O arquivo JSON gerado terá o seguinte formato:

```json
[
  {
    "nome": "João Silva",
    "email": "joao.silva@universidade.edu.br"
  },
  {
    "nome": "Maria Santos",
    "email": "maria.santos@universidade.edu.br"
  }
]
```

## Características

- ✓ Extrai automaticamente nomes e emails do PDF
- ✓ Remove duplicatas de emails
- ✓ Suporta múltiplas páginas
- ✓ Salva em JSON com encoding UTF-8
- ✓ Tratamento de erros robusto
- ✓ Feedback em tempo real do processamento

## Personalização

Se o formato do seu PDF for diferente, você pode ajustar a regex na função `extrair_alunos_do_pdf()`:

```python
# Padrão atual (procura por emails)
match_email = re.search(r'([^@]+@[^@]+\.[a-zA-Z]{2,})', linha)
```

### Exemplos de formatos de PDF suportados:

1. **Formato: Nome seguido de email**
   ```
   João Silva joao.silva@universidade.edu.br
   Maria Santos maria.santos@universidade.edu.br
   ```

2. **Formato: Email em linha separada**
   ```
   João Silva
   joao.silva@universidade.edu.br
   ```

3. **Formato: Com números/IDs**
   ```
   001 João Silva joao.silva@universidade.edu.br
   002 Maria Santos maria.santos@universidade.edu.br
   ```

## Resolução de Problemas

### Nenhum email foi encontrado
- Verifique se o PDF contém emails
- Tente abrir o PDF com um visualizador para confirmar o formato
- Ajuste a regex se necessário

### Nomes incompletos ou incorretos
- Modifique a regex para capturar melhor o nome
- Veja a seção de Personalização acima

### Erro: ModuleNotFoundError
- Execute: `pip install -r requirements.txt`
- Certifique-se de estar no ambiente Python correto

## Exemplo de Uso Avançado

Você também pode usar o script em seu próprio código:

```python
from extract_emails_from_pdf import extrair_alunos_do_pdf, salvar_json

# Extrair dados
alunos = extrair_alunos_do_pdf('meu_pdf.pdf')

# Processar dados conforme necessário
for aluno in alunos:
    print(f"{aluno['nome']}: {aluno['email']}")

# Salvar em JSON
salvar_json(alunos, 'saida.json')
```
