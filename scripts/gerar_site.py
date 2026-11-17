"""Gera o site inteiro na ordem certa: áreas (e menu/sitemap), serviços, artigos.
Uso: python scripts/gerar_site.py
"""
import gerar_paginas, gerar_servicos, gerar_artigos

gerar_paginas.main()
gerar_servicos.main()
gerar_artigos.main()
