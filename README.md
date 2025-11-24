Repositorio destinado a analisar o consumo de energia em aviários de frango de corte

- Dias de Vida alvo = 46 dias
- Peso Vivo alvo = 3,250 kg por ave viva
- Mortalidade standard = 6% ao final do lote (acumulado)

Aviários: São estruturas onde os frangos de corte são criados para o abate,
Lotes: são ciclos de criacao de frango de corte, do alojamento ao abate
Lote composto: É o conjunto de número de "aviario-lote", por exemplo 171-165

## Informacoes dos lotes
Esta salvo em /assets/dados_lotes_filtrados_projeto_BESS.csv
Formato: csv utf-8 sep=";"

## Informação de consumo dos lotes
Estao seperados por Produtores/lotes em subpastas em /data/raw
Formato: Planilha Excel

## Objetivo
- carregar e tratar os dados eliminando fazendo uma EDA
- Extrair KPIs para a analise
    - kwh por ave
    - kwh média por dia de criacao de aves
    - pico de kwh por aviario e em mediana por dia de criacao
    - outras análises pertinentes que uma llm possa sugerir
