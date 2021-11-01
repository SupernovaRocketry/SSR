# SSR
 Repositório destinado ao supervisório SSR.

## O Projeto
Esse repositório contém o Supervisório Supernova Rocketry, projeto feito para monitorar o lançamento de mini foguetes e realizar testes com um banco estático. Associado a esse projeto, existe o repositório *simuladorSSR*, que serve como simulador de dados de voo para testes. 

Para o monitoramento do foguete, o supervisório deverá receber e mostrar os seguintes dados:

1. Altitude.
2. Posição (latitude e longitude).
2. Aceleração nos três eixos.
3. Angulação nos três eixos.
4. Qualidade do sinal da antena (RSSI).

## Andamento do projeto
- [X] Interface Gráfica
    - [X] Cabeçalho.
    - [X] Ambiente superior booleano
    - [X] Ambiente lateral com dados em tempo real.
    - [X] Ambiente gráfico.
- [X] Recebimento de dados em tempo real.
- [ ] Multiprocessamento.
- [ ] Abas com dados específicos.
- [ ] Geração de relatórios automatizada.
- [ ] Aba para banco estático.


## Instalação
Ao realizar o download do projeto, é necessário instalar o ambiente virtual e todos os pacotes utilizados no projeto. Para isso, basta executar no terminal os seguintes comandos:

1. pip install virtualenv
2. python -m virtualenv .env
3. .env\Scripts\Activate
4. pip install -r requirements.txt
5. python -m pip install kivy_garden.graph

## Considerações finais
Atualizado por: [Thiago Saber](https://github.com/ThiiD).

Repositório criado em 11/05/2021
