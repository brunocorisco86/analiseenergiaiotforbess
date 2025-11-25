# Análise de Perfis de Consumo de Energia em Aviários de Frango de Corte

---

## Slide 1: Título
**Título:** Análise de Perfis de Consumo de Energia em Aviários de Frango de Corte
**Subtítulo:** Insights para Otimização Energética e Redução de Custos
**Autor:** Análise de Negócios - Manus AI
**Data:** Novembro 2025

**Preferências visuais:** Utilizar paleta de cores da C.Vale Cooperativa Agroindustrial com adição da cor ouro velho. Aspecto 16:9.

---

## Slide 2: Contexto e Objetivo da Análise
**Título:** Dados IoT revelam oportunidades de eficiência energética em 5 aviários integrados

**Conteúdo:**
O consumo de energia elétrica representa um dos principais custos operacionais na avicultura de corte, impactando diretamente a rentabilidade dos produtores integrados. Esta análise exploratória examina dados coletados por sensores IoT em 5 aviários de produtores vinculados à C.Vale Cooperativa Agroindustrial, abrangendo 53 lotes de criação e 2.280 registros diários ao longo de ciclos completos de 49 dias.

**Objetivos principais:**
- Identificar padrões de consumo de energia ao longo do ciclo de vida dos frangos
- Comparar a eficiência energética entre diferentes aviários
- Correlacionar o uso de energia com indicadores-chave de produção (peso, conversão alimentar, mortalidade)
- Quantificar oportunidades de economia e fornecer recomendações práticas para otimização

A análise utiliza dados consolidados de consumo diário de energia (kWh), permitindo uma visão granular do comportamento energético em cada fase do ciclo produtivo.

---

## Slide 3: Visão Geral dos Dados Analisados
**Título:** Dataset robusto com 2.280 registros diários de 53 lotes em 5 aviários

**Conteúdo:**
A base de dados analisada oferece uma cobertura abrangente do consumo energético na produção avícola, com as seguintes características:

**Dimensões do estudo:**
- **2.280 registros diários** após tratamento de outliers extremos (21 registros removidos)
- **53 lotes de criação** distribuídos em 5 aviários de diferentes tamanhos
- **5 aviários** com áreas variando de 1.440 m² a 2.400 m²
- **Ciclo completo:** 1 a 49 dias de vida dos frangos

**Cobertura de dados por aviário:**
- Aviário 170: 1.440 m², 10 lotes
- Aviário 171: 1.440 m², 9 lotes
- Aviário 785: 2.250 m², 7 lotes
- Aviário 883: 2.250 m², 9 lotes
- Aviário 1037: 2.400 m², 18 lotes (maior representatividade)

**Qualidade dos dados:** A variável-chave "Energia (kWh)" apresenta 100% de completude, garantindo a confiabilidade das análises. Outras variáveis produtivas (peso, conversão alimentar, mortalidade) possuem entre 70% e 85% de cobertura, suficiente para análises de correlação.

---

## Slide 4: Perfil de Consumo ao Longo do Ciclo
**Título:** Consumo de energia segue padrão em "U" com picos no início e final do ciclo

**Conteúdo:**
A análise temporal revela um comportamento característico do consumo de energia ao longo dos 49 dias do ciclo de criação, refletindo as necessidades fisiológicas das aves e as práticas de manejo ambiental.

**Padrão identificado:**
- **Fase 1 - Aquecimento (dias 1-10):** Consumo elevado devido à necessidade de aquecimento artificial para pintinhos, que ainda não regulam adequadamente sua temperatura corporal. Nesta fase, o consumo médio pode ultrapassar 400 kWh/dia em alguns aviários.

- **Fase 2 - Crescimento (dias 11-25):** Redução e estabilização do consumo à medida que as aves desenvolvem termorregulação. O consumo médio nesta fase é o mais baixo do ciclo, em torno de 150-200 kWh/dia, representando uma janela de maior eficiência energética.

- **Fase 3 - Terminação (dias 26-49):** Aumento gradual do consumo devido à maior necessidade de ventilação e resfriamento. Aves maiores produzem mais calor metabólico, exigindo sistemas de climatização mais intensos. O consumo pode retornar a níveis próximos aos da fase inicial.

**Implicação estratégica:** O gerenciamento energético deve priorizar a otimização nas fases 1 e 3, que concentram os maiores custos. Investimentos em isolamento térmico e sistemas de ventilação eficientes têm maior retorno nessas etapas.

![Evolução do Consumo](images/evolucao_consumo_aviarios.png)

---

## Slide 5: Comparativo de Eficiência entre Aviários
**Título:** Diferença de 73% na eficiência energética entre o melhor e o pior aviário

**Conteúdo:**
A normalização do consumo pela área (kWh/m²) permite uma comparação justa entre aviários de diferentes tamanhos, revelando disparidades significativas na eficiência energética que não podem ser explicadas apenas pela escala das instalações.

**Ranking de eficiência energética (kWh/m²):**
1. **Aviário 1037:** 0,123 kWh/m² (benchmark de eficiência)
2. **Aviário 883:** 0,143 kWh/m² (+16% vs. benchmark)
3. **Aviário 171:** 0,155 kWh/m² (+26% vs. benchmark)
4. **Aviário 785:** 0,207 kWh/m² (+69% vs. benchmark)
5. **Aviário 170:** 0,212 kWh/m² (+73% vs. benchmark)

**Análise de desempenho:**
O aviário 1037, apesar de ser o maior (2.400 m²), demonstra a melhor eficiência energética, sugerindo que economias de escala, melhores práticas de manejo ou equipamentos mais modernos podem estar contribuindo para seu desempenho superior. Em contraste, os aviários 170 e 785 apresentam consumo por m² significativamente mais alto, indicando oportunidades claras de melhoria.

**Fatores potenciais de variação:** Isolamento térmico das instalações, idade e eficiência dos equipamentos de climatização, práticas de manejo operacional, densidade de alojamento e condições climáticas locais.

![Ranking de Eficiência](images/ranking_eficiencia.png)

---

## Slide 6: Análise de Variabilidade e Consistência
**Título:** Aviários 170 e 785 apresentam maior variabilidade no consumo diário

**Conteúdo:**
Além da média de consumo, a análise da variabilidade (dispersão dos dados) fornece insights sobre a consistência operacional e a previsibilidade dos custos energéticos em cada aviário.

**Principais observações:**
- **Aviário 1037:** Apesar de ser o mais eficiente, apresenta variabilidade moderada, com consumo diário concentrado entre 150 e 400 kWh. A consistência sugere processos bem estabelecidos e equipamentos confiáveis.

- **Aviários 170 e 171:** Exibem a maior dispersão de dados, com picos de consumo que podem ultrapassar 1.000 kWh em dias específicos. Essa alta variabilidade indica possíveis problemas de controle ambiental, eventos climáticos extremos ou falhas operacionais que geram consumo atípico.

- **Aviário 883:** Apresenta padrão intermediário, com variabilidade controlada e poucos outliers, sugerindo operação estável.

**Implicação para gestão:** Alta variabilidade dificulta o planejamento financeiro e pode indicar ineficiências operacionais. Aviários com consumo errático devem ser priorizados para auditorias técnicas e implementação de sistemas de monitoramento em tempo real.

![Variabilidade do Consumo](images/variabilidade_consumo.png)

---

## Slide 7: Consumo Total e Distribuição por Aviário
**Título:** Aviário 1037 concentra 34% do consumo total registrado no período analisado

**Conteúdo:**
A análise do consumo total acumulado por aviário revela a distribuição do gasto energético e permite priorizar ações de eficiência com base no impacto potencial.

**Consumo total por aviário:**
- **Aviário 1037:** 232.000 kWh (34% do total) - Maior volume devido ao maior número de lotes analisados (18 lotes)
- **Aviário 785:** 151.000 kWh (22% do total)
- **Aviário 170:** 126.000 kWh (19% do total)
- **Aviário 883:** 123.000 kWh (18% do total)
- **Aviário 171:** 94.000 kWh (14% do total)

**Consumo médio diário geral:** 298 kWh/dia (mediana de 178 kWh/dia)

**Consumo total registrado:** 680.120 kWh no período analisado

**Insight estratégico:** Embora o aviário 1037 seja o mais eficiente por m², seu grande volume de consumo absoluto o torna um alvo prioritário para ações de otimização. Mesmo pequenas melhorias percentuais neste aviário resultarão em economias significativas em termos absolutos.

![Consumo Total por Aviário](images/consumo_total_aviario.png)

---

## Slide 8: Correlação com Indicadores de Produção
**Título:** Consumo de energia não correlaciona diretamente com peso ou ração, mas sim com climatização

**Conteúdo:**
A análise de correlação entre o consumo de energia e os principais indicadores zootécnicos revela insights importantes sobre os drivers do gasto energético na avicultura.

**Principais correlações identificadas:**
- **Energia vs. Dia de Criação:** Correlação negativa fraca (-0,17), refletindo o padrão em "U" com picos no início e final do ciclo.

- **Energia vs. Peso das Aves:** Correlação próxima de zero (0,05), indicando que o crescimento das aves não aumenta linearmente o consumo de energia. Isso contraria a intuição inicial e reforça que o consumo é determinado primariamente por necessidades de climatização, não pelo metabolismo das aves.

- **Energia vs. Consumo de Ração:** Correlação muito baixa (0,03), confirmando que o gasto energético não está diretamente ligado à alimentação, mas sim ao controle térmico do ambiente.

- **Energia vs. Mortalidade:** Sem correlação significativa, sugerindo que o consumo de energia não é um preditor de problemas sanitários.

**Implicação prática:** O foco da gestão energética deve estar em sistemas de aquecimento, ventilação e resfriamento (HVAC), não em processos produtivos diretos. Melhorias no isolamento térmico e na eficiência dos equipamentos de climatização terão maior impacto na redução de custos do que ajustes na nutrição ou densidade de alojamento.

---

## Slide 9: Oportunidades de Economia Identificadas
**Título:** Potencial de redução de 15-20% no consumo energético com adoção de melhores práticas

**Conteúdo:**
Com base no benchmark estabelecido pelo aviário 1037 (0,123 kWh/m²), é possível estimar o potencial de economia se os demais aviários alcançassem níveis similares de eficiência.

**Cenário de otimização:**
- **Aviário 170:** Redução potencial de 32% no consumo (41.000 kWh economizados)
- **Aviário 785:** Redução potencial de 54% no consumo (82.000 kWh economizados)
- **Aviário 171:** Redução potencial de 7% no consumo (7.000 kWh economizados)
- **Aviário 883:** Já opera próximo ao benchmark (economia marginal)

**Economia total estimada:** Aproximadamente 130.000 kWh no período analisado, representando cerca de 19% do consumo total. Considerando um custo médio de R$ 0,60/kWh, isso equivale a uma economia potencial de **R$ 78.000** no período.

**Ações recomendadas para captura de valor:**
1. **Auditoria energética nos aviários 170 e 785:** Identificar falhas de isolamento, equipamentos obsoletos e práticas de manejo ineficientes.
2. **Benchmarking operacional:** Documentar e replicar as práticas do aviário 1037 nos demais.
3. **Investimento em automação:** Implementar sistemas de controle automatizado de temperatura e ventilação para reduzir desperdícios.
4. **Monitoramento em tempo real:** Instalar dashboards de consumo para identificar anomalias rapidamente.

---

## Slide 10: Recomendações Estratégicas
**Título:** Plano de ação em três frentes para capturar oportunidades de eficiência energética

**Conteúdo:**
Com base nos insights da análise, recomenda-se uma abordagem estruturada em três pilares para otimização do consumo de energia nos aviários.

**1. Curto Prazo (0-3 meses) - Ações Operacionais:**
- Realizar auditoria energética detalhada nos aviários 170 e 785 (prioridade alta)
- Revisar protocolos de manejo de temperatura e ventilação em todas as instalações
- Implementar checklist de manutenção preventiva para equipamentos de climatização
- Treinar operadores em boas práticas de eficiência energética

**2. Médio Prazo (3-12 meses) - Melhorias Estruturais:**
- Avaliar e melhorar o isolamento térmico dos aviários com pior desempenho
- Substituir equipamentos de aquecimento e ventilação obsoletos por modelos de alta eficiência
- Instalar sistemas de automação para controle preciso de temperatura e umidade
- Implementar painéis solares para geração de energia complementar (análise de viabilidade)

**3. Longo Prazo (12+ meses) - Transformação Digital:**
- Desenvolver modelo preditivo de consumo de energia baseado em machine learning
- Integrar dados de IoT com sistemas de gestão para tomada de decisão em tempo real
- Estabelecer programa de benchmarking contínuo entre aviários
- Criar indicadores de desempenho energético (KPIs) vinculados a metas de sustentabilidade

**Governança:** Designar um responsável pela gestão energética e estabelecer revisões trimestrais de desempenho com metas claras de redução de consumo.

---

## Slide 11: Próximos Passos e Continuidade da Análise
**Título:** Expandir análise com dados climáticos e desenvolver modelo preditivo de consumo

**Conteúdo:**
Para aprofundar os insights e maximizar o valor da análise, recomenda-se a evolução do estudo em três direções complementares.

**1. Enriquecimento de dados:**
- Integrar dados climáticos (temperatura externa, umidade, velocidade do vento) para correlacionar consumo com condições meteorológicas
- Incluir informações sobre linhagem genética das aves e densidade de alojamento
- Coletar dados de custos de energia por aviário para análise de ROI de melhorias

**2. Análise avançada:**
- Desenvolver modelo de machine learning para prever consumo de energia com base em variáveis operacionais e climáticas
- Realizar análise de causa raiz (RCA) dos picos de consumo identificados nos aviários 170 e 785
- Segmentar lotes por desempenho energético e identificar características dos "lotes campeões"

**3. Escalabilidade:**
- Expandir a coleta de dados IoT para outros aviários da cooperativa
- Criar dashboard interativo para monitoramento em tempo real do consumo de todos os integrados
- Estabelecer programa de reconhecimento para produtores com melhores práticas de eficiência energética

**Impacto esperado:** Com a implementação dessas ações, estima-se uma redução de 15-25% no consumo de energia nos próximos 24 meses, contribuindo para a competitividade e sustentabilidade da cadeia produtiva da C.Vale.

---

## Slide 12: Conclusões
**Título:** Dados IoT revelam caminho claro para redução de custos e sustentabilidade na produção avícola

**Conteúdo:**
A análise exploratória dos dados de consumo de energia em 5 aviários integrados à C.Vale demonstra que a gestão energética baseada em dados oferece oportunidades tangíveis de redução de custos e melhoria da competitividade.

**Principais conclusões:**
1. **Padrão de consumo identificado:** O perfil em "U" com picos no início (aquecimento) e final (ventilação) do ciclo é consistente e previsível, permitindo planejamento estratégico.

2. **Disparidade de eficiência:** A diferença de 73% entre o aviário mais e menos eficiente comprova que há espaço significativo para melhoria através da adoção de melhores práticas.

3. **Driver principal:** O consumo de energia está primariamente ligado à climatização, não ao crescimento das aves, direcionando o foco para sistemas HVAC.

4. **Potencial de economia:** Estimativa de 19% de redução no consumo total (R$ 78.000 no período analisado) com ações de otimização.

5. **Aviário 1037 como benchmark:** O desempenho superior deste aviário deve ser estudado e replicado nos demais.

**Mensagem final:** A transformação digital na avicultura, através de IoT e análise de dados, não é apenas uma tendência tecnológica, mas uma necessidade competitiva. Os produtores que investirem em eficiência energética e gestão baseada em dados estarão melhor posicionados para enfrentar os desafios de custos crescentes e demandas por sustentabilidade.
