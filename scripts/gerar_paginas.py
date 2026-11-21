"""Gera as páginas de cada área (tributario/, previdenciario/, direito-bancario/, direito-penal/).

Edite os textos em AREAS e rode:  python scripts/gerar_paginas.py
Todo texto deve seguir o Provimento 205/2021 da OAB: informativo, sem promessa de resultado.
"""
import html
import json
from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).resolve().parent.parent
SITE = "https://waschburger.adv.br/"
WHATS = "5549991728535"
AGENDA = "https://calendar.app.google/XQkxsDjP38xJTfrn6"

AREAS = [
    {
        "slug": "tributario",
        "nome": "Tributário",
        "titulo": "Advogado Tributário em Guarujá do Sul (SC) | Waschburger",
        "descricao": "Recuperação de tributos, revisão fiscal, impostos atrasados e reforma tributária para empresas de Guarujá do Sul e região. José Viro Waschburger, OAB/SC 78.480.",
        "h1": "Direito Tributário em Guarujá do Sul (SC)",
        "sub": "Orientação para empresas e empresários da região que querem entender, regularizar ou revisar os tributos que pagam.",
        "assunto": "um assunto tributário",
        "servicos": [
            ("Recuperação tributária", "Revisão dos tributos pagos nos últimos cinco anos para identificar valores recolhidos a mais ou sem necessidade. Quando há crédito, ele pode ser pedido de volta ou compensado com tributos futuros, conforme a lei."),
            ("Revisão fiscal", "Análise das notas fiscais, do enquadramento (Simples Nacional, Lucro Presumido ou Lucro Real) e das rotinas fiscais da empresa, com os riscos e ajustes encontrados."),
            ("Impostos atrasados", "Levantamento das pendências com a Receita Federal, o Estado e o Município, com a explicação dos riscos e das opções de parcelamento e transação disponíveis."),
            ("Reforma tributária", "O que muda com a CBS e o IBS, que substituem aos poucos PIS, Cofins, ICMS e ISS entre 2026 e 2033, e como a empresa pode se preparar."),
        ],
        "documentos": [
            "Contrato social da empresa.",
            "Declarações e apurações dos últimos anos (o contador costuma ter).",
            "Relatório de débitos da Receita Federal, do Estado ou do Município, se houver.",
        ],
        "duvidas": [
            ("Até quanto tempo para trás dá para recuperar tributos?", "Em regra, até cinco anos contados de cada pagamento. Valores mais antigos que isso normalmente não podem mais ser pedidos."),
            ("Empresa do Simples Nacional também pode ter crédito?", "Pode haver, por exemplo, na venda de produtos em que o tributo já foi recolhido antes na cadeia. A análise dos documentos mostra se é o caso."),
        ],
    },
    {
        "slug": "previdenciario",
        "nome": "Previdenciário",
        "titulo": "Advogado Previdenciário em Guarujá do Sul (SC) | INSS",
        "descricao": "Aposentadoria rural e urbana, BPC/LOAS, benefício negado, auxílio-acidente e pensão por morte em Guarujá do Sul e região. José Viro Waschburger, OAB/SC 78.480.",
        "h1": "Direito Previdenciário em Guarujá do Sul (SC)",
        "sub": "Orientação para quem precisa pedir, revisar ou recorrer de um benefício do INSS, e para servidores públicos.",
        "assunto": "um assunto previdenciário",
        "servicos": [
            ("Aposentadoria rural", "Para quem trabalha ou trabalhou na roça com a família. A idade mínima é de 55 anos para mulheres e 60 para homens, com 15 anos de atividade rural comprovada por documentos como notas e bloco de produtor.", "aposentadoria-rural"),
            ("Aposentadoria e planejamento", "Conferência do histórico de contribuições (CNIS), cálculo das regras de transição da Reforma da Previdência de 2019 e pedido no momento adequado.", "aposentadoria"),
            ("Benefício do INSS negado", "Análise da carta de indeferimento e dos documentos para decidir entre novo pedido, recurso ao próprio INSS ou ação na Justiça.", "beneficio-negado"),
            ("BPC/LOAS", "Benefício de um salário mínimo para idosos a partir de 65 anos e pessoas com deficiência de família de baixa renda. Não exige contribuição ao INSS, mas exige inscrição no CadÚnico.", "bpc-loas"),
            ("Auxílio-acidente", "Para quem ficou com sequela que reduz a capacidade para o trabalho depois de um acidente de qualquer tipo. Pode ser recebido junto com o salário."),
            ("Pensão por morte", "Para os dependentes de quem faleceu: cônjuge ou companheiro, filhos e, em alguns casos, pais e irmãos."),
            ("Aposentadoria de servidores públicos", "Regras de aposentadoria e pensão dos regimes próprios de estados e municípios."),
        ],
        "documentos": [
            "Documento de identidade e CPF.",
            "Celular com acesso ao gov.br (login e senha), para consultar o Meu INSS durante a conversa.",
            "Extrato do CNIS, que sai pelo aplicativo ou site Meu INSS.",
            "Carteiras de trabalho e a carta do INSS, se o pedido já foi feito.",
            "Para atividade rural: notas de produtor, bloco, contratos e outros documentos do trabalho no campo.",
        ],
        "duvidas": [
            ("O INSS negou meu pedido. Qual é o prazo para recorrer?", "O recurso ao próprio INSS deve ser apresentado em até 30 dias a partir do conhecimento da decisão. Também é possível fazer um novo pedido ou ir à Justiça."),
            ("Quem trabalha na roça precisa ter pago carnê do INSS?", "O segurado especial (quem trabalha no campo com a família) não precisa pagar carnê: ele comprova a atividade rural, e a contribuição é feita sobre a venda da produção."),
        ],
    },
    {
        "slug": "direito-bancario",
        "nome": "Direito Bancário",
        "titulo": "Advogado de Direito Bancário em Guarujá do Sul (SC)",
        "descricao": "Revisão de contratos bancários e agrícolas, dívidas rurais, revisão de prazos, FINAME e cobranças indevidas em Guarujá do Sul e região. OAB/SC 78.480.",
        "h1": "Direito Bancário em Guarujá do Sul (SC)",
        "sub": "Revisão de contratos com bancos e cooperativas, inclusive crédito rural e financiamento de máquinas.",
        "assunto": "um assunto de Direito Bancário",
        "servicos": [
            ("Contratos agrícolas e dívidas rurais", "Análise de cédulas de crédito rural de custeio e investimento, orientação na renegociação e pedido de revisão de prazos quando há frustração de safra ou queda de renda, conforme as normas do crédito rural."),
            ("Revisão de contratos bancários", "Conferência de juros, encargos e tarifas de empréstimos, financiamentos e cartão de crédito em relação ao que foi contratado."),
            ("FINAME e financiamento de máquinas", "Análise de contratos de financiamento de máquinas e equipamentos agrícolas e industriais."),
            ("Juros, tarifas e cobranças indevidas", "Verificação de valores cobrados sem previsão no contrato ou acima do permitido."),
            ("Renegociação de dívidas", "Orientação na renegociação de dívidas com bancos e cooperativas de crédito."),
        ],
        "documentos": [
            "Cópia do contrato ou da cédula de crédito.",
            "Extratos, boletos e comunicados do banco ou da cooperativa.",
            "No crédito rural: laudos, comunicados de perda de safra e notas da produção.",
        ],
        "duvidas": [
            ("Safra frustrada permite prorrogar a dívida rural?", "As normas do crédito rural preveem a prorrogação em situações como frustração de safra por clima, desde que comprovada. A análise do contrato e dos documentos mostra se é o caso."),
            ("Contratos com cooperativas de crédito também podem ser revisados?", "Sim. Contratos com cooperativas de crédito são analisados da mesma forma que os de bancos."),
        ],
    },
    {
        "slug": "direito-penal",
        "nome": "Direito Penal",
        "titulo": "Advogado Criminal em Guarujá do Sul (SC) | Waschburger",
        "descricao": "Defesa em inquéritos e processos criminais e acompanhamento do cumprimento de sentença em Guarujá do Sul e região. José Viro Waschburger, OAB/SC 78.480.",
        "h1": "Direito Penal em Guarujá do Sul (SC)",
        "sub": "Defesa em inquéritos e processos criminais e acompanhamento do cumprimento de sentença.",
        "assunto": "um assunto de Direito Penal",
        "servicos": [
            ("Defesa em inquéritos", "Acompanhamento da investigação, com acesso aos autos e orientação ao investigado."),
            ("Defesa em processos criminais", "Defesa técnica ao longo do processo, da resposta à acusação aos recursos."),
            ("Acompanhamento do cumprimento de sentença", "Acompanhamento da execução da pena, com os pedidos previstos na Lei de Execução Penal, como progressão de regime e remição."),
        ],
        "documentos": [
            "Intimação ou documento recebido.",
            "Número do inquérito ou do processo, se houver.",
        ],
        "duvidas": [
            ("A conversa com o advogado é sigilosa?", "Sim. Tudo o que é dito ao advogado é protegido pelo sigilo profissional."),
        ],
    },
]


def e(texto):
    return html.escape(texto, quote=True)


def link_whats(assunto):
    msg = f"Olá! Vim pelo site e gostaria de falar sobre {assunto}."
    return f"https://wa.me/{WHATS}?text={quote(msg, safe='')}"


def menu(prefixo, atual=None):
    itens = "\n".join(
        f'<a href="{prefixo}{a["slug"]}/"' + (' aria-current="page"' if a["slug"] == atual else "") + f'>{e(a["nome"])}</a>'
        for a in AREAS
    )
    return f"""<button type="button" class="menu-abrir" aria-expanded="false" aria-controls="menu-principal"><span class="menu-icone" aria-hidden="true"></span><span class="menu-texto">Menu</span></button>
<nav aria-label="Menu principal" class="menu" id="menu-principal">
<div class="submenu">
<button type="button" class="menu-link submenu-botao" aria-expanded="false" aria-controls="submenu-areas">Áreas de atuação</button>
<div class="submenu-lista" id="submenu-areas">
{itens}
</div>
</div>
<a href="{prefixo}#sobre" class="menu-link">Sobre</a>
<a href="{prefixo}artigos/" class="menu-link">Artigos</a>
<a href="{prefixo}#contato" class="menu-link">Contato</a>
<a href="https://wa.me/{WHATS}?text={quote('Olá! Vim pelo site e gostaria de mais informações.', safe='')}" class="botao botao-branco botao-menor">Falar no WhatsApp</a>
</nav>"""


def schema(a):
    url = f"{SITE}{a['slug']}/"
    grafo = [
        {
            "@type": "Service",
            "@id": f"{url}#servico",
            "name": a["nome"],
            "serviceType": a["nome"],
            "url": url,
            "description": a["sub"],
            "provider": {"@id": f"{SITE}#escritorio"},
            "areaServed": {"@type": "City", "name": "Guarujá do Sul"},
            "hasOfferCatalog": {
                "@type": "OfferCatalog",
                "name": a["nome"],
                "itemListElement": [
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": nome}}
                    for nome, *_ in a["servicos"]
                ],
            },
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE},
                {"@type": "ListItem", "position": 2, "name": a["nome"], "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": r}}
                for p, r in a["duvidas"]
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False, indent=2)


def pagina(a):
    url = f"{SITE}{a['slug']}/"
    whats = link_whats(a["assunto"])
    servicos = "\n".join(
        f'<li><h3>{e(sv[0])}</h3><p>{e(sv[1])}</p>'
        + (f'<a href="{sv[2]}/" class="link-servico">Saiba mais sobre {e(sv[0] if sv[0] == "BPC/LOAS" else sv[0][0].lower() + sv[0][1:])}</a>' if len(sv) > 2 else "")
        + "</li>"
        for sv in a["servicos"]
    )
    docs = "\n".join(f"<li>{e(d)}</li>" for d in a["documentos"])
    duvidas = "\n".join(
        f'<div class="duvida"><h3>{e(p)}</h3><p>{e(r)}</p></div>' for p, r in a["duvidas"]
    )
    outras = "\n".join(
        f'<a href="../{o["slug"]}/" class="outra-area">{e(o["nome"])}</a>'
        for o in AREAS if o["slug"] != a["slug"]
    )
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(a['titulo'])}</title>
<meta name="description" content="{e(a['descricao'])}">
<meta name="theme-color" content="#0F1D3F">
<link rel="canonical" href="{url}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{e(a['h1'])}">
<meta property="og:description" content="{e(a['sub'])}">
<meta property="og:image" content="{SITE}img/jose-escritorio.jpg">
<link rel="icon" type="image/png" href="../img/favicon.png">
<link rel="apple-touch-icon" href="../img/apple-touch-icon.png">
<link rel="preload" href="../fontes/playfair.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../fontes/source-sans-3.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../estilo.css">
<script type="application/ld+json">
{schema(a)}
</script>
</head>
<body>

<a href="#principal" class="pular">Pular para o conteúdo</a>

<header class="topo">
<div class="caixa topo-linha">
<a href="../" class="marca">
<img src="../img/logo-branco-112.webp" alt="" width="56" height="56">
<span translate="no">Waschburger Advocacia</span>
</a>
{menu('../', a['slug'])}
</div>
</header>

<main id="principal" tabindex="-1">
<section class="hero hero-area">
<div class="caixa hero-area-texto">
<nav aria-label="Você está em" class="trilha"><a href="../">Início</a> <span aria-hidden="true">›</span> <span aria-current="page">{e(a['nome'])}</span></nav>
<h1>{e(a['h1'])}</h1>
<p class="hero-sub">{e(a['sub'])}</p>
<div class="botoes">
<a href="{whats}" class="botao botao-branco">Falar sobre {e(a['nome'])}</a>
<a href="{AGENDA}" target="_blank" rel="noopener" class="botao botao-contorno-claro">Agendar uma conversa</a>
</div>
</div>
</section>

<section class="caixa area-pagina">
<h2>Como o escritório pode ajudar</h2>
<ul class="servicos">
{servicos}
</ul>
</section>

<section class="faixa-clara">
<div class="caixa area-pagina area-colunas">
<div>
<h2>O que levar para a primeira conversa</h2>
<ul class="lista-docs">
{docs}
</ul>
<p class="nota">Os documentos são enviados por e-mail ou entregues no escritório, nunca pelo WhatsApp.</p>
</div>
<div>
<h2>Dúvidas comuns</h2>
{duvidas}
</div>
</div>
</section>

<section class="caixa area-pagina area-final">
<div class="area-cta">
<h2>Vamos conversar sobre o seu caso</h2>
<p>Atendimento presencial em Guarujá do Sul ou por videoconferência, sempre com horário marcado.</p>
<div class="botoes">
<a href="{whats}" class="botao botao-azul">Falar no WhatsApp</a>
<a href="{AGENDA}" target="_blank" rel="noopener" class="botao botao-contorno">Escolher dia e horário</a>
</div>
</div>
<div class="outras-areas">
<h2>Outras áreas</h2>
{outras}
</div>
</section>
</main>

<footer class="rodape">
<div class="caixa rodape-linha">
<div class="rodape-marca">
<img src="../img/logo-branco-112.webp" alt="" width="52" height="52" loading="lazy">
<div><strong translate="no">Waschburger Advocacia</strong><span>José Viro Waschburger, OAB/SC&nbsp;78.480</span><span>Av. João Pessoa, 1616, Centro, Guarujá do Sul (SC)</span></div>
</div>
<p>Conteúdo de caráter informativo, conforme o Código de Ética e o Provimento 205/2021 da OAB. Não constitui promessa de resultado.</p>
</div>
</footer>

<a href="{whats}" class="whats-flutuante" aria-label="Falar no WhatsApp"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M21 12a9 9 0 0 1-13.2 7.9L3 21l1.2-4.6A9 9 0 1 1 21 12z"/></svg></a>
<script src="../menu.js" defer></script>
</body>
</html>
"""


def main():
    for a in AREAS:
        pasta = RAIZ / a["slug"]
        pasta.mkdir(exist_ok=True)
        (pasta / "index.html").write_text(pagina(a), encoding="utf-8", newline="\n")
        print("ok", a["slug"])
    # menu da página inicial
    inicio = RAIZ / "index.html"
    s = inicio.read_text(encoding="utf-8")
    # o menu começa no botão do celular (se já existir) ou direto no <nav>
    ini = s.find('<button type="button" class="menu-abrir"')
    if ini < 0:
        ini = s.index('<nav aria-label="Menu principal" class="menu"')
    fim = s.index("</nav>", ini) + len("</nav>")
    s = s[:ini] + menu("") + s[fim:]
    inicio.write_text(s, encoding="utf-8", newline="")
    # sitemap
    urls = [SITE] + [f"{SITE}{a['slug']}/" for a in AREAS]
    linhas = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    (RAIZ / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{linhas}\n</urlset>\n',
        encoding="utf-8", newline="\n")
    print("ok menu + sitemap")


if __name__ == "__main__":
    main()
