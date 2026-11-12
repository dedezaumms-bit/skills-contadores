# MT Concreto LTDA — ficha fiscal

Dados institucionais, pessoas e documentos timbrados: skill `mt-concreto`. Folha, premiação e Caju: skill `fechamento-mtconcreto`.
Esta ficha foi extraída da skill `auditoria-fiscal-mtconcreto`, que continua valendo até a validação descrita ao final.

## Cadastro
- CNPJ: matriz 49.508.863/0001-63; filial 0002-44
- Regime: Lucro Real; PIS/COFINS não cumulativo. Periodicidade do IRPJ/CSLL (trimestral ou anual): **confirmar com a contabilidade**
- Atividade: concretagem (concreto usinado e bombeamento). Emite apenas NFS-e
- Municípios (código IBGE): Cuiabá 5103403 · Várzea Grande 5108402 · Poconé 5106505 · Acorizal 5100102
- Contabilidade externa: Solução Contabilidade MT, sistema Domínio

## Tributos e obrigações aplicáveis
- ISSQN próprio por município de prestação; retido por tomadores; devido como tomadora (IssRetido=1 nas notas tomadas)
- Retenções federais como tomadora: IRRF e CSRF
- PIS/COFINS não cumulativo; IRPJ/CSLL (aqui só bases; LALUR é da contabilidade)
- Estadual: sem apuração própria; monitorar NF-e/CT-e interestaduais (DIFAL/ST) sem calcular guia
- 2026: conferir destaque de CBS/IBS nas NFS-e emitidas e recebidas

## Fontes de dados — pasta `FISCAL MM-AAAA`
| Subpasta | Conteúdo | Cuidados |
|---|---|---|
| PDF E XML BAIXADO DO QIVE | XML+PDF de NFS-e emitidas/recebidas dos 2 CNPJs (com canceladas), NF-e, CT-e | Chave pode repetir entre pastas de manifestação e matriz/filial |
| RELATORIOS EM EXCEL DO QIVE | NFS-e emitidas, tomadas, NF-e, CT-e | Duplicatas "(1)": detectar por MD5; ler com pandas |
| RELATORIOS EMITIDOS DO PUZL | PDF de entradas por central (MTVG/MTC2); XLSX ENTRADAS (1 linha/documento); XLSX DESPESAS (1 linha/**item** — não somar como total) | DESPESAS tem chave de 44 dígitos e flags de retenção |
| FATURAS E NFS-E SALVAS POR ANDRE | Não eletrônicos: aluguéis, NFS-e de outros estados, notas de débito | Escaneados: OCR |
| APURACAO FEITA PELA CONTABILIDADE EXTERNA | Demonstrativo PIS/COFINS, acompanhamento de entradas, livro de ISSQN | Chegam depois |
| AUDITORIA | Saída | |

Layouts: NFS-e ABRASF 2.02 (raiz CompNfse, gerador Várzea Grande); NF-e 4.00; CT-e 4.00.
Casamento Qive × PUZL: chave de 44 dígitos; senão CNPJ + número; senão CNPJ + valor (± R$ 0,02).

## Particularidades de apuração
- ISS em Cuiabá: base com dedução de materiais (cerca de 40% do valor). Várzea Grande: base cheia, 5%.
- Retenções a recolher: usar o **maior conjunto** entre XML, relatórios e PDFs (há retenção que só aparece no PDF).
- Créditos de PIS/COFINS: critério amplo de concreteira (matéria-prima, combustível, frete de insumo com CT-e como tomadora, energia, locação de PJ, manutenção), com a origem de cada crédito marcada e ressalva para validação da contabilidade. Depreciação e extemporâneos são lançados pela contabilidade.
- Pacote para escrituração: união de todas as fontes, nada fica de fora.

## Entregáveis esperados (em `AUDITORIA/`)
Dashboard HTML autocontido · planilha de auditoria (fórmulas reais) · relatório executivo PDF · ZIP de escrituração (01-NF-E, 02-CT-E, 03-MDF-E, 04-NFS-E, 05-NFS-E COM RETENCOES, 06-não eletrônicos + relatório do pacote) · planilha de confronto com a contabilidade quando os arquivos dela chegarem.

## Pendências e histórico
Mantidos na skill `auditoria-fiscal-mtconcreto` (baseline 06/2026 e pendências herdadas). Não foram copiados para cá porque este arquivo é versionado em repositório.

## Validação pendente desta ficha
Rodar a competência 06/2026 por esta skill e comparar com o baseline. Só depois de os números baterem a skill antiga pode ser aposentada.
