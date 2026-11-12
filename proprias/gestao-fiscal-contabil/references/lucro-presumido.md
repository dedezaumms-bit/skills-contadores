# Lucro Presumido — regras de apuração

Valores e prazos: `tabelas-2026.md` e `calendario-obrigacoes.md`. Cálculo: `scripts/calculos.py presumido`.
Limite: receita até R$ 78 milhões no ano anterior (Lei 9.718/98, art. 13).

## Trimestral — IRPJ e CSLL
Percentuais de presunção sobre a receita bruta (deduzidas vendas canceladas e descontos incondicionais):

| Atividade | IRPJ | CSLL |
|---|---|---|
| Revenda de combustíveis | 1,6% | 12% |
| Comércio, indústria, transporte de cargas, serviços hospitalares (sociedade empresária, normas Anvisa) | 8% | 12% |
| Transporte de passageiros | 16% | 12% |
| Serviços em geral, intermediação, locação, profissões regulamentadas | 32% | 32% |
| Construção por empreitada com fornecimento de todos os materiais | 8% | 12% |

Serviços em geral com receita anual até R$ 120 mil podem usar 16% no IRPJ.

- Somar à base, sem presunção: receitas financeiras, ganhos de capital, aluguéis fora do objeto, juros recebidos, demais receitas.
- **LC 224/2025**: acréscimo de 10% nos percentuais sobre a receita excedente (regra e ressalva em `tabelas-2026.md`).
- IRPJ 15% + adicional; CSLL 9%. Abater IRRF e CSLL retidos por tomadores e IRRF de aplicações financeiras.
- Regime de caixa ou competência: opção anual; manter o mesmo critério para PIS/COFINS.

## Mensal — PIS/COFINS cumulativo
0,65% + 3% sobre a receita bruta, excluídos ICMS destacado (Tema 69), IPI, ICMS-ST, vendas canceladas, descontos incondicionais; receitas financeiras não entram. Produtos monofásicos e alíquota zero: segregar. Abater retenções sofridas (CSRF, órgãos públicos).

## Demais
- ISS/ICMS conforme atividade; retenções como tomador (IRRF 1,5%, CSRF 4,65%, INSS 11%, ISS).
- Declarações: DCTFWeb com MIT, EFD-Contribuições, EFD-Reinf, eSocial, ECF; ECD se distribuir lucro acima da base presumida líquida de tributos.
- **Lucros**: isento o lucro presumido menos tributos; para distribuir mais, é preciso escrituração contábil (ECD). Retenção de 10% acima de R$ 50 mil/mês por sócio.
- 2026: destacar CBS/IBS nas notas (`reforma-tributaria.md`); para 2027, `regras-2027.md`.
