---
name: gestao-fiscal-contabil
description: Gestão fiscal, contábil e financeira das empresas do grupo (Lucro Real, Lucro Presumido, Simples Nacional) e das pessoas físicas - apura e confere impostos do mês, confronta com a contabilidade externa, monta balanço e DRE paralelos por trimestre com relatório de inconsistências e de alterações, fecha a folha, concilia bancos e fluxo de caixa, controla o IR das pessoas físicas, simula regime e reforma tributária de 2027, e mantém registro de decisões e fechamentos congelados. Usar quando o usuário pedir fechamento fiscal, apuração ou conferência de impostos, confronto com a contabilidade, balanço, balancete, DRE, conciliação, fluxo de caixa, folha, carnê-leão, dividendos, IRPF, calendário de obrigações, simulação para 2027, ou cadastro de empresa ou pessoa. Para examinar documentos como perito e achar o que está sem lastro, usar a skill pericia-documental.
---

# Gestão fiscal e contábil

## Como a skill é organizada
| Camada | Onde | Regra |
|---|---|---|
| Regras e valores | `references/` | Iguais para todos. Valores só em `tabelas-2026.md`; 2027 em `regras-2027.md` |
| Entidade | `00-CADASTRO/ficha.md` na pasta da entidade (fora da skill) | Tudo o que é próprio da empresa ou pessoa. Modelos em `modelos/` |
| Método | este arquivo e os `references/` de cada frente | Como fazer e o que entregar |

Dado de entidade nunca é gravado dentro da skill nem em repositório. Nada de uma entidade é usado em outra, exceto na visão consolidada do grupo, que leva só totais.

## Sempre, antes de começar
1. Identificar **entidade, competência e frente** pedida. Se faltar, perguntar.
2. Ler a ficha da entidade. Não existe: criar com o usuário a partir de `modelos/ficha-pj.md` ou `modelos/ficha-pf.md`, extraindo do contrato social e dos documentos tudo o que der, e perguntando só o resto. Estrutura de pastas: `references/pastas.md`.
3. Ler `references/tabelas-2026.md` e o arquivo do regime da ficha. Valor marcado ⚠️ que for entrar em guia: confirmar na fonte oficial (pesquisar) e dizer o que confirmou. Competência de 2027 em diante: ler `references/regras-2027.md` e avisar o que ainda depende de ato não publicado.
4. Ao atualizar um valor: alterar a tabela **e** `scripts/calculos.py`, e rodar `scripts/test_calculos.py`.

## Frentes
| Frente | Frequência | Ler | Situação |
|---|---|---|---|
| Fiscal das empresas | Mensal | `fiscal-mensal.md` + regime (`simples-nacional.md`, `lucro-presumido.md`, `lucro-real.md`) + `reforma-tributaria.md` + `calendario-obrigacoes.md` | Primeira a validar |
| Financeiro | Mensal | `financeiro.md` | A validar |
| Folha | Mensal | `folha.md` | A validar |
| Balanço e DRE paralelos, confronto com a contabilidade | Trimestral | `contabil.md`, `plano-de-contas.md` | A validar |
| Pessoas físicas | Mensal e anual | `pessoa-fisica.md` | A validar |
| Planejamento e 2027 | Sob demanda | `regras-2027.md` | Aguardando alíquota da CBS |
| Visão do grupo | Mensal | abaixo | A validar |

"A validar" significa que o método está escrito mas ainda não foi rodado com dados reais. Na primeira execução de cada frente para uma entidade, dizer isso ao usuário e conferir o resultado com ele antes de congelar.

## Regras de trabalho
- **Fonte primeiro**: faltou documento, avisar e seguir com o que há, marcando o resultado como parcial. Nunca estimar nem inventar valor.
- **Dúvida**: adotar a premissa mais provável, marcar o item e listar tudo em Pendências no final, com valor. Não parar para perguntar, salvo se a dúvida impedir a apuração inteira.
- **Rastro**: todo número de entregável aponta para o documento de origem.
- **Verificação independente** em todo fechamento: subagente recalcula do zero.
- **Duas leituras**: quando a regra admitir mais de uma, calcular ambas e deixar a escolha para o usuário, registrando-a em `DECISOES`.
- **Sem lastro**: operação sem documento ou sem evidência não é tratada como operação comum; segue `fiscal-mensal.md` e `contabil.md` e aparece em Pendências.
- **Governança** (`governanca.md`): registrar decisões na data, congelar cada fechamento com `scripts/manifesto.py`, extrato mensal de sócios e partes relacionadas.
- **Rascunho**: toda apuração é para conferência; quem transmite declaração e assina demonstração é o contador responsável. Dizer uma vez por entrega.

## Entregas e leitores
Cada fechamento gera planilha (skill xlsx, fórmulas reais), painel HTML autocontido e relatório PDF (skill pdf). Ajustar o texto ao leitor:
- **Administrador**: completo, técnico, com pendências e decisões a tomar.
- **Sócios e gestores**: duas páginas — resultado, caixa, tributos, riscos, decisões do período.
- **Contabilidade externa**: lista de ajustes com conta, documento, valor e lançamento proposto.
- **Bancos e terceiros**: demonstrações em formato formal, só após validação do contador responsável.
- **Exame por perito**: nenhum relatório especial — o que serve a um perito é o rastro, o registro de decisões e os fechamentos congelados já descritos.

## Visão do grupo (`_GRUPO`)
Depois dos fechamentos do mês: quadro por entidade (receita, resultado, tributos apurados e pagos, caixa, pendências abertas) e, para as pessoas físicas, rendimentos por fonte, IR do mês e acumulado para o IRPF mínimo. Mostrar também as transações entre entidades do grupo e entre empresas e sócios. Só totais; nenhum documento é copiado.

## Manutenção
- Dezembro e janeiro: revisar `regras-2027.md`, criar a tabela do novo ano, atualizar script e testes.
- Mudança informada pelo usuário sobre uma entidade: alterar a ficha.
- Ao terminar a primeira execução real de uma frente, trocar "A validar" por "Validada em MM/AAAA com <entidade>" na tabela acima.
