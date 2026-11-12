# Skills próprias

`apuracao-fiscal/` — skill única para apurar o fiscal das empresas e das pessoas físicas.

- `SKILL.md`: método e regras de uso.
- `references/`: base comum (tabelas 2026, calendário, regras por regime, reforma tributária).
- `entidades/`: uma ficha por empresa ou pessoa (`_modelo-pj.md`, `_modelo-pf.md`, `mt-concreto.md`).
- `scripts/calculos.py`: INSS, IRRF com redutor, DAS do Simples, Lucro Presumido com LC 224. Teste: `python scripts/test_calculos.py`.

Instalação: compactar a pasta `apuracao-fiscal` e enviar em Configurações → Skills do Claude, ou copiar para `.claude/skills/`.

As 57 skills em `skills/` ficaram como material de consulta; não instalar (conteúdo de 2024/2025).
