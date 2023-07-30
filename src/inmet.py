import requests
import json
import urllib.parse

_API_PREV3 = 'https://apiprevmet3.inmet.gov.br'
_HEADERS = {
    'Content-Type': 'application/json;charset=utf-8'
}

class inmet:

    """ 
        Cria uma instancia para extrair dados do site https://portal.inmet.gov.br/ baseado 
        em seus próprios métodos de obtenção de dados através de consultas em APIs do próprio
        INMET (Instituto Nacional de Meteorologia)

        Atributos:
        - `session: requests.Session`

        Métodos:
        - `busca_cidade(city_name: str) -> list | dict`: Retorna informações sobre uma ou mais cidades a partir do nome fornecido.
        - `previsao_por_capital() -> dict`: Retorna os dados de previsão do tempo atual e dos próximos 4 dias de todas as capitais do país.
        - `previsao_por_cidade(geocode: int) -> dict`: Retorna os dados de previsão do tempo atual e dos próximos 4 dias de uma cidade específica com base no código de localização (geocode).
        - `estacao_automatica(geocode: int) -> dict`: Retorna informações de uma estação meteorológica automática localizada em ou próximo da geolocalização do município informado, com base no código de localização (geocode).

    """

    def __init__(self):
        self.session = requests.Session()

    def _parse_response(self, response: requests.Response) -> list | dict:
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return {
                'status_code': response.status_code,
                'reason': response.reason,
                'content': response.text
            }

    def busca_cidade(self, nome_cidade: str) -> list | dict:
        
        """
            Retorna informações sobre uma ou mais cidades a partir do nome fornecido.

            PARAMS:
            - nome_cidade: str -> nome da cidade para busca.
        """
        url = f'{_API_PREV3}/autocomplete/{urllib.parse.quote(nome_cidade)}'
        response = self.session.get(url, headers=_HEADERS)
        return self._parse_response(response)

    def previsao_por_capital(self) -> dict:

        """
            Retorna os dados de previsão do tempo atual e dos
            próximos 4 dias de todas as capitais do país
        """
        url = f'{_API_PREV3}/previsao/capitais'
        response = self.session.get(url, headers=_HEADERS)
        return self._parse_response(response)

    def previsao_por_cidade(self, geocode: int) -> dict:
        
        """
            Retorna os dados de previsão do tempo do dia atual e dos próximos 4 dias de uma cidade específica. 

            PARAMS:
            - geocode: int -> código de localização da cidade encontrada no objeto retornado pelo método 'busca_cidade'.
        """
        url = f'{_API_PREV3}/previsao/{geocode}'
        response = self.session.get(url, headers=_HEADERS)
        return self._parse_response(response)
    
    def estacao_proxima(self, geocode: int) -> dict:
        
        """
            Retorna dados de uma estação meteorológica automática
            localizada em um ponto fixo na ou próximo da geolocalização do município informado

            PARAMS:
            - geocode: int -> código de localização da cidade encontrada no objeto retornado pelo método 'busca_cidade'.
        """
        url = f'{_API_PREV3}/estacao/proxima/{geocode}'
        reponse = self.session.get(url, headers=_HEADERS)
        return self._parse_response(reponse)