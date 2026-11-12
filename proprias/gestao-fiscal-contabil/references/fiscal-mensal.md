# Fechamento fiscal mensal — método

Primeira frente da skill. Vale para qualquer empresa; o que muda entre elas está na ficha.

## Sequência
1. **Inventário das fontes** do mês (`01-ENTRADA`): conferir contra a lista da ficha. Faltou fonte essencial: avisar, seguir com o que há e marcar a apuração como parcial.
2. **Base de documentos**: uma linha por documento único. Campos mínimos: origem, tipo (NFS-e, NF-e, CT-e, fatura, recibo), sentido (emitida/recebida), situação (ativa/cancelada/substituída), chave ou número, emissão, competência, CNPJ/CPF da contraparte, município, valor, base, alíquotas, cada retenção, IBS/CBS destacados, arquivo de origem.
   - Deduplicar por chave de acesso; sem chave, por CNPJ + número + valor.
   - Cancelada não some: fica marcada e fora das somas.
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
