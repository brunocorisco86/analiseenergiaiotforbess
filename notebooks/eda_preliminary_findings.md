# Análise Exploratória Preliminar - Consumo de Energia em Lotes de Frango de Corte

## Contexto do Projeto

Este projeto analisa dados de consumo de energia elétrica em lotes de criação de frango de corte, coletados através de sistemas IoT em aviários de diferentes produtores rurais vinculados à C.Vale Cooperativa Agroindustrial.

## Estrutura dos Dados

### Dimensões do Dataset
- **Total de registros**: 2.301 linhas
- **Variáveis**: 14 colunas
- **Lotes únicos**: 53 lotes de criação
- **Aviários únicos**: 5 aviários (170, 171, 785, 883, 1037)
- **Período de criação**: Dias 1 a 49 do ciclo de vida dos frangos

### Variáveis Disponíveis

1. **dia_criacao**: Dia do ciclo de vida do lote (1-49 dias)
2. **Peso (g)**: Peso médio das aves em gramas
3. **GMD (g)**: Ganho Médio Diário em gramas
4. **Mortalidade (un)**: Número de aves mortas
5. **Mortalidade (%)**: Percentual de mortalidade
6. **CA**: Conversão Alimentar real
7. **CA estimada**: Conversão Alimentar estimada
8. **Ração (kg)**: Consumo de ração em quilogramas
9. **Água (l)**: Consumo de água em litros
10. **Energia (kWh)**: **Consumo de energia elétrica em kWh (variável-chave)**
11. **Gás (kg)**: Consumo de gás em quilogramas
12. **lote_composto**: Identificador único do lote (formato: aviario-numero_lote)
13. **aviario**: Número do aviário
14. **metros_quadrados**: Área do aviário em m²

### Características dos Aviários

| Aviário | Área (m²) | Número de Lotes |
|---------|-----------|-----------------|
| 170     | 1.440     | 9               |
| 171     | 1.440     | 9               |
| 785     | 2.250     | 7               |
| 883     | 2.250     | 9               |
| 1037    | 2.400     | 18              |

### Estatísticas Descritivas Principais

#### Consumo de Energia (kWh)
- **Média**: ~50-100 kWh/dia (a ser calculado)
- **Sem valores nulos**: 100% de cobertura
- **Variável completa**: Todos os 2.301 registros possuem medição

#### Peso das Aves
- **Média**: 1.348,67 g
- **Mínimo**: 35,99 g (primeiros dias)
- **Máximo**: 4.111,30 g (final do ciclo)
- **Valores nulos**: 574 registros (24,9%)

#### Conversão Alimentar (CA)
- **Valores nulos**: 673 registros (29,2%)
- Indicador crucial de eficiência produtiva

### Qualidade dos Dados

#### Completude por Variável
- **Energia (kWh)**: 100% completo ✓
- **Água (l)**: 89,4% completo
- **Ração (kg)**: 84,3% completo
- **Mortalidade**: 84,3% completo
- **CA**: 70,8% completo
- **Peso**: 75,1% completo
- **Gás (kg)**: 35,6% completo (muitos valores ausentes)

## Observações Iniciais

1. **Granularidade temporal**: Cada linha representa um dia de vida de um lote específico
2. **Cobertura completa de energia**: A variável principal (Energia kWh) não possui valores ausentes
3. **Variabilidade de tamanho**: Aviários com áreas entre 1.440 m² e 2.400 m²
4. **Ciclo produtivo**: Dados cobrem o ciclo completo de criação (até 49 dias)
5. **Dados de gás limitados**: 64,4% de valores ausentes podem indicar uso não universal

## Próximos Passos da Análise

1. Análise temporal do consumo de energia ao longo do ciclo de vida
2. Comparação de eficiência energética entre aviários
3. Correlação entre consumo de energia e variáveis produtivas (peso, CA, mortalidade)
4. Identificação de padrões e outliers
5. Análise de consumo por área (kWh/m²)
6. Segmentação de perfis de consumo
