# INMET (Instituto Nacional de Meteorologia) Crawler
Uma ferramenta que utiliza técnicas de web crawler para obter dados do portal do [Instituto Nacional de Meteorologia (INMET)](https://portal.inmet.gov.br/) através do uso da biblioteca `requests` em Python. O código automatiza o processo de extração de informações meteorológicas do INMET, fornecendo acesso a dados atualizados relacionados às condições climáticas em várias localidades do pais.

O objetivo deste projeto é facilitar o acesso a informações meteorológicas para uma varidade de finalidades, desde análises científicas e monitoramento do clima até o desenvolvimento de aplicativos e serviços relacionados. Através do web crawler implementado, o código pode explorar a API disponibilizada pelo INMET, acessando endpoints específicos para recuperar dados.

O projeto é desenvolvido sobre uma licença que incentiva outros desenvolvedores a utilizar, copiar, modificar e mesclar este código. O objetivo do projeto é promover o compartilhamento e a colaboração na comunidade de desenvolvimento, permitindo que este código seja uma base sólida para futuros projetos e aplicações relacionadas ao clima no pais.

## Como usar?

Usar o `inmet_crawler` é muito simples:

    import inmet_crawler
    
    cities = inmet_crawler.busca_cidade(nome_cidade='Sao Paulo')
    sp = cities[0]
    weather_forecast = inmet_crawler.previsao_por_cidade(geocode=sp['geocode'])

No exemplo acima:

 1. O módulo `inmet_crawler` é importando.
 2. Uma pesquisa por cidades é feita a partir do nome "Sao Paulo" através da função `busca_cidade`.
 3. O primeiro valor da lista de cidades em `cities` obtida pela busca é armazenado na variável `sp`.
 4.  Uma variável `weather_forecast` é criada para armazenar os dados de previsão do tempo obtidos atráves da função `previsao_por_cidade`.

## Observações

`inmet_crawler` suporta oficialmente 3.7+.

O projeto está em fase inicial de testes e sua colaboração é muito importante para o seu desenvolvimento contínuo e aprimoramento. Caso você deseje contribuir com o projeto, existem várias maneiras pelas quais você pode participar:

1. **Testando o código**: Você pode ajudar testando o código em diferentes cenários e ambientes para identificar possíveis bugs ou problemas. Relatar problemas encontrados nos registros de problemas (issues) no GitHub é uma forma valiosa de contribuir.
2. **Melhorando a documentação**: Contribuir com melhorias na documentação, incluindo detalhes adicionais sobre o funcionamento dos métodos, exemplos de uso e instruções de instalação, pode ajudar outros usuários a entenderem e utilizarem o projeto de forma mais eficiente.
3. **Implementando novos recursos**: Caso você tenha ideias de novos recursos ou funcionalidades para o projeto, pode propor e implementar essas melhorias. Você pode abrir um pull request com o código para revisão e inclusão no projeto.
4. **Corrigindo problemas existentes**: Se você identificar algum problema ou erro no código, pode contribuir corrigindo-o e enviando um pull request para a equipe do projeto revisar e incorporar as alterações.

## Referências

1. [Instituto Nacional de Meteorologia](https://portal.inmet.gov.br/)
2. [Python requests](https://pypi.org/project/requests/)
