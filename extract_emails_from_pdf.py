import pdfplumber
import json
import re
from pathlib import Path


def extrair_alunos_do_pdf(caminho_pdf):
    """
    Extrai nomes e emails institucionais de um PDF com tabelas.
    """
    alunos = []
    
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            print(f"Total de páginas: {len(pdf.pages)}")
            
            for num_pagina, pagina in enumerate(pdf.pages, 1):
                print(f"\n--- Página {num_pagina} ---")
                
                # Tenta extrair tabelas primeiro (mais preciso)
                tabelas = pagina.extract_tables()
                
                if tabelas:
                    for tabela in tabelas:
                        for linha in tabela:
                            # Processa cada célula da tabela
                            texto_linha = ' '.join(str(celula) if celula else '' for celula in linha)
                            aluno = extrair_email_e_nome(texto_linha, num_pagina)
                            if aluno:
                                alunos.append(aluno)
                
                # Se não encontrou tabelas, tenta com texto simples
                if not tabelas:
                    texto = pagina.extract_text()
                    if texto:
                        linhas = texto.split('\n')
                        for linha in linhas:
                            aluno = extrair_email_e_nome(linha, num_pagina)
                            if aluno:
                                alunos.append(aluno)
    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_pdf}' não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao processar PDF: {e}")
        return []
    
    return alunos


def extrair_email_e_nome(linha, num_pagina):
    """
    Extrai email e nome de uma linha.
    """
    linha = linha.strip()
    
    if not linha:
        return None
    
    # Procura por padrão de email
    match_email = re.search(r'[\w\.\-]+@[\w\.\-]+\.\w+', linha)
    
    if match_email:
        email = match_email.group(0)
        
        # Extrai o nome (texto entre MATR: ... e o email)
        # Remove "MATR: XXXXX" do início
        nome_parte = re.sub(r'MATR:\s*\d+\s*', '', linha)
        
        # Remove o email do final
        nome_parte = nome_parte[:match_email.start()].strip()
        
        # Remove espaços extras
        nome = ' '.join(nome_parte.split())
        
        if nome and len(nome) > 2:  # Validação básica
            print(f"✓ Página {num_pagina}: {nome} - {email}")
            return {
                'nome': nome,
                'email': email
            }
    
    return None


def remover_duplicatas(alunos):
    """
    Remove emails duplicados, mantendo o primeiro registro.
    """
    emails_vistos = set()
    alunos_unicos = []
    
    for aluno in alunos:
        if aluno['email'] not in emails_vistos:
            emails_vistos.add(aluno['email'])
            alunos_unicos.append(aluno)
    
    return alunos_unicos


def salvar_json(alunos, caminho_saida='alunos.json'):
    """
    Salva a lista de alunos em um arquivo JSON.
    """
    try:
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            json.dump(alunos, f, ensure_ascii=False, indent=2)
        print(f"\n✓ Dados salvos em '{caminho_saida}'")
        print(f"Total de alunos: {len(alunos)}")
    except Exception as e:
        print(f"Erro ao salvar JSON: {e}")


def main():
    """Função principal"""
    caminho_pdf = input("Digite o caminho do arquivo PDF (ou pressione Enter para 'listagem.pdf'): ").strip()
    
    if not caminho_pdf:
        caminho_pdf = 'listagem.pdf'
    
    caminho_saida = input("Digite o caminho de saída para o JSON (ou pressione Enter para 'alunos.json'): ").strip()
    
    if not caminho_saida:
        caminho_saida = 'alunos.json'
    
    print(f"\nProcessando: {caminho_pdf}")
    print("-" * 50)
    
    alunos = extrair_alunos_do_pdf(caminho_pdf)
    
    if alunos:
        alunos = remover_duplicatas(alunos)
        salvar_json(alunos, caminho_saida)
    else:
        print("\nNenhum email foi encontrado no PDF.")


if __name__ == '__main__':
    main()
