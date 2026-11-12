# Balanço e DRE paralelos — trimestral

Objetivo: demonstrações próprias, montadas a partir dos documentos, para comparar com as da contabilidade e dizer onde e por que diferem.

## Construção
1. **Plano de contas**: usar `plano-de-contas.md` como base e manter, na ficha da entidade, o **de-para** com o plano da contabilidade (conta dela → conta nossa). Sem de-para não há confronto.
2. **Saldos de abertura**: balanço de fechamento do período anterior. No primeiro uso, partir do balanço da contabilidade em 31/12 e registrar que a abertura **não foi auditada** até a perícia cobrir aquele ano.
3. **Lançamentos**, sempre com documento e partida dobrada, por origem:
   - Extratos: todo movimento de toda conta vira lançamento (banco × contrapartida).
   - Notas emitidas e recebidas: receita, custos, despesas, tributos, clientes e fornecedores por competência.
   - Folha: salários, encargos, provisões de férias e 13º.
   - Apuração fiscal do mês: tributos a recolher e a recuperar.
   - Imobilizado: aquisições, depreciação (taxa contábil na ficha), baixas.
   - Financiamentos: principal, juros por competência, curto × longo prazo.
   - Sócios: pró-labore, lucros, mútuos, reembolsos — cada um em conta própria por sócio.
4. **Movimento sem documento ou sem classificação segura**: vai para a conta `1.1.9 Valores a regularizar` (saídas) ou `2.1.9 Valores a regularizar` (entradas), com histórico do que se sabe. Nunca diluir em despesa genérica. O saldo dessas contas é indicador do fechamento.
5. **Conciliações obrigatórias** antes de fechar: bancos (saldo contábil = extrato), clientes e fornecedores (composição por título), tributos (saldo = guias a vencer), folha (saldo = líquidos e encargos a pagar), sócios (extrato por sócio).
6. **Demonstrações**: balancete, balanço patrimonial, DRE (mês, trimestre, acumulado), fluxo de caixa pelo método direto, mutações do patrimônio líquido.

## Confronto com a contabilidade
Conta a conta pelo de-para, com materialidade da ficha (padrão: R$ 500 ou 1% do saldo, o maior). Para cada diferença: valor, causa (documento que ela não tem, classificação diferente, competência, erro de soma, lançamento sem documento do lado dela), e quem está certo com base em qual documento.

## Dois relatórios de saída
- **Relatório de inconsistências** — o que está errado ou sem suporte nas demonstrações da contabilidade. Por item: conta, período, valor, documento que comprova, correção proposta (lançamento a débito e a crédito).
- **Relatório de alterações solicitadas** — o que não está errado, mas a administração quer apresentar de outra forma (abrir uma conta em subcontas, reclassificar entre grupos, mudar critério dentro do que a norma permite). Por item: situação atual, alteração pedida, fundamento (norma contábil), efeito nas demonstrações, se exige reapresentar períodos anteriores.

Toda alteração de critério vale daqui para frente ou, se retroativa, é tratada como mudança de política ou correção de erro (ajuste de exercícios anteriores com nota explicativa). A skill não propõe alteração cujo único efeito seja deixar de evidenciar uma operação.

## Erros de anos anteriores
Achado da perícia que pede correção contábil entra aqui como proposta de **ajuste de exercícios anteriores**: lançamento, efeito no patrimônio líquido, texto sugerido de nota explicativa, declarações a retificar. A decisão é registrada em `DECISOES`.

## Entregáveis do trimestre
Planilha com balancete, balanço, DRE, fluxo de caixa, conciliações e confronto; os dois relatórios em PDF; painel; versão formal das demonstrações (para bancos e terceiros) **somente** depois que o usuário confirmar que os números foram validados pelo contador responsável, que é quem assina.
