#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports()' function so that it returns a list of airport
codes, excluding any combinations like "All".

Refer to the 'options.html' file in the tab above for a stripped down version
of what is actually on the website. The test() assertions are based on the
given file.
"""

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    INICIO_STRING = 0
    TERMINO_STRING = 3

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        valor = soup.find(id="AirportList")

        # Busca pelas tags option contidas na tag cujo id eh AirportList
        for opcoes in valor.find_all('option'):
            # Obtem os atributos na tag como se fosse um dicionario
            aeroporto = opcoes['value']

            # Conceito de slice
            if aeroporto[INICIO_STRING:TERMINO_STRING].upper() != "ALL":
                data.append(aeroporto)

    return data

def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

if __name__ == "__main__":
    test()
