# Plano de contas base

Estrutura mínima, comum a todas as empresas. Cada ficha pode abrir subcontas, nunca mudar os grupos.

```
1 ATIVO
 1.1 Circulante
  1.1.1 Caixa e bancos (uma conta por conta bancária)
  1.1.2 Aplicações financeiras
  1.1.3 Clientes
  1.1.4 Tributos a recuperar (por tributo; retenções sofridas separadas)
  1.1.5 Estoques
  1.1.6 Adiantamentos (fornecedores; empregados)
  1.1.7 Despesas antecipadas
  1.1.8 Créditos com sócios e partes relacionadas (uma conta por pessoa)
  1.1.9 Valores a regularizar
 1.2 Não circulante
  1.2.1 Realizável a longo prazo
  1.2.2 Investimentos
  1.2.3 Imobilizado (custo por classe)
  1.2.4 (-) Depreciação acumulada
  1.2.5 Intangível
2 PASSIVO
 2.1 Circulante
  2.1.1 Fornecedores
  2.1.2 Obrigações trabalhistas (salários, pró-labore, provisões de férias e 13º)
  2.1.3 Encargos sociais (INSS, FGTS)
  2.1.4 Tributos a recolher (por tributo; retenções a recolher separadas)
  2.1.5 Empréstimos e financiamentos
  2.1.6 Adiantamentos de clientes
  2.1.7 Lucros a pagar
  2.1.8 Débitos com sócios e partes relacionadas (uma conta por pessoa)
  2.1.9 Valores a regularizar
 2.2 Não circulante
  2.2.1 Empréstimos e financiamentos
  2.2.2 Parcelamentos tributários
  2.2.3 Provisões para contingências (trabalhistas, tributárias, cíveis)
 2.3 Patrimônio líquido
  2.3.1 Capital social
  2.3.2 Reservas
  2.3.3 Lucros ou prejuízos acumulados
  2.3.4 Ajustes de exercícios anteriores
  2.3.5 Resultado do exercício
3 RECEITAS
 3.1 Receita bruta (por atividade e, se útil, por município)
 3.2 (-) Deduções (cancelamentos, descontos, tributos sobre a receita)
 3.3 Receitas financeiras
 3.4 Outras receitas
4 CUSTOS
 4.1 Materiais e insumos
 4.2 Pessoal de produção
 4.3 Combustíveis, fretes, manutenção de equipamentos
 4.4 Depreciação de produção
 4.5 Serviços de terceiros de produção
5 DESPESAS
 5.1 Pessoal administrativo e pró-labore
 5.2 Administrativas (aluguel, energia, sistemas, honorários)
 5.3 Comerciais
 5.4 Tributárias (não incidentes sobre receita ou lucro)
 5.5 Financeiras
 5.6 Outras despesas
 5.7 IRPJ e CSLL
```

Regras de uso:
- Sócio nunca em conta genérica: toda movimentação com sócio ou parte relacionada passa por 1.1.8 ou 2.1.8 antes de ser classificada (pró-labore, lucro, reembolso com notas, mútuo com contrato).
- 1.1.9 e 2.1.9 devem tender a zero; saldo crescente é alerta no painel.
- Conta Caixa (dinheiro físico) só existe se houver controle de caixa com comprovantes.
