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
        Retorna informações sobre uma ou mais cidades a partir do nome fornecido.

        PARAMS:
        - nome_cidade: str -> nome da cidade para busca.
    """
    url = f'{_API_PREV3}/autocomplete/{urllib.parse.quote(nome_cidade)}'
    response = session.get(url, headers=_HEADERS)
    return _parse_response(response)

def previsao_por_capital() -> dict:

    """
        Retorna os dados de previsão do tempo atual e dos próximos 4 dias de todas as capitais do país.
    """
    url = f'{_API_PREV3}/previsao/capitais'
    response = session.get(url, headers=_HEADERS)
    return _parse_response(response)

def previsao_por_cidade(geocode: int) -> dict:
    
    """
        Retorna os dados de previsão do tempo do dia atual e dos próximos 4 dias de uma cidade específica. 

        PARAMS:
        - geocode: int -> código de localização da cidade encontrada no objeto retornado pelo método 'busca_cidade'.
    """
    url = f'{_API_PREV3}/previsao/{geocode}'
    response = session.get(url, headers=_HEADERS)
    return _parse_response(response)

def estacao_proxima(geocode: int) -> dict:

    """
        Retorna informações de uma estação meteorológica automática localizada em ou próximo da geolocalização
        do município informado, com base no código de localização (geocode), juntamente com os dados do tempo no  intervalo UTC atual.

        PARAMS:
        - geocode: int -> código de localização da cidade encontrada no objeto retornado pelo método 'busca_cidade'.
    """
    url = f'{_API_PREV3}/estacao/proxima/{geocode}'
    reponse = session.get(url, headers=_HEADERS)
    return _parse_response(reponse)