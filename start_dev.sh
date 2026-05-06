#!/bin/bash
# Script de setup para iniciar o desenvolvimento

echo "🚀 School Email Lookup - Setup Script"
echo "======================================"
echo ""

# Verificar se Python está instalado
if ! command -v python &> /dev/null; then
    echo "❌ Python não está instalado. Por favor, instale Python 3.7+"
    exit 1
fi

echo "✅ Python encontrado: $(python --version)"
echo ""

# Iniciar o servidor de desenvolvimento
echo "📂 Iniciando servidor de desenvolvimento..."
echo "🌐 Acesse: http://localhost:8000"
echo ""
echo "Pressione Ctrl+C para parar o servidor"
echo ""

python dev_server.py 8000
