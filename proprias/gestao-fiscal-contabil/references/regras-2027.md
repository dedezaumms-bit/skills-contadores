# Regras para 2027 — preparação

Situação em 12/11/2026. Parte das regras ainda depende de ato a publicar; cada item diz o que já é lei e o que falta. **Revisar este arquivo em dezembro/2026 e de novo em janeiro/2027**, e então criar `tabelas-2027.md`.

## O que já está definido em lei (EC 132/2023, LC 214/2025)
| Tema | 2027 |
|---|---|
| PIS e COFINS | **Extintos**. A CBS passa a ser cobrada integralmente |
| CBS | Não cumulativa plena para todo o regime regular (Real **e** Presumido): crédito sobre praticamente todas as aquisições com CBS destacada e paga |
| IBS | Continua em 0,1% (estadual + municipal), agora efetivamente recolhido; a CBS é reduzida em 0,1 ponto em 2027 e 2028 |
| IPI | Alíquota zero, exceto produtos com similar fabricado na Zona Franca de Manaus |
| Imposto Seletivo | Entra em vigor (bens e serviços prejudiciais à saúde ou ao meio ambiente); alíquotas por lei ordinária |
| ICMS e ISS | **Continuam integrais** em 2027 e 2028. Redução gradual de 2029 a 2032; extinção em 2033 |
| IRPJ e CSLL | Sem mudança pela reforma do consumo. Seguem as regras de 2026 (LC 224/2025, Lei 15.270/2025) |
| Split payment | Recolhimento do IBS/CBS no momento do pagamento; implantação por etapas definidas em ato conjunto da Receita e do Comitê Gestor |

## O que ainda falta definir
- **Alíquota da CBS**: o TCU aprovou em 28/10/2026 o cálculo de **11,3%** (11,3468%). O Senado fixa a alíquota de referência até 15/12/2026. Estimativas anteriores iam de 8,8% a 10,85%. Até a resolução do Senado, simular com 11,3% e mostrar sensibilidade (9,5% e 11,3%).
- Cronograma do split payment e regulamentos operacionais (apuração assistida, prazos de recolhimento, obrigações acessórias que substituem a EFD-Contribuições).
- Salário mínimo, tabela do INSS e demais valores de 2027 (saem entre dezembro e janeiro).
- Regimes específicos e reduções de alíquota aplicáveis a cada atividade (construção civil, saúde, educação, profissões regulamentadas, etc.): verificar caso a caso na LC 214 ao cadastrar a entidade.

## Efeito por regime — o que simular para cada empresa
### Lucro Real
- Sai PIS/COFINS 9,25% com crédito restrito (insumos); entra CBS com crédito amplo. Ganha quem tem muita compra tributada; perde quem tem custo concentrado em folha.
- Revisar preços e contratos de longo prazo (cláusula de reequilíbrio).
- Créditos acumulados de PIS/COFINS em 31/12/2026: levantar o saldo e a forma de aproveitamento.

### Lucro Presumido
- Sai PIS/COFINS cumulativo de 3,65% sem crédito; entra CBS cheia com crédito. Para prestador de serviço com pouca compra, a carga sobre o consumo sobe de forma relevante — é a simulação mais importante do grupo.
- O cliente pessoa jurídica passa a tomar crédito integral da CBS destacada, o que muda a negociação de preço.
- Refazer a comparação Presumido × Real para 2027 somando: IRPJ/CSLL (com o acréscimo de 10% da LC 224), CBS e a folha.

### Simples Nacional
- Escolha semestral: recolher IBS/CBS **dentro do DAS** (mais simples; o cliente PJ toma crédito só do valor efetivamente pago, e a empresa não toma crédito) ou **pelo regime regular, fora do DAS** (o cliente toma crédito cheio e a empresa também, mas com apuração própria).
- A escolha para janeiro–junho/2027 foi feita em setembro/2026 e pode ser cancelada até 30/11/2026. Para cada empresa do Simples: confirmar qual opção foi registrada e se convém manter.
- Regra prática: quem vende para consumidor final ou para outros optantes tende a ficar por dentro; quem vende para empresas do regime regular deve simular por fora.
- ⚠️ Uma fonte afirma que acima de R$ 3,6 milhões de receita o IBS vai obrigatoriamente pelo regime regular. Não confirmado: conferir na Resolução CGSN 186/2026.

### Pessoas físicas
- Sem mudança pela reforma do consumo, salvo locação de imóveis e atividades habituais que possam tornar a pessoa contribuinte de IBS/CBS (LC 214 traz limites de receita e de número de imóveis) — verificar para quem tem vários imóveis alugados.
- 2027 é o primeiro ano de declaração com redutor anual e IRPF mínimo (ano-calendário 2026).

## Preparação a fazer ainda em 2026 (por entidade)
1. Cadastro de produtos e serviços com a classificação tributária de IBS/CBS (cClassTrib) e o código da nomenclatura de serviços (NBS), validado com a contabilidade.
2. Fornecedores: quem é Simples (crédito menor), quem é regime regular; revisar os maiores contratos.
3. Preços: recalcular com CBS por fora do preço e crédito nas compras.
4. Caixa: efeito do split payment (o tributo deixa de transitar pelo caixa da empresa).
5. Sistemas: emissão de nota e ERP aptos ao leiaute de 2027.
6. Decisão de regime para 2027 documentada no registro de decisões, com a simulação anexada.
