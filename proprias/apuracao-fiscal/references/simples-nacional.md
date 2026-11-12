# Simples Nacional — regras de apuração

Valores e prazos: `tabelas-2026.md` e `calendario-obrigacoes.md`. Cálculo: `scripts/calculos.py simples`.

## Apuração mensal (DAS)
1. **RBT12**: receita bruta dos 12 meses anteriores ao mês apurado (não inclui o próprio mês). Empresa com menos de 13 meses: média mensal × 12.
2. **Limites**: RBT12 até R$ 4,8 milhões. Acima de R$ 3,6 milhões (sublimite), ICMS e ISS saem do DAS e são apurados por fora.
3. **Anexo** por tipo de receita: I comércio · II indústria · III serviços (e os do V com fator R ≥ 28%) · IV construção, vigilância, limpeza, advocacia (CPP por fora) · V serviços intelectuais com fator R < 28%.
4. **Fator R** = folha dos 12 meses (salários, pró-labore, FGTS, CPP) ÷ RBT12. Calcular todo mês para atividades sujeitas.
5. **Alíquota efetiva** = (RBT12 × alíquota nominal − parcela a deduzir) ÷ RBT12, aplicada à receita do mês, por anexo.
6. **Segregação no PGDAS-D**: receita com ICMS-ST, monofásico de PIS/COFINS, exportação, ISS retido ou devido a outro município. Classificar errado gera pagamento em dobro — é o erro mais caro do Simples.
7. Conferir o DAS do PGDAS-D contra o cálculo do script; diferença indica segregação ou anexo errado.

## Outras obrigações
- Folha: eSocial, FGTS Digital; DCTFWeb para o INSS dos segurados (e CPP no Anexo IV).
- Retenções: Simples não sofre retenção de IRRF/CSRF sobre serviços (declaração ao tomador); sofre INSS (cessão de mão de obra) e ISS conforme o município.
- DEFIS anual. Estadual: DeSTDA/DIFAL conforme UF.

## Pontos de atenção 2026
- **Distribuição de lucros**: isenta dentro do lucro contábil apurado (com escrituração) ou do limite presumido; acima de R$ 50 mil/mês por sócio, retenção de 10% (ver tabelas — aplicação ao Simples contestada, tratar como vigente).
- Sem CBS/IBS em 2026.
- Monitorar todo mês: RBT12 perto de R$ 3,6 mi e R$ 4,8 mi; fator R perto de 28%; excesso de receita acima de 20% do limite (exclusão retroativa).
