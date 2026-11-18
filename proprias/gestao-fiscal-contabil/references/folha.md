# Folha completa — mensal

Regras de valores: `tabelas-2026.md`; cálculo: `scripts/calculos.py inss | irrf`. Regras próprias da empresa (ciclo de apuração, premiação, benefícios, forma de pagamento) ficam na ficha.

## Entradas
Prévia ou folha do escritório, ponto, relatórios de produção que alimentam prêmios, benefícios pagos, admissões e desligamentos do ciclo, contratos e notas dos prestadores PJ.

## Sequência
1. **Extrair a folha** por pessoa (proventos, descontos, líquido) e conferir com o total do documento.
2. **Conferir** ponto × horas extras e faltas pagas; INSS e IRRF de cada pessoa recalculados pelo script; FGTS; base de cada rubrica.
3. **Premiação e variáveis** pelas regras escritas na ficha. Regra que não está na ficha não se aplica: perguntar e registrar.
4. **Encargos e provisões**: INSS patronal, RAT/FAP e terceiros conforme o regime, FGTS, provisão de férias + 1/3 e 13º com encargos.
5. **Prestadores PJ**: pagamento só confere com contrato e nota do mês; registrar retenções.
6. **Quadro de pagamentos**: pessoa, vínculo, documento, líquido, variáveis, total, e o suporte de cada linha.
7. **Arquivos de pagamento** no formato da ficha, com soma conferida contra o quadro.
8. **Auditor independente** (subagente) recalcula totais, encargos e arquivos.

## Vínculo de cada pessoa paga
Toda pessoa que recebe aparece com um destes vínculos: Empregado registrado · Sócio (pró-labore) · Estagiário/aprendiz · PJ com contrato e nota · Autônomo com RPA · **Sem vínculo formalizado**.

Para "sem vínculo formalizado" a skill:
- calcula o que é devido à pessoa pelo critério da ficha e inclui no quadro, identificado como tal — o trabalhador não deixa de receber por falha de registro;
- calcula e mostra, todo mês, os encargos que seriam devidos (INSS, FGTS, provisões) e o acumulado desde o início;
- lança o pagamento como custo de pessoal e o encargo estimado como provisão, sem misturar com outra despesa;
- mantém a pendência "regularizar vínculo" aberta em todos os fechamentos até decisão registrada.

A skill não gera arranjo para que o pagamento deixe de aparecer na contabilidade. O mesmo vale para PJ com valor fixo e sinais de subordinação (marcar risco de vínculo e estimar a exposição) e para prêmio habitual fora da folha (marcar e estimar encargos).

## Entregáveis
Planilha de fechamento de folha (quadro de pagamentos, conferências, premiação, encargos, provisões, pendências), arquivos de pagamento, resumo com totais e divergências.
