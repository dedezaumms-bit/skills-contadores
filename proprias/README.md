# Skills próprias

| Skill | Papel | Situação |
|---|---|---|
| `gestao-fiscal-contabil/` | Apura e confere impostos, confronta com a contabilidade, balanço e DRE paralelos, folha, financeiro, pessoas físicas, preparação para 2027, registro de decisões e fechamentos congelados | Método escrito; scripts testados; nenhuma frente rodou com dados reais |
| `pericia-documental/` | Diagnóstico interno: examina os documentos como um perito, aponta o que está sem lastro, monta a lista de busca e dimensiona a exposição | Método e script prontos; ainda não rodou com dados reais |

Nenhum dado de empresa ou pessoa fica neste repositório. Fichas, documentos e resultados ficam na pasta local do usuário.

Instalação: compactar cada pasta de skill e enviar em Configurações → Skills do Claude, ou copiar para `.claude/skills/`.

Testes:
- `python proprias/gestao-fiscal-contabil/scripts/test_calculos.py`
- `python proprias/pericia-documental/scripts/test_lastro.py`

As 57 skills em `skills/` ficaram como material de consulta; não instalar (conteúdo de 2024/2025).
