import json

# Carregar arquivos JSON
with open('alunos.json', 'r', encoding='utf-8') as f:
    alunos1 = json.load(f)

with open('alunos2.json', 'r', encoding='utf-8') as f:
    alunos2 = json.load(f)

# Extrair emails de alunos2 para comparação rápida
emails_alunos2 = {aluno['email'] for aluno in alunos2}

# Encontrar alunos que estão em alunos.json mas não em alunos2.json
alunos_faltando = []
for aluno in alunos1:
    if aluno['email'] not in emails_alunos2:
        alunos_faltando.append({
            'nome': aluno['nome'],
            'email': aluno['email']
        })

# Salvar resultado em alunosLeft.json
with open('alunosLeft.json', 'w', encoding='utf-8') as f:
    json.dump(alunos_faltando, f, ensure_ascii=False, indent=2)

# Exibir resultado
print(f"Total de alunos em alunos.json: {len(alunos1)}")
print(f"Total de alunos em alunos2.json: {len(alunos2)}")
print(f"Total de alunos que não estão em alunos2.json: {len(alunos_faltando)}")
print(f"\nArquivo 'alunosLeft.json' criado com sucesso!")

if alunos_faltando:
    print("\nAlunos que faltam em alunos2.json:")
    for aluno in alunos_faltando:
        print(f"  - {aluno['nome']} ({aluno['email']})")
