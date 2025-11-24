# Roadmap do Projeto

Este arquivo descreve as próximas etapas planejadas para o projeto de análise de consumo de energia em aviários.

## Fase 1: Análise Exploratória de Dados (EDA) e Visualização

- [ ] **Análise Descritiva Aprofundada:**
  - Calcular estatísticas descritivas para as principais variáveis (consumo de energia, peso das aves, mortalidade, etc.).
  - Analisar a distribuição das variáveis para identificar outliers e anomalias.

- [ ] **Criação de KPIs:**
  - Calcular e analisar os seguintes Indicadores Chave de Performance (KPIs):
    - Consumo de energia por ave (`kwh por ave`).
    - Consumo médio de energia por dia de criação (`kwh média por dia de criacao de aves`).
    - Pico de consumo de energia por aviário e por dia de criação.
    - Densidade de aves por metro quadrado (`aves por m²`).
    - Consumo de energia por metro quadrado (`kwh por m²`).

- [ ] **Visualizações:**
  - Criar gráficos de série temporal para visualizar o consumo de energia ao longo do tempo para cada lote.
  - Gerar gráficos de dispersão para explorar a relação entre o consumo de energia e outras variáveis (e.g., `Peso (g)`, `GMD (g)`, `Mortalidade (%)`).
  - Criar box plots para comparar o consumo de energia entre diferentes aviários e produtores.
  - Desenvolver um mapa de calor para visualizar a correlação entre as variáveis.

## Fase 2: Modelagem de Machine Learning

- [ ] **Preparação dos Dados para Modelagem:**
  - Selecionar as features mais relevantes para a modelagem.
  - Dividir os dados em conjuntos de treino e teste.
  - Implementar o scaling e a normalização das features, se necessário.

- [ ] **Modelos de Regressão para Previsão de Consumo:**
  - Desenvolver e treinar modelos de regressão (e.g., Regressão Linear, Random Forest, Gradient Boosting) para prever o consumo de energia (`Energia (kWh)`).
  - Avaliar a performance dos modelos usando métricas como RMSE, MAE e R².

- [ ] **Modelos para Previsão de KPIs de Produção:**
  - Desenvolver modelos para prever outros KPIs importantes, como `Conversão Alimentar`, `GMD` (Ganho de Massa Diário) e `Mortalidade`.

- [ ] **Otimização dos Modelos:**
  - Realizar a sintonia de hiperparâmetros (hyperparameter tuning) para otimizar a performance dos melhores modelos.

## Fase 3: API e Dashboard

- [ ] **Desenvolvimento de uma API:**
  - Criar uma API RESTful (usando FastAPI ou Flask) para servir os dados processados e as previsões dos modelos.
  - Documentar a API (e.g., usando Swagger/OpenAPI).

- [ ] **Criação de um Dashboard Interativo:**
  - Desenvolver um dashboard (usando Streamlit, Dash ou outra ferramenta) para:
    - Visualizar os dados brutos e processados.
    - Apresentar os KPIs e as análises de forma interativa.
    - Exibir as previsões dos modelos de machine learning.

## Fase 4: Automação e MLOps

- [ ] **Implementação de um Pipeline de CI/CD:**
  - Configurar um pipeline de Integração Contínua/Entrega Contínua (usando GitHub Actions ou GitLab CI/CD) para automatizar:
    - O processo de ETL.
    - O treinamento e a avaliação dos modelos.
    - O deploy da API e do dashboard.
- [ ] **Monitoramento dos Modelos:**
  - Implementar o monitoramento da performance dos modelos em produção para detectar `data drift` e `concept drift`.
  - Configurar alertas para quando a performance dos modelos degradar.
