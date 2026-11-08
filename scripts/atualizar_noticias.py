"""Atualiza noticias.json com as notícias mais recentes de fontes oficiais.

Roda uma vez por dia pelo GitHub Actions (.github/workflows/noticias.yml).
Usa só a biblioteca padrão do Python.
"""
import email.utils
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

SAIDA = Path(__file__).resolve().parent.parent / "noticias.json"
POR_AREA = 6
DIAS = 45

SITES_OFICIAIS = (
    "site:gov.br OR site:stj.jus.br OR site:stf.jus.br OR site:tst.jus.br "
    "OR site:senado.leg.br OR site:camara.leg.br OR site:agenciabrasil.ebc.com.br"
)

AREAS = {
    "tributario": {
        "busca": '(tributária OR tributário OR imposto OR ICMS OR "PIS" OR Cofins OR CBS OR IBS OR "Receita Federal")',
        "feeds": ["https://www.gov.br/receitafederal/pt-br/assuntos/noticias/RSS"],
        "palavras": r"tribut|impost|icms|\bpis\b|cofins|\bcbs\b|\bibs\b|receita federal|fiscal|parcelamento|simples nacional",
    },
    "previdenciario": {
        "busca": '(INSS OR aposentadoria OR previdência OR "auxílio-acidente" OR "benefício previdenciário" OR BPC)',
        "feeds": ["https://www12.senado.leg.br/noticias/rss", "https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml"],
        "palavras": r"\binss\b|aposentad|previd|auxílio|benefício|\bbpc\b|pensão",
    },
}

# Páginas de serviço que o Google Notícias às vezes devolve como se fossem notícia.
DESCARTAR = re.compile(r"^(solicitar|consultar|receber|bem-vindo|páginas|meu inss|sistema nacional"
                       # Programas de rádio/TV do Senado: o título é o nome do programa, não a notícia.
                       r"|onze minutos|edição da (manhã|tarde|noite)|senado notícias|conexão senado"
                       r"|repórter senado|rádio senado|a voz do brasil|senado em pauta|home page)\b", re.I)
# Temas que batem nas palavras-chave mas não interessam ao cliente (ex.: "aposentadoria compulsória" de juiz punido).
FORA_DO_TEMA = re.compile(r"compulsória|desembargador|magistrad|condena|operação |login", re.I)
# Fontes estaduais e municipais ficam de fora: o foco é a esfera federal.
FONTES_FORA = re.compile(r"prefeitura|assembleia|governo d[eoa] |câmara municipal|agenciasp|sefaz|\.sp\.gov|\.pr\.gov", re.I)


def baixar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (site Waschburger Advocacia)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def data(texto):
    if not texto:
        return None
    try:
        d = email.utils.parsedate_to_datetime(texto)
    except (TypeError, ValueError):
        try:
            d = datetime.fromisoformat(texto.replace("Z", "+00:00"))
        except ValueError:
            return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def ler_feed(xml, fonte_padrao=""):
    raiz = ET.fromstring(xml)
    atom = "{http://www.w3.org/2005/Atom}"
    itens = []
    for i in raiz.iter("item"):
        itens.append({
            "titulo": (i.findtext("title") or "").strip(),
            "link": (i.findtext("link") or "").strip(),
            "fonte": (i.findtext("source") or fonte_padrao).strip(),
            "data": data(i.findtext("pubDate")),
        })
    for e in raiz.iter(atom + "entry"):
        link = e.find(atom + "link")
        itens.append({
            "titulo": (e.findtext(atom + "title") or "").strip(),
            "link": link.get("href", "") if link is not None else "",
            "fonte": fonte_padrao,
            "data": data(e.findtext(atom + "updated") or e.findtext(atom + "published")),
        })
    return itens


def nome_fonte(url):
    host = urllib.parse.urlparse(url).netloc
    if "receitafederal" in url:
        return "Receita Federal"
    if "senado" in host:
        return "Agência Senado"
    if "agenciabrasil" in host:
        return "Agência Brasil"
    return host


def limpar_titulo(item):
    t = re.sub(r"\s+", " ", item["titulo"])
    fonte = item["fonte"]
    # O Google Notícias termina o título com " - Fonte".
    if fonte and t.endswith(" - " + fonte):
        t = t[: -len(fonte) - 3]
    t = re.sub(r"\s+[—-]\s+(GOV\.BR|www\.gov\.br|Governo Federal)$", "", t)
    # Páginas do gov.br trazem o órgão no fim: "Título — Receita Federal".
    m = re.match(r"(.+?)\s+—\s+(.+)$", t)
    if m and re.match(r"(gov\.br|www\.gov\.br|governo federal)$", fonte, re.I):
        t, fonte = m.group(1), m.group(2)
    return t.strip(), apelido_fonte(fonte)


def apelido_fonte(fonte):
    f = fonte.strip()
    for padrao, nome in (
        (r"^stf", "STF"),
        (r"^stj", "STJ"),
        (r"^senado$", "Agência Senado"),
        (r"inss", "INSS"),
        (r"^(gov\.br|www\.gov\.br)$", "Gov.br"),
    ):
        if re.search(padrao, f, re.I):
            return nome
    return f


def coletar(area):
    cfg = AREAS[area]
    itens = []
    q = urllib.parse.quote(f"{cfg['busca']} ({SITES_OFICIAIS}) when:{DIAS}d")
    url_google = f"https://news.google.com/rss/search?q={q}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    try:
        itens += ler_feed(baixar(url_google))
    except Exception as e:  # uma fonte fora do ar não pode derrubar as outras
        print(f"[{area}] Google Notícias falhou: {e}")
    for url in cfg["feeds"]:
        try:
            itens += ler_feed(baixar(url), nome_fonte(url))
        except Exception as e:
            print(f"[{area}] {url} falhou: {e}")
    filtro = re.compile(cfg["palavras"], re.I)
    itens = [i for i in itens if filtro.search(i["titulo"]) and not FORA_DO_TEMA.search(i["titulo"])
             and not FONTES_FORA.search(i["fonte"])]

    limite = datetime.now(timezone.utc) - timedelta(days=DIAS)
    vistos, saida = set(), []
    for it in sorted((i for i in itens if i["data"] and i["data"] >= limite), key=lambda i: i["data"], reverse=True):
        titulo, fonte = limpar_titulo(it)
        chave = re.sub(r"\W+", "", titulo.lower())[:60]
        if not titulo or not it["link"].startswith("http") or chave in vistos or DESCARTAR.match(titulo):
            continue
        vistos.add(chave)
        saida.append({"titulo": titulo, "link": it["link"], "fonte": fonte, "data": it["data"].isoformat()})
        if len(saida) == POR_AREA:
            break
    return saida


def main():
    anterior = json.loads(SAIDA.read_text(encoding="utf-8")) if SAIDA.exists() else {}
    novo = {"atualizado": datetime.now(timezone.utc).isoformat(timespec="minutes")}
    for area in AREAS:
        itens = coletar(area)
        # Se todas as fontes falharem, mantém as notícias do dia anterior.
        novo[area] = itens or anterior.get(area, [])
        print(f"[{area}] {len(itens)} notícias")
    SAIDA.write_text(json.dumps(novo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
