---
name: pericia-documental
description: Diagnóstico interno que examina os documentos de uma empresa como um perito contábil examinaria hoje, do jeito que estão - aponta movimentos sem documento fiscal, notas sem evidência de serviço, retiradas e despesas sem lastro, caixa que não fecha e saldos contábeis sem composição, monta a lista do que procurar e dimensiona a exposição do que não existe. Usar quando o usuário pedir perícia, auditoria como perito, teste de lastro, o que está sem documento, o que um perito veria, ou revisão de balanços e DRE de anos anteriores. Não apura impostos nem faz fechamento (isso é da skill de gestão).
---

# Perícia documental — diagnóstico interno

Objetivo: mostrar ao administrador, antes de qualquer terceiro, **o que um perito encontraria** nos documentos como estão, para que ele (1) localize o que existe e não está arquivado e (2) saiba o tamanho do problema onde não existe nada.

Esta skill **não apura nem corrige**. Ela recebe o que a skill de gestão gerou e os documentos de origem, e tenta derrubar. Achado só se resolve com documento.

## Regras que não se negociam
1. **Somente leitura nas origens.** Nunca alterar, renomear, mover ou apagar documento de origem.
2. **Nunca produzir documento com data passada** nem sugerir isso. Documento que existe é localizado; o que não existe é dimensionado e segue para regularização formal (retificação, ajuste de exercícios anteriores, recolhimento), decidida com advogado e contabilidade. Declaração feita hoje leva a data de hoje.
3. **Descrever, não acusar.** Redigir cada achado como um laudo: fato, documento examinado, o que falta. Sem adjetivo e sem presumir intenção.
4. **"Sem documento" ≠ "não existe".** Significa "não encontrado no que foi fornecido". Só o usuário muda o status para Inexistente.
5. **Saída em pasta própria**, indicada pelo usuário, fora de pastas compartilhadas. Antes de gravar, confirmar o local. Lembrar uma vez que o material é sensível e que a guarda deve ser combinada com o advogado.
6. Na dúvida, seguir com a premissa mais provável, marcar o item e listar no final.

## Etapas
1. **Escopo**: empresa, período, contas bancárias, lista de partes relacionadas (sócios, administrador, familiares, empresas ligadas). Vem da ficha da entidade na skill de gestão; se faltar, perguntar.
2. **Inventário** (`references/inventario.md`): o que existe por mês e por tipo. Buraco de documento inteiro (extrato de um mês, livro, balancete) é o primeiro achado.
3. **Normalização**: montar `movimentos.csv`, `documentos.csv` e `partes.csv` no formato descrito em `scripts/lastro.py`. Todo extrato de toda conta entra; transferências entre contas próprias são casadas entre si e saem da análise.
4. **Cruzamento**: rodar `scripts/lastro.py`. Depois, revisar à mão os `CONFERIR` e `VALOR_DIVERGENTE`.
5. **Testes de perito** (`references/testes.md`): aplicar todos os blocos que tiverem dados; registrar os que não puderam ser aplicados e por quê.
6. **Classificação de cada achado** (`references/classificacao.md`): situação do lastro, natureza, gravidade, beneficiário.
7. **Lista de busca**: para cada item "A localizar", qual documento resolve, onde provavelmente está, quem pede, prazo.
8. **Exposição** (`references/exposicao.md`): para os itens Inexistente e Parcial, faixa de valor com as premissas escritas.
9. **Verificação**: um subagente refaz os totais a partir dos CSVs e confere 20 achados por amostragem contra o documento.

## Entregas
- **Planilha "Matriz de lastro"** (skill xlsx): abas Resumo · Inventário · Movimentos · Achados · Lista de busca · Exposição · Partes relacionadas · Testes não aplicados. Cada achado tem ID fixo (`ANO-NNNN`) para acompanhar entre rodadas.
- **Painel HTML** autocontido: % do valor movimentado com lastro por mês, achados por natureza e gravidade, evolução da lista de busca.
- **Resumo no chat**, nesta ordem: cobertura (quanto do período e do valor foi examinado), os dez maiores achados, total a localizar × inexistente, exposição em faixa, próximos documentos a buscar.

## Rodadas seguintes
Ao receber novos documentos: reprocessar, manter os IDs, marcar o que foi resolvido com a referência do documento e a data em que foi apresentado. Nunca apagar achado resolvido — o histórico de saneamento é parte do valor.

## Anos anteriores
Aplicar o mesmo método ano a ano, do mais antigo ao mais recente, e acrescentar o bloco de demonstrações de `references/testes.md` (saldos de abertura × fechamento anterior, composição de cada conta do balanço, DRE × notas × declarações).
