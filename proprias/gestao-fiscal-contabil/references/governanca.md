# Governança — trilha, decisões e fechamento congelado

Serve a qualquer empresa. Protege o administrador porque mostra, com data, o que foi feito, com base em quê e quem sabia.

## 1. Rastro de cada número
Todo valor de entregável aponta para a origem: arquivo, aba/página, linha ou chave do documento. Número sem origem não entra em entregável; entra em Pendências.

## 2. Registro de decisões (`DECISOES/registro.csv` na pasta da entidade)
Uma linha por decisão relevante do administrador ou dos sócios: id · data · assunto · decisão · motivo · alternativas consideradas · base documental (arquivos) · quem decidiu · quem foi informado e como (e-mail, mensagem, reunião, com referência) · efeito financeiro · fechamento a que se refere.

Registrar sempre: distribuição de lucros e pró-labore, operações com sócios e partes relacionadas, contratação ou pagamento fora do padrão, escolha entre leituras de regra fiscal, mudança de critério contábil, correção de erro, regularização de pendência, escolha de regime tributário.

A linha é escrita **na data em que a decisão é tomada**. Decisão antiga reconstruída depois é registrada com a data de hoje e o campo motivo começando por "Registro posterior de decisão tomada em DD/MM/AAAA", citando a evidência da época.

## 3. Fechamento congelado
Ao concluir um fechamento, os entregáveis vão para `03-FECHAMENTO` e roda-se `scripts/manifesto.py gerar <pasta>`. A partir daí a pasta não muda. Correção posterior: nova pasta `03-FECHAMENTO-AJUSTE-n`, com um arquivo `MOTIVO.md` (o que mudou, por quê, documento que motivou) e manifesto próprio. `manifesto.py conferir` prova que nada foi alterado.

## 4. Sócios e partes relacionadas
Lista mantida na ficha. Todo mês, extrato por pessoa: valor, data, título (pró-labore, lucro, reembolso, mútuo, aluguel, outro), documento. Lucro distribuído é comparado com o lucro apurado, a proporção do contrato social e a deliberação escrita. Diferença entre sócios é mostrada, não explicada pela skill.

## 5. Prestação de contas
Trimestralmente, montar o pacote do administrador para os sócios: demonstrações, extrato de partes relacionadas, decisões do período, pendências abertas. O envio e o registro de recebimento são do usuário; a skill prepara e anota no registro de decisões quando e para quem foi enviado, se o usuário informar.

## 6. O que a skill não faz
Não altera nem apaga documento de origem; não gera documento com data anterior à de criação; não reclassifica operação para que deixe de aparecer; não regrava fechamento congelado.
