import requests
from controllers.Token import *
from util.constants import URL_API
import json
from flask import Flask


class Titulos(object):

    def __init__(self):
        self.headers = {'Authorization': f'Bearer {Token.getToken()}'}

    def getTitulos(self):
        response = requests.get(f'{URL_API}/Titulos/FCI', headers=self.headers)
        res = {'response': response.json()}
        return res

    def getCotizaciones(self, pais):
        response = requests.get(
            f'{URL_API}/{pais}/Titulos/Cotizacion/Instrumentos', headers=self.headers)
        res = {'response': response.json()}

        return res

    def get_serie_historica(self, mercado, simbolo, desde, hasta):
        response = requests.get(
            f'{URL_API}/{mercado}/Titulos/{simbolo}/Cotizacion/seriehistorica/{desde}/{hasta}/ajustada', headers=self.headers)
        res = {'response': response.json()}
        return res
