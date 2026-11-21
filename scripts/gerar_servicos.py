"""Gera as páginas de serviço (ex.: previdenciario/aposentadoria-rural/).

Base: textos enviados pelo José em 17/11/2026, reescritos conforme o Provimento 205/2021 da OAB.
Rode pelo scripts/gerar_site.py.
"""
import json
from pathlib import Path

from gerar_paginas import AGENDA, SITE, e, link_whats
from gerar_artigos import cabeca, rodape

RAIZ = Path(__file__).resolve().parent.parent

ATENDIMENTO_PADRAO = [
    ("Conversa direta com o advogado", "Por WhatsApp, em áudio ou texto, ou por telefone, em linguagem simples."),
    ("Análise dos documentos", "Você recebe uma explicação clara sobre a situação e o caminho possível."),
    ("Documentos organizados antes do pedido", "Nada é protocolado sem que a documentação esteja conferida."),
]

SERVICOS = [
    {
        "area": ("Previdenciário", "previdenciario"),
        "slug": "aposentadoria-rural",
        "nome": "Aposentadoria rural",
        "titulo": "Aposentadoria Rural em Guarujá do Sul (SC) | Advogado",
        "descricao": "Quem tem direito à aposentadoria rural, idade mínima e como comprovar o trabalho no campo sem carteira assinada. Guarujá do Sul e região. OAB/SC 78.480.",
        "h1": "Aposentadoria rural em Guarujá do Sul (SC)",
        "sub": "Quem trabalhou na roça com a família pode ter direito à aposentadoria rural, mesmo sem carteira assinada.",
        "assunto": "aposentadoria rural",
        "secoes": """
<h2>Quem tem direito</h2>
<ul>
<li>Mulheres a partir de <strong>55 anos</strong> e homens a partir de <strong>60 anos</strong>.</li>
<li><strong>15 anos de atividade rural</strong>, mesmo que com interrupções, trabalhando no campo com a família (o chamado segurado especial).</li>
<li>Não é preciso ter pago carnê do INSS: a contribuição do segurado especial é feita sobre a venda da produção.</li>
</ul>

<h2>Como o trabalho no campo é comprovado</h2>
<p>Muita gente acha que não tem prova porque nunca teve carteira assinada. O INSS aceita documentos como:</p>
<ul>
<li>certidão de casamento ou de nascimento dos filhos com a profissão de lavrador ou agricultor;</li>
<li>notas fiscais e bloco de produtor rural;</li>
<li>ficha de filiação ao sindicato rural;</li>
<li>histórico escolar de escola rural, cadastro no INCRA e contratos de arrendamento, parceria ou comodato.</li>
</ul>
<p>Testemunhas que trabalharam junto na mesma época ajudam a confirmar o período, mas precisam vir acompanhadas de algum desses documentos. O pedido também inclui a autodeclaração do segurado especial, que o INSS usa no lugar da antiga entrevista rural.</p>

<h2>Trabalhou na roça e depois na cidade?</h2>
<p>Quem tem tempo rural e tempo urbano pode somar os dois na aposentadoria híbrida, com idade de 62 anos para mulheres e 65 para homens. <a href="../aposentadoria/">Veja a página de aposentadoria</a>.</p>
""",
        "atendimento": [
            ("Conversa direta com o advogado", "Por WhatsApp, em áudio ou texto, em linguagem simples."),
            ("Análise dos documentos antigos", "Você recebe uma explicação clara sobre o que comprova o período e o que falta."),
            ("Pedido organizado", "Documentos conferidos e orientação para preencher a autodeclaração antes do pedido ao INSS."),
        ],
        "documentos": [
            "Documento de identidade, CPF e comprovante de residência.",
            "Celular com acesso ao gov.br (login e senha), para consultar o Meu INSS durante a conversa.",
            "Certidões de casamento e de nascimento dos filhos.",
            "Notas e bloco de produtor, contratos e outros documentos do trabalho no campo, dos mais antigos aos mais recentes.",
        ],
        "duvidas": [
            ("Preciso de um documento para cada ano?", "Não. Os documentos servem como início de prova do período, que pode ser confirmado por testemunhas."),
            ("Trabalhei parte do tempo na cidade. Perco o tempo rural?", "Não. Dependendo do caso, os dois tempos podem ser somados na aposentadoria híbrida."),
        ],
    },
    {
        "area": ("Previdenciário", "previdenciario"),
        "slug": "aposentadoria",
        "nome": "Aposentadoria e planejamento",
        "titulo": "Aposentadoria e Planejamento em Guarujá do Sul (SC)",
        "descricao": "Regras de transição, aposentadoria híbrida, conferência do CNIS e tempo especial antes do pedido ao INSS. Guarujá do Sul e região. OAB/SC 78.480.",
        "h1": "Aposentadoria e planejamento em Guarujá do Sul (SC)",
        "sub": "As regras de transição da Reforma da Previdência mudam a idade, o tempo e o valor. Vale comparar antes de fazer o pedido.",
        "assunto": "aposentadoria",
        "secoes": """
<h2>As regras de transição</h2>
<p>Quem já contribuía antes de 13/11/2019 pode se aposentar por uma das regras de transição: <strong>pontos</strong>, <strong>idade mínima progressiva</strong>, <strong>pedágio de 50%</strong> ou <strong>pedágio de 100%</strong>. Cada uma tem requisitos e forma de cálculo diferentes. A comparação mostra qual se aplica ao seu caso e qual resulta em valor maior.</p>

<h2>O que é conferido antes do pedido</h2>
<ul>
<li><strong>CNIS:</strong> vínculos de emprego que não aparecem no sistema do INSS e salários registrados a menor.</li>
<li><strong>Tempo especial:</strong> trabalho com ruído, agentes químicos ou risco, comprovado por PPP e LTCAT. O período trabalhado até 13/11/2019 pode ser convertido e aumentar o tempo de contribuição.</li>
<li><strong>Simulação das regras:</strong> comparação entre as regras de transição, para evitar aposentadoria com redução desnecessária.</li>
</ul>

<h2>Aposentadoria híbrida: roça e cidade</h2>
<p>Quem trabalhou na roça na juventude e depois foi para a cidade não precisa escolher entre um tempo e outro. Na aposentadoria híbrida, o período rural (mesmo sem contribuição) é somado ao tempo urbano para completar a carência, com idade de <strong>62 anos para mulheres e 65 para homens</strong>.</p>
<p>Só trabalhou no campo? <a href="../aposentadoria-rural/">Veja a aposentadoria rural</a>.</p>
""",
        "atendimento": [
            ("Análise do seu CNIS", "Você recebe uma explicação objetiva do que está certo e do que falta no histórico."),
            ("Conversa direta com o advogado", "Cada etapa e cada regra do cálculo explicadas em linguagem simples."),
            ("Pedido com a documentação conferida", "Correções feitas antes do pedido, para reduzir exigências e atrasos na análise do INSS."),
        ],
        "documentos": [
            "Extrato do CNIS, que sai pelo aplicativo ou site Meu INSS.",
            "Celular com acesso ao gov.br (login e senha), para consultar o Meu INSS durante a conversa.",
            "Carteiras de trabalho e carnês, se houver.",
            "PPP e LTCAT, para quem trabalhou com ruído, produtos químicos ou risco.",
            "Documentos do trabalho rural, se houver tempo na roça.",
        ],
        "duvidas": [
            ("Posso pedir a aposentadoria sozinho pelo Meu INSS?", "Pode. A análise antes do pedido serve para conferir o CNIS e escolher a regra adequada."),
            ("Tempo especial depois de 2019 ainda conta?", "Para converter em tempo comum, só o período até 13/11/2019. Depois disso, ele vale para a aposentadoria especial, que tem regras próprias."),
        ],
    },
    {
        "area": ("Previdenciário", "previdenciario"),
        "slug": "bpc-loas",
        "nome": "BPC/LOAS",
        "titulo": "BPC/LOAS em Guarujá do Sul (SC) | Idosos e PCD",
        "descricao": "Quem tem direito ao BPC/LOAS, como é calculada a renda da família, gastos que podem ser descontados e CadÚnico. Guarujá do Sul e região. OAB/SC 78.480.",
        "h1": "BPC/LOAS em Guarujá do Sul (SC)",
        "sub": "Benefício de um salário mínimo por mês para idosos a partir de 65 anos e pessoas com deficiência de família de baixa renda.",
        "assunto": "BPC/LOAS",
        "secoes": """
<h2>Quem pode ter direito</h2>
<p>O BPC/LOAS não exige contribuição ao INSS, mas exige estes critérios:</p>
<ul>
<li><strong>Idosos:</strong> 65 anos ou mais e baixa renda familiar.</li>
<li><strong>Pessoas com deficiência, de qualquer idade:</strong> impedimento de longo prazo (no mínimo 2 anos) de natureza física, mental, intelectual ou sensorial, incluindo o Transtorno do Espectro Autista (TEA).</li>
<li><strong>CadÚnico:</strong> inscrição feita no CRAS e atualizada nos últimos 2 anos, com os dados de todos da casa.</li>
</ul>

<h2>A regra da renda não é absoluta</h2>
<p>A referência é a renda de até 1/4 do salário mínimo por pessoa da família, e o pedido costuma ser negado quando alguém da casa recebe um salário mínimo. Mas a lei permite descontar do cálculo os gastos comprovados com:</p>
<ul>
<li>medicamentos de uso contínuo não fornecidos pelo SUS;</li>
<li>fraldas, alimentação especial e insumos médicos;</li>
<li>consultas, terapias e tratamentos de saúde.</li>
</ul>
<p>Além disso, o benefício de até um salário mínimo recebido por outro idoso ou pessoa com deficiência da mesma casa não entra na conta.</p>

<h2>Perícia e avaliação social</h2>
<p>No caso de pessoa com deficiência, o INSS faz perícia médica e avaliação social. A orientação inclui o que levar (laudos, receitas, relatórios de terapia) e como relatar as limitações reais do dia a dia.</p>
""",
        "atendimento": [
            ("Análise da renda e do CadÚnico", "Conferência da composição da família e dos comprovantes de gastos antes do pedido."),
            ("Atendimento simples pelo WhatsApp", "Para quem cuida de alguém e tem pouco tempo livre: orientações por áudio ou texto."),
            ("Orientação para a perícia", "O que levar e como se preparar para a perícia médica e a avaliação social."),
        ],
        "documentos": [
            "Documento de identidade e CPF de todos da casa.",
            "Celular com acesso ao gov.br (login e senha), para consultar o Meu INSS durante a conversa.",
            "Comprovante de inscrição no CadÚnico.",
            "Laudos, receitas e relatórios médicos ou de terapia.",
            "Notas e recibos de remédios, fraldas e tratamentos.",
        ],
        "duvidas": [
            ("O BPC paga 13º?", "Não. O BPC também não gera pensão por morte, porque é um benefício assistencial."),
            ("Alguém da casa trabalha. Ainda assim pode ter direito?", "Pode. A renda é dividida por todos da família, e alguns gastos e benefícios podem ser descontados do cálculo."),
        ],
    },
    {
        "area": ("Previdenciário", "previdenciario"),
        "slug": "beneficio-negado",
        "nome": "Benefício negado ou cortado",
        "titulo": "Benefício do INSS Negado ou Cortado | Guarujá do Sul (SC)",
        "descricao": "O INSS negou ou cortou o benefício? Prazo de recurso, cuidado com o novo pedido, ação judicial e documentos. Guarujá do Sul e região. OAB/SC 78.480.",
        "h1": "Benefício do INSS negado ou cortado",
        "sub": "Depois da negativa ainda há caminhos: recurso ao INSS, novo pedido com as provas corrigidas ou ação judicial.",
        "assunto": "um benefício negado pelo INSS",
        "secoes": """
<h2>Cuidado antes de fazer um novo pedido igual</h2>
<p>Fazer um novo pedido no Meu INSS sem corrigir o que faltou no primeiro pode fazer você perder a <strong>data do primeiro pedido</strong> (a DER). É a partir dela que os valores atrasados são contados. Por isso, vale entender o motivo da negativa antes de pedir de novo.</p>

<h2>Os caminhos depois da negativa</h2>
<ul>
<li><strong>Recurso ao INSS:</strong> deve ser apresentado em até 30 dias a partir do conhecimento da decisão.</li>
<li><strong>Novo pedido:</strong> com os documentos que faltaram, quando isso fizer sentido.</li>
<li><strong>Ação judicial:</strong> na Justiça Federal, quando o caso pede outras provas.</li>
</ul>

<h2>O que muda quando o caso vai à Justiça</h2>
<ul>
<li><strong>Perícia por médico nomeado pelo juiz</strong>, fora do INSS, nos casos de auxílio por incapacidade temporária (antigo auxílio-doença), aposentadoria por incapacidade permanente (antiga aposentadoria por invalidez) e BPC.</li>
<li><strong>Mais provas:</strong> testemunhas, novos laudos e a revisão da contagem de tempo rural ou especial.</li>
<li><strong>Atrasados:</strong> se o direito já existia na data do primeiro pedido, as parcelas podem ser pagas desde então.</li>
</ul>

<h2>Benefício cortado</h2>
<p>Quando o INSS revisa e corta um benefício, a notificação informa o motivo e o prazo para a defesa. Vale procurar orientação logo que ela chegar.</p>
""",
        "atendimento": [
            ("Leitura da carta do INSS", "Para entender o motivo real da negativa ou do corte."),
            ("Explicação clara do caminho", "Recurso, novo pedido com provas corrigidas ou ação judicial, com os prós e contras de cada um."),
            ("Levantamento do que faltou", "Laudos, exames e documentos que não estavam no pedido ao INSS."),
        ],
        "documentos": [
            "Carta de indeferimento ou notificação de corte.",
            "Celular com acesso ao gov.br (login e senha), para consultar o Meu INSS durante a conversa.",
            "Número do benefício e extrato do CNIS (Meu INSS).",
            "Laudos, exames e documentos enviados ao INSS no pedido.",
        ],
        "duvidas": [
            ("Qual é o prazo para recorrer?", "O recurso ao INSS deve ser apresentado em até 30 dias a partir do conhecimento da decisão."),
            ("Posso ir direto à Justiça?", "Depende do caso. A análise da carta e dos documentos mostra qual caminho é mais adequado."),
        ],
    },
]


def pagina(s):
    area_nome, area_slug = s["area"]
    url = f"{SITE}{area_slug}/{s['slug']}/"
    whats = link_whats(s["assunto"])
    p = "../../"
    duvidas = s["duvidas"]
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "name": s["nome"],
                "serviceType": s["nome"],
                "url": url,
                "description": s["sub"],
                "provider": {"@id": f"{SITE}#escritorio"},
                "areaServed": {"@type": "City", "name": "Guarujá do Sul"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE},
                    {"@type": "ListItem", "position": 2, "name": area_nome, "item": f"{SITE}{area_slug}/"},
                    {"@type": "ListItem", "position": 3, "name": s["nome"], "item": url},
                ],
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}}
                    for q, r in duvidas
                ],
            },
        ],
    }
    extra = f'<script type="application/ld+json">\n{json.dumps(ld, ensure_ascii=False, indent=2)}\n</script>\n'
    atend = "\n".join(f"<li><h3>{e(t)}</h3><p>{e(d)}</p></li>" for t, d in s["atendimento"])
    docs = "\n".join(f"<li>{e(d)}</li>" for d in s["documentos"])
    duv = "\n".join(f'<div class="duvida"><h3>{e(q)}</h3><p>{e(r)}</p></div>' for q, r in duvidas)
    outros = "\n".join(
        f'<a href="../{o["slug"]}/" class="outra-area">{e(o["nome"])}</a>'
        for o in SERVICOS if o["area"] == s["area"] and o["slug"] != s["slug"]
    )
    return cabeca(s["titulo"], s["descricao"], url, p, extra, tipo="website") + f"""
<main id="principal" tabindex="-1">
<section class="hero hero-area">
<div class="caixa hero-area-texto">
<nav aria-label="Você está em" class="trilha"><a href="{p}">Início</a> <span aria-hidden="true">›</span> <a href="../">{e(area_nome)}</a> <span aria-hidden="true">›</span> <span aria-current="page">{e(s['nome'])}</span></nav>
<h1>{e(s['h1'])}</h1>
<p class="hero-sub">{e(s['sub'])}</p>
<div class="botoes">
<a href="{whats}" class="botao botao-branco">Falar sobre {e(s['nome'] if s['nome'] == 'BPC/LOAS' else s['nome'][0].lower() + s['nome'][1:])}</a>
<a href="{AGENDA}" target="_blank" rel="noopener" class="botao botao-contorno-claro">Agendar uma conversa</a>
</div>
</div>
</section>

<article class="caixa artigo">
{s['secoes']}
</article>

<section class="faixa-cinza">
<div class="caixa area-pagina">
<h2>Como é o atendimento</h2>
<ul class="servicos">
{atend}
</ul>
</div>
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
{duv}
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
<h2>Outros assuntos de {e(area_nome)}</h2>
{outros}
<a href="../" class="outra-area">Todos os serviços de {e(area_nome)}</a>
</div>
</section>
</main>
""" + rodape(p, whats)


def main():
    sm = RAIZ / "sitemap.xml"
    texto = sm.read_text(encoding="utf-8")
    for s in SERVICOS:
        d = RAIZ / s["area"][1] / s["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(pagina(s), encoding="utf-8", newline="\n")
        u = f"{SITE}{s['area'][1]}/{s['slug']}/"
        if u not in texto:
            texto = texto.replace("</urlset>", f"  <url><loc>{u}</loc></url>\n</urlset>")
        print("ok", s["slug"])
    sm.write_text(texto, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
