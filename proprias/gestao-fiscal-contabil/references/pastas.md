# Estrutura de pastas

A raiz é a pasta sincronizada do OneDrive informada pelo usuário (fica na ficha, não nesta skill). Uma pasta por entidade; nada de uma entidade é lido ou gravado na pasta de outra.

```
<RAIZ>/
  <ENTIDADE>/
    00-CADASTRO/
      ficha.md                  ← ficha da entidade (a partir de modelos/)
      DOCS SOCIEDADE/           ← contrato social, alterações, atas, procurações
      contas-bancarias.xlsx
      sistemas.xlsx
      de-para-plano-de-contas.xlsx
    DECISOES/registro.csv
    AAAA/
      MM-AAAA/
        01-ENTRADA/             ← só documentos de origem; a skill não grava aqui
          BANCOS/  NOTAS-EMITIDAS/  NOTAS-RECEBIDAS/  SISTEMA-GESTAO/
          FOLHA/   CONTABILIDADE/   OUTROS/
        02-TRABALHO/            ← bases intermediárias, podem ser refeitas
        03-FECHAMENTO/          ← entregáveis + MANIFESTO.csv (congelado)
      TRIMESTRE-n/              ← balanço e DRE paralelos, mesmo padrão 01/02/03
  _GRUPO/
    AAAA/MM-AAAA/               ← visão consolidada (só totais; sem documentos)
  <PESSOA>/                     ← pessoa física: 00-CADASTRO, AAAA/MM-AAAA, AAAA/DECLARACAO
```

- Subpastas de `01-ENTRADA` podem ter outro nome se a ficha disser (ex.: estrutura já usada de downloads do portal de notas).
- Resultados da skill `pericia-documental` **não** ficam nesta árvore; vão para o local indicado pelo usuário.
- Antes da primeira gravação em uma entidade, confirmar a raiz com o usuário e criar a árvore.
