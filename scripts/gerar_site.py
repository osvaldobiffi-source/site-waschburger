"""Gera o site inteiro na ordem certa: áreas (e menu/sitemap), serviços, artigos.
Depois põe <lastmod> em cada URL do sitemap.
Uso: python scripts/gerar_site.py
"""
import re
import subprocess
from datetime import date

import gerar_paginas, gerar_servicos, gerar_artigos
from gerar_paginas import RAIZ, SITE


def data_da_pagina(arquivo):
    """Data do último commit da página; hoje se ela mudou e ainda não foi commitada."""
    rel = arquivo.relative_to(RAIZ).as_posix()
    def git(*args):
        return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True)
    # git diff ignora diferença só de fim de linha (CRLF/LF); git status não ignora.
    novo = not git("ls-files", "--", rel).stdout.strip()
    if novo or git("diff", "--quiet", "HEAD", "--", rel).returncode:
        return date.today().isoformat()
    return git("log", "-1", "--format=%cs", "--", rel).stdout.strip() or date.today().isoformat()


def lastmod_no_sitemap():
    sm = RAIZ / "sitemap.xml"
    xml = sm.read_text(encoding="utf-8")

    def troca(m):
        url = m.group(1)
        arquivo = RAIZ / url[len(SITE):] / "index.html"
        return f"<url><loc>{url}</loc><lastmod>{data_da_pagina(arquivo)}</lastmod></url>"

    xml = re.sub(r"<url><loc>([^<]+)</loc>(?:<lastmod>[^<]*</lastmod>)?</url>", troca, xml)
    sm.write_text(xml, encoding="utf-8", newline="\n")
    print("ok lastmod no sitemap")


gerar_paginas.main()
gerar_servicos.main()
gerar_artigos.main()
lastmod_no_sitemap()
