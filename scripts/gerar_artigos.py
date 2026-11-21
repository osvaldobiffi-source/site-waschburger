"""Gera os artigos do blog (artigos/<slug>/) e a lista (artigos/).

Cada artigo só vai ao ar depois da aprovação do José: enquanto não aprovado, fica com
"rascunho": True (não gera página nem entra no sitemap). Rode:  python scripts/gerar_site.py
Texto informativo, conforme o Provimento 205/2021 da OAB.
"""
import json
from pathlib import Path

from gerar_paginas import AGENDA, SITE, e, link_whats, menu

RAIZ = Path(__file__).resolve().parent.parent
AUTOR = "José Viro Waschburger"

ARTIGOS = [
    {
        "rascunho": True,  # aguardando correção do José
        "slug": "mp-1376-renegociacao-dividas-rurais",
        "titulo": "MP 1.376/2026: o que muda na renegociação de dívidas rurais",
        "descricao": "Quem pode renegociar, quais dívidas entram, juros, prazos e documentos da MP 1.376/2026, aprovada pelo Congresso em novembro de 2026.",
        "resumo": "Quem pode renegociar, quais dívidas entram, juros, prazos e o que separar desde já.",
        "area": ("Direito Bancário", "direito-bancario"),
        "assunto": "a renegociação de dívidas rurais",
        "publicado": "2026-11-18",
        "atualizado": "2026-11-18",
        "corpo": """
<p class="artigo-lead">O Congresso aprovou, em 10 e 11 de novembro de 2026, a Medida Provisória 1.376/2026, que cria linhas para renegociar dívidas de produtores rurais prejudicados por eventos climáticos entre 2019 e 2025. O texto aprovado (PLV 16/2026) segue para sanção presidencial e ainda depende de regulamentação.</p>

<p>Não se trata de perdão de dívida, e a renegociação não é automática: o produtor precisa se enquadrar nos critérios, comprovar a perda e contratar a nova linha na instituição financeira.</p>

<h2>Quem pode renegociar</h2>
<ul>
<li>Produtores rurais e cooperativas de produção que tiveram <strong>duas ou mais quebras de safra</strong> por eventos climáticos extremos entre 2019 e 2025, como estiagem, geada, granizo, chuvas intensas, enxurradas, vendaval e tornado.</li>
<li>A perda precisa ser de pelo menos <strong>30% da renda bruta agropecuária esperada</strong> para a safra ou atividade financiada (25% nas áreas da Sudam, Sudene e Sudeco).</li>
<li>Também entra a perda de receita causada pela queda do preço de venda dos produtos financiados.</li>
</ul>
<p>Há uma <strong>situação especial</strong>, com condições melhores, para quem teve perdas em três ou mais safras e redução de pelo menos 40% da renda (35% nas áreas da Sudam, Sudene e Sudeco).</p>

<h2>Quais dívidas entram</h2>
<ul>
<li><strong>Investimento</strong> contratado até 31/12/2025, com parcelas vencidas ou a vencer entre 1º/1/2024 e 31/12/2026.</li>
<li><strong>Custeio, comercialização e industrialização</strong> contratados até 31/12/2025, mesmo que já renegociados ou prorrogados, em atraso desde 2024, conforme as datas definidas na lei.</li>
<li><strong>Capital de giro</strong> contratado até 31/12/2025 e em atraso.</li>
</ul>
<p>Ficam de fora as dívidas inscritas na Dívida Ativa da União, as contratadas com recursos do Fundo Social e as operações feitas pela MP 1.314/2025. Valores já quitados antes da lei, inclusive por Proagro ou seguro rural, também não entram.</p>

<h2>Juros, limites e prazos</h2>
<div class="tabela-rolagem">
<table>
<caption>Limite por produtor e juros ao ano</caption>
<thead><tr><th scope="col">Enquadramento</th><th scope="col">Caso geral (2 ou mais safras, perda de 30%)</th><th scope="col">Situação especial (3 ou mais safras, perda de 40%)</th></tr></thead>
<tbody>
<tr><th scope="row">Pronaf</th><td>até R$ 400 mil, 6% a.a.</td><td>até R$ 500 mil, 5% a.a.</td></tr>
<tr><th scope="row">Pronamp</th><td>até R$ 2 milhões, 9% a.a.</td><td>até R$ 2,5 milhões, 8% a.a.</td></tr>
<tr><th scope="row">Demais produtores</th><td>até R$ 4 milhões, 12% a.a.</td><td>até R$ 8 milhões, 11% a.a.</td></tr>
</tbody>
</table>
</div>
<ul>
<li><strong>Carência de 2 anos</strong>, pagando só os juros.</li>
<li>Depois, pagamento em <strong>até 8 anos</strong> (até 10 anos na situação especial).</li>
<li>Nas dívidas com recursos dos fundos constitucionais (FNO, FNE e FCO), os juros seguem as regras de cada fundo.</li>
</ul>

<h2>Como pedir</h2>
<ul>
<li>O pedido é feito na <strong>instituição financeira</strong> onde está a dívida (banco ou cooperativa de crédito).</li>
<li>O prazo para contratar será de <strong>120 dias depois da regulamentação</strong> da lei.</li>
<li>A quebra de safra e a perda de renda são comprovadas por <strong>laudo de profissional habilitado</strong>. Em alguns casos, como em operações do Pronaf e do Pronamp, o laudo pode ser coletivo.</li>
<li>Pela lei, a renegociação não impede novos empréstimos nem gera registro em cadastros de inadimplentes.</li>
</ul>

<h2>O que separar desde já</h2>
<ul>
<li>Contratos e cédulas de crédito rural de cada operação.</li>
<li>Extratos e comunicados com as parcelas em atraso.</li>
<li>Laudos, comunicados de perda, Proagro ou seguro rural das safras afetadas.</li>
<li>Notas de produtor e outros documentos que mostrem a queda da produção ou da renda.</li>
</ul>

<h2>Atenção: o texto ainda pode mudar</h2>
<p>A lei ainda pode receber vetos na sanção, e vários detalhes dependem da regulamentação. Este artigo será atualizado quando isso acontecer. Cada contrato tem suas condições, e o enquadramento depende da análise dos documentos.</p>

<p class="fontes">Fontes: <a href="https://www12.senado.leg.br/noticias/materias/2026/11/11/renegociacao-de-dividas-rurais-e-aprovada-pelo-senado-e-vai-a-sancao-presidencial">Agência Senado (11/11/2026)</a> e <a href="https://www.camara.leg.br/noticias/1317852-camara-aprova-renegociacao-de-dividas-rurais-de-produtores-prejudicados-por-eventos-climaticos-extremos">Agência Câmara (10/11/2026)</a>.</p>
""",
    },
]


def publicados():
    return [a for a in ARTIGOS if not a.get("rascunho")]


def data_br(iso):
    a, m, d = iso.split("-")
    return f"{d}/{m}/{a}"


def cabeca(titulo, descricao, url, prefixo, extra="", tipo="article"):
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(titulo)}</title>
<meta name="description" content="{e(descricao)}">
<meta name="theme-color" content="#0F1D3F">
<link rel="canonical" href="{url}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="{tipo}">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(descricao)}">
<meta property="og:image" content="{SITE}img/jose-escritorio.jpg">
<link rel="icon" type="image/png" href="{prefixo}img/favicon.png">
<link rel="preload" href="{prefixo}fontes/playfair.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{prefixo}fontes/source-sans-3.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{prefixo}estilo.css">
{extra}</head>
<body>

<a href="#principal" class="pular">Pular para o conteúdo</a>

<header class="topo">
<div class="caixa topo-linha">
<a href="{prefixo}" class="marca">
<img src="{prefixo}img/logo-branco-112.webp" alt="" width="56" height="56">
<span translate="no">Waschburger Advocacia</span>
</a>
{menu(prefixo)}
</div>
</header>
"""


def rodape(prefixo, whats):
    return f"""
<footer class="rodape">
<div class="caixa rodape-linha">
<div class="rodape-marca">
<img src="{prefixo}img/logo-branco-112.webp" alt="" width="52" height="52" loading="lazy">
<div><strong translate="no">Waschburger Advocacia</strong><span>José Viro Waschburger, OAB/SC&nbsp;78.480</span><span>Av. João Pessoa, 1616, Centro, Guarujá do Sul (SC)</span></div>
</div>
<p>Conteúdo de caráter informativo, conforme o Código de Ética e o Provimento 205/2021 da OAB. Não constitui promessa de resultado.</p>
</div>
</footer>

<a href="{whats}" class="whats-flutuante" aria-label="Falar no WhatsApp"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M21 12a9 9 0 0 1-13.2 7.9L3 21l1.2-4.6A9 9 0 1 1 21 12z"/></svg></a>
</body>
</html>
"""


def artigo(a):
    url = f"{SITE}artigos/{a['slug']}/"
    area_nome, area_slug = a["area"]
    whats = link_whats(a["assunto"])
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": a["titulo"],
                "description": a["descricao"],
                "url": url,
                "datePublished": a["publicado"],
                "dateModified": a["atualizado"],
                "inLanguage": "pt-BR",
                "author": {"@id": f"{SITE}#jose"},
                "publisher": {"@id": f"{SITE}#escritorio"},
                "image": f"{SITE}img/jose-escritorio.jpg",
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE},
                    {"@type": "ListItem", "position": 2, "name": "Artigos", "item": f"{SITE}artigos/"},
                    {"@type": "ListItem", "position": 3, "name": a["titulo"], "item": url},
                ],
            },
        ],
    }
    extra = f'<script type="application/ld+json">\n{json.dumps(ld, ensure_ascii=False, indent=2)}\n</script>\n'
    p = "../../"
    return cabeca(a["titulo"], a["descricao"], url, p, extra) + f"""
<main id="principal" tabindex="-1">
<section class="hero hero-area">
<div class="caixa hero-area-texto">
<nav aria-label="Você está em" class="trilha"><a href="{p}">Início</a> <span aria-hidden="true">›</span> <a href="../">Artigos</a> <span aria-hidden="true">›</span> <span aria-current="page">{e(area_nome)}</span></nav>
<h1>{e(a['titulo'])}</h1>
<p class="assinatura">Por {AUTOR}, OAB/SC 78.480 · Atualizado em <time datetime="{a['atualizado']}">{data_br(a['atualizado'])}</time></p>
</div>
</section>

<article class="caixa artigo">
{a['corpo']}
<aside class="artigo-cta">
<h2>Quer saber se o seu contrato se enquadra?</h2>
<p>O enquadramento depende dos contratos e dos laudos de cada caso. Atendimento presencial em Guarujá do Sul ou por videoconferência, com horário marcado.</p>
<div class="botoes">
<a href="{whats}" class="botao botao-azul">Falar no WhatsApp</a>
<a href="{p}{area_slug}/" class="botao botao-contorno">Ver a página de {e(area_nome)}</a>
</div>
</aside>
</article>
</main>
""" + rodape(p, whats)


def lista():
    p = "../"
    url = f"{SITE}artigos/"
    itens = "\n".join(
        f'<li><a href="{a["slug"]}/"><span class="rotulo">{e(a["area"][0])} · {data_br(a["publicado"])}</span><strong>{e(a["titulo"])}</strong><span>{e(a["resumo"])}</span></a></li>'
        for a in sorted(publicados(), key=lambda x: x["publicado"], reverse=True)
    )
    if not itens:
        itens = '<li class="vazio">Os primeiros artigos serão publicados em breve.</li>'
    whats = link_whats("um assunto")
    return cabeca("Artigos | Waschburger Advocacia", "Artigos informativos sobre direito tributário, previdenciário, bancário e rural, escritos por José Viro Waschburger, OAB/SC 78.480.", url, p, tipo="website") + f"""
<main id="principal" tabindex="-1">
<section class="hero hero-area">
<div class="caixa hero-area-texto">
<nav aria-label="Você está em" class="trilha"><a href="{p}">Início</a> <span aria-hidden="true">›</span> <span aria-current="page">Artigos</span></nav>
<h1>Artigos</h1>
<p class="hero-sub">Textos informativos sobre mudanças na lei e dúvidas comuns de quem vive e produz na região.</p>
</div>
</section>
<section class="caixa area-pagina">
<ul class="lista-artigos">
{itens}
</ul>
</section>
</main>
""" + rodape(p, whats)


def main():
    pasta = RAIZ / "artigos"
    pasta.mkdir(exist_ok=True)
    (pasta / "index.html").write_text(lista(), encoding="utf-8", newline="\n")
    for a in publicados():
        d = pasta / a["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(artigo(a), encoding="utf-8", newline="\n")
        print("ok", a["slug"])
    # sitemap: acrescenta artigos (a lista só entra quando houver artigo publicado)
    if not publicados():
        return
    sm = RAIZ / "sitemap.xml"
    s = sm.read_text(encoding="utf-8")
    for u in [f"{SITE}artigos/"] + [f"{SITE}artigos/{a['slug']}/" for a in publicados()]:
        if u not in s:
            s = s.replace("</urlset>", f"  <url><loc>{u}</loc></url>\n</urlset>")
    sm.write_text(s, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
