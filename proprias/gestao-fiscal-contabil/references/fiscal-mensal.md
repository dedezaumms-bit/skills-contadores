# Fechamento fiscal mensal — método

Primeira frente da skill. Vale para qualquer empresa; o que muda entre elas está na ficha.

## Sequência
1. **Inventário das fontes** do mês (`01-ENTRADA`): conferir contra a lista da ficha. Faltou fonte essencial: avisar, seguir com o que há e marcar a apuração como parcial.
   - Conferir o **conteúdo**, não só a existência: planilha só com cabeçalho, PDF sem texto, ZIP de outro período e pasta vazia contam como "falta".
   - Antes de declarar uma planilha vazia, **reler o arquivo inteiro**: exportações de alguns portais trazem o metadado de dimensão errado e a leitura rápida devolve só o cabeçalho (ler com pandas, ou openpyxl sem `read_only`, e contar as linhas).
   - Conferir a quem pertence cada documento recebido de terceiros (CNPJ e razão social no próprio arquivo): guia ou livro de outra empresa enviado por engano é pendência a devolver.
   - Conferir a **cobertura de datas** de cada fonte (primeiro e último dia do mês) e a qual CNPJ pertence.
   - Material baixado por trimestre ou em outra estrutura de pastas é aceito como está: separar por competência na base de documentos, sem mover arquivos.
   - **Só PDF, sem XML**: a apuração do tributo que depende daquele documento fica bloqueada para o mês; não digitar valores de PDF como se fossem a base. Exceção: documento que não existe em XML (fatura, recibo, nota de outro município sem padrão nacional) entra por leitura do PDF, marcado como tal.
   - Notas emitidas faltando = **sem base de receita**: o mês não fecha. Dizer isso na primeira linha da resposta.
2. **Base de documentos**: uma linha por documento único. Campos mínimos: origem, tipo (NFS-e, NF-e, CT-e, fatura, recibo), sentido (emitida/recebida), situação (ativa/cancelada/substituída), chave ou número, emissão, competência, CNPJ/CPF da contraparte, município, valor, base, alíquotas, cada retenção, IBS/CBS destacados, arquivo de origem.
   - Deduplicar por chave de acesso; sem chave, por CNPJ + número + valor.
   - Cancelada não some: fica marcada e fora das somas.
   - Manifestação do destinatário: contar as NF-e recebidas sem ciência/confirmação por mês. Salto no volume é pendência, e nota desconhecida contra o CNPJ deve ser recusada no portal dentro do prazo.
   - NF-e em que a empresa aparece só como **transportadora** não é compra nem receita: registrar à parte e conferir se é transporte de carga própria (sem CT-e) ou serviço de frete a terceiros (exige CT-e e ICMS).
   - Sequência numérica das notas emitidas: todo salto precisa de explicação (inutilização, cancelamento, salto do emissor) confirmada no portal ou no livro da prefeitura.
   - **Faturamento do sistema de gestão × notas emitidas**, por mês e por cliente. Diferença relevante não é arredondada nem atribuída a "prazo" sem prova: abrir cliente a cliente e classificar (nota sem produção registrada, produção sem nota, serviço fora do sistema, faturamento antecipado ou atrasado).
3. **Cruzamentos** entre fontes (XML × relatório do portal × sistema de gestão × lançamentos manuais × extrato quando disponível). Divergência = linha com gravidade e ação.
4. **Apuração**, na ordem: tributos sobre a receita (DAS, ou PIS/COFINS e ISS/ICMS) → retenções sofridas → retenções a recolher como tomadora → IRPJ/CSLL (mensal por estimativa, trimestral, ou só acompanhamento da base) → conferência do destaque de IBS/CBS.
   - Usar `scripts/calculos.py`. Aplicar as particularidades da ficha.
   - Onde houver mais de uma leitura da regra, calcular as duas e mostrar a diferença.
5. **Verificação independente**: subagente recalcula do zero a partir dos documentos, sem ver o resultado. Diferença acima de R$ 0,05 por tributo tem de ser explicada.
6. **Confronto com a contabilidade** quando os arquivos dela chegarem: tributo a tributo — base, débito, créditos por categoria, retenções, saldo anterior, valor a recolher. Cada diferença com causa provável e quem ajusta (empresa ou contabilidade).
7. **Calendário do mês**: o que vence, quando, valor apurado, situação (a pagar/pago/divergente da guia).
8. **Pendências**: itens marcados por dúvida, documentos faltantes, perguntas ao usuário. Atualizar a ficha.
9. **Congelar**: copiar entregáveis para `03-FECHAMENTO` e rodar `scripts/manifesto.py gerar`.

## Entregáveis do mês
- `Apuracao-Fiscal-MM-AAAA.xlsx` (skill xlsx, fórmulas reais): Resumo · Documentos · Receita por município/atividade · Tributos · Retenções · Créditos · Confronto · Divergências · Calendário · Pendências.
- Painel HTML autocontido.
- Relatório PDF de duas páginas para sócios e, em anexo, a lista de ajustes para a contabilidade.
- Pacote para escrituração (ZIP com os documentos deduplicados, organizado por tipo), se a ficha pedir.

## Operações sem lastro encontradas na apuração
Não classificar como operação comum. Marcar o documento (`sem evidência de prestação`, `entrada sem nota`, `saída sem documento`), manter fora das conclusões de resultado até decisão, e listar em Pendências com valor. O tratamento fiscal e contábil é decidido pelo usuário com advogado e contabilidade e registrado em `DECISOES`.
