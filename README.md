# Análise de Consumo de Energia em Aviários de Frango de Corte

Este repositório é destinado a analisar o consumo de energia em aviários de frango de corte.

**Metas de Produção:**
- **Dias de Vida alvo:** 46 dias
- **Peso Vivo alvo:** 3,250 kg por ave viva
- **Mortalidade padrão:** 6% ao final do lote (acumulado)

**Terminologia:**
- **Aviários:** Estruturas onde os frangos de corte são criados para o abate.
- **Lotes:** Ciclos de criação de frango de corte, do alojamento ao abate.
- **Lote composto:** O conjunto de número de "aviario-lote", por exemplo `171-165`.

## Fontes de Dados

- **Informações dos Lotes:**
  - Localização: `/assets/dados_lotes_filtrados_projeto_BESS.csv`
  - Formato: CSV (utf-8, separador ";")
- **Informação de Consumo dos Lotes:**
  - Localização: Subpastas em `/data/raw` (separados por Produtores/lotes)
  - Formato: Planilha Excel
- **Área dos Aviários:**
  - Localização: `/assets/area_aviarios.md`
  - Formato: Tabela Markdown

## Estrutura do Projeto

```
/
├── assets/                  # Arquivos de dados auxiliares
├── data/
│   ├── raw/                 # Dados brutos de consumo dos lotes
│   └── processed/           # Dados processados e limpos
├── src/
│   ├── utils/
│   │   └── logger.py        # Módulo de logging
│   ├── data_loader.py       # Módulo para carregar os dados
│   ├── data_cleaner.py      # Módulo para limpar e transformar os dados
│   ├── data_analyzer.py     # Módulo para analisar os dados
│   └── data_saver.py        # Módulo para salvar os dados processados
├── main.py                  # Script principal para orquestrar o processo
├── README.md                # Documentação do projeto
└── roadmap.md               # Próximas etapas do projeto
```

## Processamento de Dados (ETL)

O script `main.py` orquestra um processo de Extração, Transformação e Carga (ETL) que realiza as seguintes etapas:

1.  **Carregamento dos Dados:**
    - Carrega as informações dos lotes do arquivo CSV.
    - Carrega os dados de consumo de energia dos arquivos Excel.
    - Carrega os dados da área dos aviários do arquivo Markdown.

2.  **Limpeza e Transformação:**
    - **Filtra dados semanais:** Mantém apenas os dados diários, removendo os subtotais semanais.
    - **Filtra consumo de energia:** Remove linhas sem valores válidos de consumo de energia (`Energia (kWh)`).
    - **Filtra consumo de energia > 0:** Mantém apenas os registros onde o consumo de energia é maior que zero.
    - **Remove colunas indesejadas:** Elimina colunas que contêm 'Unnamed' ou 'Ref.' em seus nomes.
    - **Renomeia e extrai o dia de criação:** A coluna 'Semanas' é renomeada para 'dia_criacao' e o valor numérico do dia é extraído.
    - **Remove o sufixo `.xlsx`:** O sufixo `.xlsx` é removido da coluna `source_file` para ser usada como chave de junção.

3.  **Junção dos Dados:**
    - Extrai o número do aviário da coluna `source_file`.
    - Junta os dados de consumo de energia com os dados da área dos aviários usando o número do aviário como chave.

4.  **Armazenamento dos Dados:**
    - Salva o conjunto de dados processado e unido em:
      - `data/processed/dados_processados.csv` (formato CSV)
      - `data/processed/dados_processados.db` (formato SQLite)

## Como Executar

1.  **Pré-requisitos:**
    - Python 3
    - `pandas`
    - `openpyxl` (para ler arquivos Excel)

2.  **Execução:**
    ```bash
    python3 main.py
    ```

## Objetivos

- **[Concluído]** Carregar e tratar os dados, criando um pipeline de ETL robusto.
- **[Próximas Etapas]** Extrair KPIs para a análise, como:
  - kwh por ave
  - kwh média por dia de criação de aves
  - pico de kwh por aviário e em mediana por dia de criação
  - outras análises pertinentes que um LLM possa sugerir.
- **[Próximas Etapas]** Desenvolver modelos de machine learning para prever o consumo de energia e outros KPIs.
- **[Próximas Etapas]** Criar visualizações e um dashboard para explorar os dados.