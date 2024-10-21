[![DOI](https://zenodo.org/badge/875832312.svg)](https://doi.org/10.5281/zenodo.13958863)

# pofium

Pacote para baixar, carregar e salvar os microdados da Pesquisa de Orçamentos Familiares (POF) - Atualmente somente para a POF 2017/2018.

A Pesquisa de Orçamentos Familiares (POF) tem seus microdados disponibilizados em arquivos de coluna por largura fixa, em formato `.txt`. Este pacote visa automatizar o processo de download e criação de DataFrames utilizando o Pandas. Ao fim, os DataFrames de cada questionário são salvos em formato `.parquet` no diretório de trabalho que o usuário estiver utilizando.

## Instalação

`pip install pofium`

## Uso

### Para importar o pacote:

`import pofium`

### Para realizar o download e salvar os DataFrames:

`pofium.download()`

### Para consultar variáveis pelo código ou descrição:

`pofium.consulta_var(cod='código', desc='parte da descrição buscada', d=int)`

- Utilize **um** dos parâmetros de busca (`cod` ou `desc`).
- O parâmetro `d` é **obrigatório** e corresponde ao número do questionário cujo dicionário de variáveis será alvo da consulta.
- Caso tenha dúvidas, basta rodar a função sem qualquer parâmetro:

`pofium.consulta_var()`

A resposta será a lista dos questionários e seus respectivos números.

### Para consultar as características de uma variável:

`pofium.descreva_var(cod='código', d=int)`

O retorno será as características da variável (se indica categorias e quais são). Se o retorno for nulo, a variável não tem características descritas no dicionário disponibilizado pelo IBGE.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
