---
name: abertura-empresa-cnpj
description: Conduz abertura de empresa do zero até CNPJ ativo: viabilidade, REDESIM, contrato social, alvarás, inscrições estadual/municipal, CNAE, regime tributário e eSocial.
allowed-tools: Read Grep Bash Edit Write
user-invocable: true
---

## Quando usar

Cliente quer abrir uma empresa: nova operação, segunda empresa, holding, mudança de natureza jurídica. Roteiro de 5-15 dias dependendo do município.

## Inputs necessários

1. Identificação dos sócios (CPF, RG, comprovante de endereço, e-CPF para assinatura digital)
2. Atividade principal e secundárias (CNAE)
3. Capital social e participação por sócio
4. Endereço (próprio, alugado, virtual — verificar se o município permite)
5. Tipo societário desejado (LTDA, S.A., EIRELI extinta — agora SLU; MEI, ME, EPP)
6. Regime tributário pretendido (skill 42)
7. Nome empresarial (consulta de viabilidade)

## Fluxo (REDESIM — Rede Nacional para Simplificação)

### 1. Viabilidade do nome e do endereço (gov.br/empresas)
- Consulta nacional de nome (não pode haver registro idêntico/semelhante)
- Consulta de endereço × CNAE (zoneamento municipal)

### 2. Coleta nacional do CNPJ via REDESIM
- Preenchimento do DBE (Documento Básico de Entrada)
- Solicitação de inscrição (Receita Federal, Estado, Município, ME/EPP, Bombeiros, Anvisa)
- A partir de 2024: integração total via gov.br/empresas

### 3. Contrato social
- Cláusulas obrigatórias: nome empresarial, sede, capital, sócios, atividade, prazo, administração
- Modelo simplificado (microempresa) ou completo (LTDA não-ME)
- Assinatura digital (e-CPF) — todos os sócios

### 4. Registro na Junta Comercial
- Junta Comercial (atividade comercial/industrial) ou Cartório (atividade não-comercial — sociedade simples, advogados, médicos)
- Taxa: variável por estado (~R$ 100-400)

### 5. CNPJ ativo
- Após registro, REDESIM gera o CNPJ
- Acessar gov.br/empresas para emitir Cartão CNPJ

### 6. Inscrição estadual (se atividade exigir)
- ICMS: comércio, indústria, transporte, comunicação
- Inscrição no SEFAZ (cada estado tem portal)
- Vinculação à Junta Comercial

### 7. Inscrição municipal (ISS)
- Prefeitura — alvará de funcionamento + cadastro mobiliário
- Algumas atividades: alvará sanitário, vigilância ambiental, bombeiros

### 8. Senha e-CAC + procuração eletrônica para o contador

### 9. Opção pelo regime tributário
- Simples Nacional: até último dia útil de janeiro (ou na abertura, se cabível)
- Lucro Presumido / Real: na primeira DARF do ano
- MEI: na própria abertura via Portal do Empreendedor

### 10. Cadastros adicionais
- INSS / CAEPF (PF empregador)
- FGTS / Conectividade Social ICP / FGTS Digital
- eSocial (se houver empregados)
- Certificado digital e-CNPJ A1 ou A3

### 11. Setup contábil
- Plano de contas (skill 31)
- ERP / sistema de gestão
- Notas fiscais eletrônicas (NFe, NFC-e, NFS-e)
- Conta bancária PJ

## CNAE

A atividade principal é o **CNAE primário** — usar a tabela CNAE 2.3 (ou a vigente). CNAEs secundários: até 99 outros relacionados.

Cuidado:
- CNAE escolhido define ICMS-ST, regime do Simples (anexo), RAT, encargos previdenciários.
- Empresa de prestação de serviço com CNAE de comércio = problema fiscal.

## Tipos societários (resumo)

| Tipo | Sócios | Capital | Responsabilidade |
|---|---|---|---|
| MEI | 1 | n/a | Limitada (com exceções) |
| Sociedade Limitada (LTDA) | 1+ (SLU se 1) | Definido em contrato | Limitada à integralização |
| Sociedade Anônima (S.A.) | 2+ acionistas | Mín R$ varia | Limitada à integralização |
| Sociedade Simples | 2+ | Definido | Solidária ou subsidiária |
| Empresa Individual (Empresário) | 1 | Definido | Ilimitada (PF responde) |

EIRELI foi extinta — Lei 14.195/2021 substituiu pela SLU (Sociedade Limitada Unipessoal).

## Templates

### Checklist completo de abertura

```
CLIENTE __________ Início: __/__/____ Conclusão: __/__/____

PRÉ-ABERTURA
[ ] CPF + e-CPF de todos os sócios
[ ] Comprovante de endereço dos sócios
[ ] Atividade definida (CNAE primário e secundários)
[ ] Capital social acordado
[ ] Tipo societário: __________
[ ] Endereço da empresa (próprio/alugado/virtual)

REDESIM
[ ] Viabilidade nome — protocolo: __________
[ ] Viabilidade endereço × CNAE — protocolo: __________
[ ] DBE preenchido — protocolo: __________

CONTRATO SOCIAL
[ ] Minuta elaborada
[ ] Assinaturas digitais coletadas
[ ] Junta Comercial / Cartório protocolado em __/__/____
[ ] NIRE / Registro: __________

INSCRIÇÕES
[ ] CNPJ emitido em __/__/____ (n° __________)
[ ] Inscrição Estadual (se aplicável) — n° __________
[ ] Inscrição Municipal — n° __________
[ ] Alvará de funcionamento
[ ] Alvará sanitário (se aplicável)
[ ] Bombeiros (se aplicável)

OPÇÃO TRIBUTÁRIA
[ ] Simples Nacional: opção em __/__/____
   Anexo previsto: ___
[ ] Outro: _____________

CONTÁBIL E DIGITAL
[ ] e-CNPJ A1 emitido (validade __/__/____)
[ ] Procuração e-CAC para contador
[ ] CAEPF (se PF empregador)
[ ] FGTS Digital ativado
[ ] eSocial: cadastro inicial S-1000 (se houver empregados)
[ ] Plano de contas implantado
[ ] ERP configurado
[ ] Banco PJ aberto: __________

NOTAS FISCAIS
[ ] Senha SEFAZ para NFe/NFC-e
[ ] Inscrição na NFS-e nacional
[ ] Sequencial NF iniciado em ___
```

## Erros comuns

- CNAE primário errado para a atividade real — afeta tributação e licenciamento.
- Endereço residencial em município que veda atividade comercial sem alvará.
- Capital social muito baixo (R$ 100) sem suporte para a operação real — descrédito com bancos/fornecedores.
- Esquecer de optar pelo Simples no prazo → empresa entra direto em Presumido com ônus maior.
- Sócio com pendência na Receita (CADIN, débitos): bloqueia abertura ou inclusão.
- Endereço virtual em município que não permite — alvará negado.
- Atividade que exige Conselho (CRC, CREA, CRM, OAB) sem registro no conselho antes de operar.

## Checklist final (pós-abertura)

- [ ] Empresa operando
- [ ] NF emitida com sucesso
- [ ] Conta bancária PJ ativa
- [ ] Sistema contábil rodando
- [ ] Contrato com contador assinado
- [ ] Cliente com cronograma de obrigações fiscais

## Referências

- Lei 14.195/2021 (REDESIM consolidada)
- Lei 11.598/2007 (REDESIM original)
- Decreto 9.554/2018
- Resolução CGSIM (regulamento operacional)
- LC 123/2006 (Simples)
- Código Civil arts. 966-1.195 (sociedade)
- Lei 6.404/1976 (S.A.)
