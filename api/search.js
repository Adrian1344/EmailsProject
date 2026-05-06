import fs from 'fs';
import path from 'path';

export default function handler(req, res) {
  // CORS headers
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { query } = req.query;

  if (!query || query.trim().length === 0) {
    return res.status(400).json({ error: 'Query parameter is required' });
  }

  try {
    // Carregar dados dos alunos
    let alunos;

    // Tentar ler da variável de ambiente (Vercel)
    if (process.env.ALUNOS_JSON) {
      alunos = JSON.parse(process.env.ALUNOS_JSON);
    } else {
      // Fallback para arquivo local (desenvolvimento)
      const filePath = path.join(process.cwd(), 'alunos2.json');
      const fileContent = fs.readFileSync(filePath, 'utf-8');
      alunos = JSON.parse(fileContent);
    }

    // Normalizar busca para case-insensitive e sem acentos
    const normalizeString = (str) => {
      return str
        .toLowerCase()
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '') // Remove acentos
        .trim();
    };

    const normalizedQuery = normalizeString(query);

    // Filtrar alunos que correspondem à busca
    const resultados = alunos.filter((aluno) => {
      const normalizedNome = normalizeString(aluno.nome);
      const normalizedEmail = normalizeString(aluno.email);

      return (
        normalizedNome.includes(normalizedQuery) ||
        normalizedEmail.includes(normalizedQuery)
      );
    });

    // Limitar a 10 resultados
    const limitedResults = resultados.slice(0, 10);

    return res.status(200).json({
      success: true,
      query,
      total: resultados.length,
      results: limitedResults,
    });
  } catch (error) {
    console.error('Error reading file:', error);
    return res.status(500).json({
      error: 'Internal server error',
      message: error.message,
    });
  }
}
