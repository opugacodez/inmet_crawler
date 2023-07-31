"""
    `inmet_crawler` allows the extraction of meteorological data from the website of the
    [National Institute of Meteorology (INMET)](https://portal.inmet.gov.br/) through its own APIs.
"""

import requests
import urllib.parse

__all__ = [
    'session',
    'busca_cidade',
    'previsao_por_capital',
    'previsao_por_cidade',
    'estacao_proxima'
]
    
_API_PREV3 = 'https://apiprevmet3.inmet.gov.br'
_HEADERS = {
    'Content-Type': 'application/json;charset=utf-8',
}

session = requests.Session()

def _parse_response(response: requests.Response) -> list | dict:
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return {
                'status_code': response.status_code,
                'reason': response.reason,
                'content': response.text
            }

def busca_cidade(nome_cidade: str) -> list | dict:
    
    """

        Return information about one or more cities based on the provided name.

        Params:
        - nome_cidade: str -> city name for the search.
        
    """
    url = f'{_API_PREV3}/autocomplete/{urllib.parse.quote(nome_cidade)}'
    response = session.get(url, headers=_HEADERS)
    return _parse_response(response)

def previsao_por_capital() -> dict:

    """
        Return the weather forecast data for the current day and the next 4 days for all capital
        cities of the country.
    """
    url = f'{_API_PREV3}/previsao/capitais'
    response = session.get(url, headers=_HEADERS)
    return _parse_response(response)

def previsao_por_cidade(geocode: int) -> dict:
    
    """
        Returns the weather forecast data for the current day and the next 4 days of a sepcific city

        Params:
        - geocode: int -> Geolocaltion code of the city found in the object returned by the `busca_cidade` function.
    """
    url = f'{_API_PREV3}/previsao/{geocode}'
    response = session.get(url, headers=_HEADERS)
    return _parse_response(response)

def estacao_proxima(geocode: int) -> dict:

    """
        Returns information about an automatic meteorological station located near the
        geolocation of the specified city, along with the current UTC weather data.

        Params:
        - geocode: int -> Geolocaltion code of the city found in the object returned by the `busca_cidade` function.
    """
    url = f'{_API_PREV3}/estacao/proxima/{geocode}'
    reponse = session.get(url, headers=_HEADERS)
    return _parse_response(reponse)