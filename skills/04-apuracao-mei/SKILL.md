---
name: apuracao-mei
description: Gerencia rotina mensal e anual do MEI: emissão de DAS-MEI, controle do limite de R$ 81 mil, DASN-SIMEI anual, hipóteses de desenquadramento e migração para ME no Simples Nacional.
allowed-tools: Read Grep Bash Edit Write
user-invocable: true
---

> ⚠️ **AVISO FISCAL — CONFIRA ANTES DE GERAR A GUIA.** Todo código de receita (DARF/DAS), alíquota, base de cálculo, valor e data de vencimento gerado por este agente é **rascunho de apoio** e pode variar por ano, regime tributário, município ou caso específico. **Confira sempre na fonte oficial vigente (Receita Federal / e-CAC / legislação estadual e municipal) antes de transmitir declaração ou pagar guia.** A conferência final é responsabilidade do contador responsável.

## Quando usar

Microempreendedor Individual (LC 123/2006, art. 18-A) com receita anual até R$ 81.000 (proporcional para início de atividade), atividade permitida pela Resolução CGSN 140/2018 (Anexo XI), sem sócios, com no máximo 1 empregado.

**NÃO use** para: ME/EPP no Simples Nacional (skill 01), MEI Caminhoneiro (regra própria, limite R$ 251.600).

## Inputs necessários

1. CNPJ do MEI + ocupação (CNAE)
2. Receita bruta mensal e acumulada do ano
3. Tem empregado? Se sim, salário (limite 1 empregado, salário-mínimo ou piso categoria)
4. Notas emitidas e canceladas no período
5. Emitiu nota para PJ? (PJ deve recolher INSS de 11% sobre o serviço — exceto algumas atividades)

## Passo a passo

### 1. DAS-MEI mensal (vencimento dia 20)
Valor fixo, atualizado anualmente:
- INSS: 5% do salário-mínimo (~R$ 70 em 2026)
- ICMS: R$ 1,00 (comércio/indústria)
- ISS: R$ 5,00 (serviços)
- Comércio + serviços: R$ 6,00

Total típico em 2026: ~R$ 76 (comércio), ~R$ 80 (serviços), ~R$ 81 (misto). Confirmar valor vigente no PGMEI.

Emitir no PGMEI (gov.br/empresas-e-negocios) ou app MEI.

### 2. Controle do limite de R$ 81.000
- **Excesso até 20%** (até R$ 97.200): permanece MEI no ano-calendário, mas em 1º/jan do ano seguinte é desenquadrado e migra para ME no Simples retroativo a 1º/jan; recolhe Simples sobre receita excedida.
- **Excesso acima de 20%**: desenquadramento **retroativo a 1º/jan do ano corrente**; precisa apurar Simples desde janeiro, com multa.
- Comunicar excesso no Portal do Simples Nacional em até 30 dias (Resolução CGSN 140, art. 115).

Para empresas em **início de atividade**, o limite é proporcional: R$ 6.750 × meses em atividade.

### 3. DASN-SIMEI (anual)
- Prazo: até 31/05 de cada ano-calendário, referente ao ano anterior.
- Informa: receita bruta total + receita com revenda/comércio/indústria/serviços + se contratou empregado.
- Multa por atraso: R$ 50,00 ou 2% ao mês sobre tributos declarados (mínimo).

### 4. Empregado MEI
- 1 empregado com salário-mínimo ou piso da categoria.
- INSS patronal 3% + FGTS 8% + IRRF (se aplicável) sobre o salário.
- eSocial doméstico/MEI simplificado.
- Folha mensal e GFD via DAE-MEI.

### 5. Nota fiscal
- Para PF: nota dispensada se MEI (mas recomendada).
- Para PJ: obrigatória nota fiscal eletrônica/serviço (NFS-e).
- A partir de 09/2023: NFS-e nacional padronizada para MEI prestador de serviço (Sistema NFS-e).

### 6. Retenção INSS de 11% (atenção)
- PJ tomadora deve reter 11% sobre o valor do serviço quando a atividade do MEI é construção civil, conservação, vigilância (cessão de mão de obra — art. 31 Lei 8.212/91).
- Exceção: atividades próprias de MEI em geral não cessão MO (verificar lista CGSN 140, Anexo XI).

## Templates

### Controle anual (planilha)

```
MEI: ____________________ CNPJ: __________ ANO: ____

Mês     Faturamento    Acumulado    DAS pago    NFS-e emitidas
Jan     R$________     R$________   ☐           ___
Fev     R$________     R$________   ☐           ___
...
Dez     R$________     R$________   ☐           ___
TOTAL   R$________

Limite anual: R$ 81.000
Margem usada: ____%
Status: [ ] OK  [ ] Excesso até 20%  [ ] Excesso > 20% (URGENTE)

DASN-SIMEI ano anterior: [ ] entregue em __/__/____
```

### Aviso ao cliente quando ultrapassa

> "Olá [Cliente], identificamos que sua receita acumulada em 2026 atingiu R$ ___, ultrapassando o limite do MEI (R$ 81.000). Você tem duas opções:
> 1. Solicitar desenquadramento voluntário ainda em 2026, virando ME no Simples (alíquota a partir de 6% sobre receita).
> 2. Aguardar desenquadramento automático em 01/01/2027 e recolher Simples sobre o que exceder.
> Recomendo a opção __ pelos motivos: __."

## Erros comuns

- Esquecer de pagar DAS de algum mês — a Receita só notifica no final do ano e MEI perde acesso a benefícios (auxílio-doença, salário-maternidade) com atrasos.
- Não entregar DASN-SIMEI no prazo.
- Receber pagamentos de PJ sem emitir NFS-e.
- Não monitorar acumulado mensal — dezembro chega com surpresa.
- Continuar como MEI mesmo desenquadrado (acumula dívida com Simples retroativo).
- Atividade não permitida (engenharia, advocacia, medicina — vedados ao MEI).

## Checklist mensal

- [ ] DAS gerado e pago até dia 20
- [ ] NFS-e emitidas para todas as receitas com PJ
- [ ] Acumulado anual atualizado em planilha
- [ ] Empregado: GFIP/eSocial e DAE pagos
- [ ] Comprovante DAS arquivado

## Checklist anual

- [ ] Receita acumulada conferida com extratos bancários e NFs
- [ ] DASN-SIMEI transmitida até 31/05
- [ ] Comprovante de DASN arquivado
- [ ] Cliente avisado se está perto do limite

## Referências

- LC 123/2006, art. 18-A a 18-C
- Resolução CGSN 140/2018 (Anexo XI: ocupações permitidas)
- Lei 13.043/2014 (parcelamento de débitos do MEI)
- Portaria CGSN 1/2018 (DASN-SIMEI)
