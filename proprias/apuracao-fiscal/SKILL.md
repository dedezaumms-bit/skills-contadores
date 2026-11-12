---
name: apuracao-fiscal
description: Apuração e conferência fiscal mensal, trimestral e anual das empresas do grupo (Lucro Real, Lucro Presumido, Simples Nacional) e das pessoas físicas (pró-labore, dividendos, aluguel, bolsa, ganho de capital, exterior). Usar quando o usuário pedir para apurar, conferir ou fechar impostos de uma empresa ou pessoa, calcular DAS, IRPJ/CSLL, PIS/COFINS, ISS, retenções, IRRF, carnê-leão ou IRPF, montar o calendário de obrigações do mês, ou cadastrar uma nova empresa ou pessoa. Não usar para folha, premiação e pagamentos Caju da MT Concreto (skill fechamento-mtconcreto).
---

# Apuração fiscal — empresas e pessoas físicas

Três camadas, cada uma em seu lugar. Nunca misture: regra não vai em ficha, dado de entidade não vai em referência.

| Camada | Onde | Conteúdo |
|---|---|---|
| Base comum | `references/` | Valores vigentes, prazos e regras por regime |
| Entidade | `entidades/<nome>.md` | Regime, atividades, municípios, fontes de dados, particularidades, pendências |
| Método | este arquivo | Como apurar e o que entregar |

## Antes de qualquer cálculo
1. Identifique a entidade e a competência. Se o pedido não disser, pergunte.
2. Leia a ficha em `entidades/`. Sem ficha: crie a partir de `_modelo-pj.md` ou `_modelo-pf.md`, perguntando ao usuário só o que não der para descobrir nos documentos.
3. Leia `references/tabelas-2026.md` e o arquivo do regime indicado na ficha (`simples-nacional.md`, `lucro-presumido.md`, `lucro-real.md`, `pessoa-fisica.md`). Em 2026, para Presumido e Real, leia também `reforma-tributaria.md`.
4. Se a competência for de outro ano que não o das tabelas, ou se um valor estiver marcado ⚠️ e for entrar em guia, confirme na fonte oficial (pesquise) e diga ao usuário o que confirmou. Se uma tabela estiver desatualizada, atualize o arquivo **e** `scripts/calculos.py`, e rode `scripts/test_calculos.py`.

## Método (igual para toda entidade)
1. **Inventário das fontes** listadas na ficha. Faltou documento essencial: avise e peça. Nunca estime nem invente valor.
2. **Base analítica**: uma linha por documento único (origem, tipo, status, chave, número, datas, CNPJ/CPF, município, valores, base, retenções). Deduplicar por chave de acesso; cancelados ficam marcados, não somem.
3. **Cruzamentos** entre as fontes da ficha (XML × relatório do sistema × lançamentos manuais × extrato). Cada divergência recebe gravidade (alta/média/baixa) e ação proposta.
4. **Apuração** pelas regras do regime. Use `scripts/calculos.py` para INSS, IRRF, DAS e Presumido em vez de calcular à mão. Aplique as particularidades da ficha (ex.: dedução de materiais no ISS, critério de créditos).
5. **Verificação independente**: um subagente recalcula tudo a partir dos documentos brutos, sem ver o resultado. Diferença acima de R$ 0,05 por tributo precisa ser explicada antes da entrega.
6. **Confronto com a contabilidade externa**, quando a ficha indicar e os arquivos dela existirem: débitos, créditos por categoria, retenções, saldo.
7. **Calendário**: liste o que vence para a entidade na competência, com data, usando `references/calendario-obrigacoes.md`.

## Entrega
- Resumo curto no chat: tributo a tributo (base, alíquota, valor, vencimento), divergências altas, pendências e o que depende de decisão do usuário.
- Planilha de apuração (skill xlsx, fórmulas reais) e, se a ficha pedir, dashboard, relatório PDF e pacote para a contabilidade.
- Atualize a seção "Pendências" da ficha: baixe o que foi resolvido, inclua o que surgiu.

## Regras fixas
- Todo valor apurado é rascunho para conferência: o contador responsável valida antes de transmitir declaração ou pagar guia. Diga isso uma vez na entrega, sem repetir a cada linha.
- Informe sempre de onde saiu cada número (documento, relatório, linha) e marque o que é estimativa.
- Quando a lei admitir mais de uma leitura (créditos de PIS/COFINS, ISS em outro município, dividendos no Simples), mostre as duas, calcule a diferença e deixe a decisão com o usuário.
- Visão do grupo: ao tratar pró-labore, dividendos ou JCP, considere o efeito na pessoa física (limite de R$ 50 mil por empresa, redutor, IRPFM) — ver `references/pessoa-fisica.md`.
- Dados pessoais (CPF, renda, patrimônio) ficam só na ficha da pessoa e nos entregáveis dela.

## Manutenção
- Janeiro: revisar `tabelas-2026.md` (renomear para o novo ano), `calendario-obrigacoes.md` e o script.
- Mudança informada pelo usuário (novo regime, novo município, nova fonte): alterar a ficha, não discutir.
