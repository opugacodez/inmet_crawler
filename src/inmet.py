import requests
import json
import urllib.parse

class inmet:

    """ 
        Cria uma instancia para extrair dados do site https://portal.inmet.gov.br/ baseado 
        em seus próprios métodos de obtenção de dados através de consultas em APIs do próprio
        INMET (Instituto Nacional de Meteorologia)

        CONSTANTS:
        - _API_PREV3 : str -> URL da API interna de previsão meteorológica utilizada pelo site.

        - _HEADERS: str -> configuração padrão de cabeçalho para as requisições.

        ATTRIBUTES:
        - session: requests -> sessão requests para efetuar as requisições

        METHODS:
        - busca_cidade: json -> retorna uma ou mais cidades.

        - previsao_por_capital: json -> retorna os dados de previsão do tempo do dia atual e dos
          próximos 4 dias de todas as capitais do país.

        - previsao_por_cidade: json -> retorna os dados de previsão do tempo do dia atual e dos
          próximos 4 dias de uma cidade específica.
    """


    _API_PREV3 = 'https://apiprevmet3.inmet.gov.br'
    _HEADERS = {
        'Content-Type': 'application/json;charset=utf-8'
    }

    def __init__(self) -> None:
        self.session = requests.Session()

    def busca_cidade(
        self,
        nome_cidade: str
    ) -> json:
        
        """
            Retorna uma ou mais cidades.

            PARAMS:
            - nome_cidade: str -> nome da cidade para busca.
        """

        response = self.session.get(self._API_PREV3 + '/autocomplete/%s' % urllib.parse.quote(nome_cidade), headers=self._HEADERS)

        return json.loads(response.text) if response.status_code == 200 else  json.loads({
            'status_code': response.status_code,
            'reason': response.reason,
            'content': response.text
        })

    def previsao_por_capital(
        self,
    ) -> json:

        """
            Retorna os dados de previsão do tempo do dia atual e dos
            próximos 4 dias de todas as capitais do país
        """

        response = self.session.get(self._API_PREV3 + '/previsao/capitais',  headers=self._HEADERS)

        return json.loads(response.text) if response.status_code == 200 else json.loads({
            'status_code': response.status_code,
            'reason': response.reason,
            'content': response.text
        })

    def previsao_por_cidade(
        self,
        id_cidade: str
    ) -> json:
        
        """
            Retorna os dados de previsão do tempo do dia atual e dos próximos 4 dias de uma cidade específica. 

            PARAMS:
            - id_cidade: str -> ID da cidade encontrada no objeto retornado pelo método 'busca_cidade'.
        """
        
        response = self.session.get(self._API_PREV3 + '/previsao/%i' % id_cidade)

        return json.loads(response.text) if response.status_code == 200 else json.loads({
            'status_code': response.status_code,
            'reason': response.reason,
            'content': response.text
        })