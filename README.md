# Site Waschburger Advocacia

Site estático (HTML + CSS) do escritório de José Viro Waschburger, OAB/SC 78.480.

- `index.html`, `estilo.css`: a página.
- `noticias.json`: notícias por área. É atualizado todo dia às 6h pelo GitHub Actions (`.github/workflows/noticias.yml`), que roda `scripts/atualizar_noticias.py`.
- `noticias.js`: mostra as 3 notícias mais recentes de cada área.
- `img/`: fotos e logotipo.

Para testar no computador: `python -m http.server` nesta pasta e abrir http://localhost:8000.

Domínio: waschburger.adv.br (Registro.br, no CPF do José; DNS no Registro.br apontando para o GitHub Pages).

Regras da OAB: textos revisados conforme o Código de Ética (arts. 39 a 47) e o Provimento 205/2021. Não incluir preços, promessa de resultado, casos concretos ou vínculo com outras atividades.
