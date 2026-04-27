---
name: dirf
description: Gera e transmite a DIRF anual com rendimentos pagos a PF e PJ e respectivos IRRF/CSRF retidos. Atenção: a partir de 2024 a obrigação migrou para a EFD-Reinf (R-4000), mas DIRF retroativa ainda é válida.
allowed-tools: Read Grep Bash Edit Write
user-invocable: true
---

## Quando usar

**Atenção:** a DIRF foi **extinta** para fatos geradores de 2024 em diante (substituída por R-4010/R-4020 da EFD-Reinf). Use esta skill para:
- DIRF retificadora ou original de anos anteriores a 2024 (até 2023).
- Verificação histórica e cruzamento com IRPF do beneficiário.

## Inputs necessários

1. Folha de pagamento de cada mês (IRRF retido por colaborador, dependentes, INSS, plano de saúde, previdência privada)
2. NFs de serviços com IRRF/CSRF/INSS retidos (skill 13)
3. Pagamentos de aluguel a PF
4. Pagamentos a autônomos (RPA)
5. Pagamentos ao exterior (royalties, juros, dividendos)
6. Comprovantes de rendimentos enviados aos beneficiários

## Estrutura

A DIRF organiza:
- **Beneficiários PF**: CPF, nome, dependentes, rendimentos por código de natureza, IRRF, ISS retido por município, deduções (INSS, dependentes, pensão alimentícia, plano saúde).
- **Beneficiários PJ**: CNPJ, razão, rendimentos por código, IRRF, CSRF, INSS, IRPJ residente.

## Códigos de natureza mais comuns

| Código | Natureza |
|---|---|
| 0561 | Trabalho assalariado / pró-labore |
| 0588 | Serviços profissionais a PF (autônomo) |
| 1708 | Serviços profissionais a PJ |
| 3208 | Aluguel pago a PF |
| 3280 | Aluguel pago ao exterior |
| 5952 | CSRF (PIS+COFINS+CSLL) |
| 8045 | Juros e descontos (RFB) |
| 0473 | Juros sobre capital próprio |
| 5706 | IRRF na fonte sobre rendimentos do exterior |

## Passo a passo (DIRF anos ≤ 2023)

### 1. Levantar todos os pagamentos com retenção do ano

### 2. Consolidar por beneficiário e código
- PF/PJ × natureza × mês × valor/IRRF/dedução

### 3. Plano de saúde (PGD DIRF — Quadro 12)
- Necessário informar dependentes do plano com valor anual reembolsado

### 4. Importar no PGD DIRF (Receita Federal)
- Pode digitar ou importar TXT do sistema da empresa

### 5. Validar (PVA gerou um relatório)
- Erros mais comuns: CPF inválido, soma mensal ≠ anual, beneficiário sem ao menos 1 mês de rendimento.

### 6. Assinar e transmitir até **28/02 ou 29/02** do ano subsequente.

### 7. Comprovante de Rendimentos
- Entregar até 28/02 a cada beneficiário (PF/PJ).

## DIRF migrada para Reinf (2024+)

Para fatos geradores de 2024 em diante, use:
- **R-4010** — pagamentos a PF (substitui DIRF PF)
- **R-4020** — pagamentos a PJ (substitui DIRF PJ)
- **R-4080** — retenções no recebimento (PJ que sofreu retenção)
- **R-4099** — fechamento

## Erros comuns

- Não bater soma de IRRF retido com DCTF/DCTFWeb mensal.
- Esquecer informe de dependentes do plano de saúde — beneficiário não consegue deduzir no IRPF.
- Comprovante de rendimentos sem detalhar dependentes informados.
- DIRF entregue em atraso → multa 2% a.m. (mín R$ 500 PJ ativa).
- Aluguel pago a PF: esquecer DIRF (ou em 2024+: R-4010).
- Sócio com pró-labore sem dependentes declarados.

## Checklist

- [ ] Todos os meses com IRRF retido conferidos
- [ ] DIRF (≤ 2023) ou R-4010/R-4020 (≥ 2024) com 100% dos beneficiários
- [ ] Comprovante de rendimentos entregue até 28/02
- [ ] Cruzamento com DCTF/DCTFWeb sem divergência
- [ ] Plano de saúde com dependentes informados
- [ ] Beneficiário PJ Simples imune/isenta com declaração arquivada

## Referências

- IN RFB 2.060/2021 (DIRF — última versão regulamentar)
- IN RFB 2.043/2021 (EFD-Reinf — substituição)
- Decreto 9.580/2018 (RIR/2018)
- Manual DIRF e PGD (anos ≤ 2023)
