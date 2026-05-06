#!/usr/bin/env python3
"""
Servidor local para testar a aplicação School Email Lookup
Funciona como um simulador do Vercel para desenvolvimento local
"""

import json
import re
import unicodedata
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

class SchoolEmailHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # API endpoint
        if self.path.startswith('/api/search'):
            self.handle_search()
        else:
            # Servir arquivos estáticos
            super().do_GET()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def handle_search(self):
        """Trata requisições de busca de alunos"""
        try:
            # Extrair parâmetro de busca
            query_match = re.search(r'query=([^&]*)', self.path)
            if not query_match:
                self.send_error(400, 'Query parameter is required')
                return

            import urllib.parse
            query = urllib.parse.unquote(query_match.group(1)).strip()

            if not query:
                self.send_error(400, 'Query parameter is required')
                return

            # Carregar arquivo alunos2.json
            alunos_file = Path(__file__).parent / 'alunos2.json'
            if not alunos_file.exists():
                self.send_error(500, f'File not found: {alunos_file}')
                return

            with open(alunos_file, 'r', encoding='utf-8') as f:
                alunos = json.load(f)

            # Função para normalizar strings
            def normalize(s):
                return unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode('ascii').strip()

            normalized_query = normalize(query)

            # Filtrar resultados
            resultados = [
                aluno for aluno in alunos
                if normalize(aluno['nome']).find(normalized_query) != -1
                or normalize(aluno['email']).find(normalized_query) != -1
            ]

            # Limitar a 10 resultados
            limited_results = resultados[:10]

            # Enviar resposta
            response = {
                'success': True,
                'query': query,
                'total': len(resultados),
                'results': limited_results
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))

        except Exception as e:
            self.send_error(500, str(e))

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def translate_path(self, path):
        """Serve arquivos da pasta 'public' por padrão"""
        # Se for índice, redireciona para index.html
        if path == '/' or path.endswith('/'):
            path = '/index.html'

        # Se for um arquivo .html sem extensão (como /search), adiciona .html
        if path.endswith('.html') or path.startswith('/api/'):
            return super().translate_path(path)

        # Tenta servir arquivo HTML
        if not path.startswith('/api/'):
            # Se não tem extensão, tenta adicionar .html
            if '.' not in path.split('/')[-1]:
                return super().translate_path(path + '.html')

        return super().translate_path(path)


def run_server(port=8000, directory='public'):
    """Inicia o servidor de desenvolvimento"""
    os.chdir(Path(__file__).parent)

    # Mudar para diretório público
    if Path(directory).exists():
        os.chdir(directory)

    server_address = ('', port)
    httpd = HTTPServer(server_address, SchoolEmailHandler)

    print(f'🚀 Servidor rodando em http://localhost:{port}')
    print(f'📂 Servindo arquivos de: {Path.cwd()}')
    print(f'🔍 API: http://localhost:{port}/api/search?query=termo')
    print('\nPressione Ctrl+C para parar o servidor')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n\n✋ Servidor parado')
        httpd.shutdown()


if __name__ == '__main__':
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(port=port)
