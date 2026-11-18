#!/usr/bin/env python3
"""Calculos fiscais deterministicos (parametros 2026).

Todos os parametros ficam no topo deste arquivo e espelham references/tabelas-2026.md.
Ao virar o ano ou mudar a lei, atualize os DOIS lugares.

Uso:
  python calculos.py inss 4500
  python calculos.py irrf 6000 --inss 0 --dependentes 1 [--pensao 0]
  python calculos.py simples III 1800000 150000
  python calculos.py presumido 2000000 --irpj 0.32 --csll 0.32 [--outras 5000] [--trimestre 2]
"""
import argparse
from decimal import Decimal as D, ROUND_HALF_UP

ANO = 2026


def r2(x):
    return D(x).quantize(D("0.01"), rounding=ROUND_HALF_UP)


# ---------- INSS segurado (Portaria Interministerial MPS/MF 13/2026) ----------
INSS_FAIXAS = [(D("1621.00"), D("0.075")), (D("2902.84"), D("0.09")),
               (D("4354.27"), D("0.12")), (D("8475.55"), D("0.14"))]
INSS_TETO = D("8475.55")


def inss_segurado(salario):
    """Empregado/domestico/avulso: progressivo por faixa, limitado ao teto."""
    base = min(D(salario), INSS_TETO)
    total, anterior = D(0), D(0)
    for limite, aliq in INSS_FAIXAS:
        if base > anterior:
            total += (min(base, limite) - anterior) * aliq
        anterior = limite
    return r2(total)


def inss_contribuinte_individual(valor, aliq="0.11"):
    """Pro-labore / autonomo a servico de PJ: 11% ate o teto."""
    return r2(min(D(valor), INSS_TETO) * D(aliq))


# ---------- IRRF mensal (tabela desde 05/2025 + redutor Lei 15.270/2025) ----------
IR_FAIXAS = [(D("2428.80"), D("0"), D("0")), (D("2826.65"), D("0.075"), D("182.16")),
             (D("3751.05"), D("0.15"), D("394.16")), (D("4664.68"), D("0.225"), D("675.49")),
             (None, D("0.275"), D("908.73"))]
IR_DEPENDENTE = D("189.59")
IR_SIMPLIFICADO = D("607.20")
RED_LIMITE_TOTAL = D("5000.00")
RED_LIMITE_PARCIAL = D("7350.00")
RED_A, RED_B = D("978.62"), D("0.133145")


def _tabela(base):
    base = max(D(base), D(0))
    for limite, aliq, ded in IR_FAIXAS:
        if limite is None or base <= limite:
            return max(base * aliq - ded, D(0))


def irrf_mensal(rendimento, inss=0, dependentes=0, pensao=0, outras_deducoes=0):
    """Retorna dict com o IRRF devido.

    Usa a mais vantajosa entre deducoes legais e desconto simplificado e depois
    aplica o redutor da Lei 15.270 (calculado sobre o rendimento tributavel bruto).
    """
    rend = D(rendimento)
    legais = D(inss) + D(dependentes) * IR_DEPENDENTE + D(pensao) + D(outras_deducoes)
    deducao = max(legais, IR_SIMPLIFICADO)
    imposto = _tabela(rend - deducao)
    if rend <= RED_LIMITE_TOTAL:
        reducao = imposto
    elif rend <= RED_LIMITE_PARCIAL:
        reducao = min(max(RED_A - RED_B * rend, D(0)), imposto)
    else:
        reducao = D(0)
    return {"base": r2(rend - deducao),
            "deducao_usada": "legais" if legais > IR_SIMPLIFICADO else "simplificado",
            "imposto_tabela": r2(imposto), "reducao_lei_15270": r2(reducao),
            "irrf": r2(imposto - reducao)}


# ---------- Simples Nacional (LC 123, anexos vigentes desde 2018) ----------
SN_LIMITES = [180000, 360000, 720000, 1800000, 3600000, 4800000]
SN = {
    "I":   [("0.04", 0), ("0.073", 5940), ("0.095", 13860), ("0.107", 22500), ("0.143", 87300), ("0.19", 378000)],
    "II":  [("0.045", 0), ("0.078", 5940), ("0.10", 13860), ("0.112", 22500), ("0.147", 85500), ("0.30", 720000)],
    "III": [("0.06", 0), ("0.112", 9360), ("0.135", 17640), ("0.16", 35640), ("0.21", 125640), ("0.33", 648000)],
    "IV":  [("0.045", 0), ("0.09", 8100), ("0.102", 12420), ("0.14", 39780), ("0.22", 183780), ("0.33", 828000)],
    "V":   [("0.155", 0), ("0.18", 4500), ("0.195", 9900), ("0.205", 17100), ("0.23", 62100), ("0.305", 540000)],
}


def simples(anexo, rbt12, receita_mes):
    """Aliquota efetiva e DAS cheio (sem segregar ST/monofasico/retencoes - isso e no PGDAS-D)."""
    rbt12 = D(rbt12)
    if rbt12 > SN_LIMITES[-1]:
        raise ValueError("RBT12 acima de R$ 4,8 milhoes: fora do Simples")
    faixa = next(i for i, lim in enumerate(SN_LIMITES) if rbt12 <= lim)
    nominal, pd = SN[anexo.upper()][faixa]
    efetiva = (rbt12 * D(nominal) - D(pd)) / rbt12 if rbt12 > 0 else D(nominal)
    return {"faixa": faixa + 1, "aliquota_nominal": D(nominal), "parcela_deduzir": D(pd),
            "aliquota_efetiva": efetiva.quantize(D("0.000001")),
            "das": r2(D(receita_mes) * efetiva)}


def fator_r(folha12, rbt12):
    f = D(folha12) / D(rbt12)
    return {"fator_r": f.quantize(D("0.0001")), "anexo": "III" if f >= D("0.28") else "V"}


# ---------- Lucro Presumido trimestral (com acrescimo da LC 224/2025) ----------
LP_LIMITE_TRIM = D("1250000")  # R$ 5 mi/ano proporcional ao trimestre
LP_ACRESCIMO = D("1.10")


def presumido_trimestre(receita, pct_irpj, pct_csll, outras_receitas=0, trimestre=1,
                        irrf_compensar=0):
    """Uma atividade por chamada. Com varias atividades, rateie o excedente
    proporcionalmente a receita de cada uma (IN RFB 2.305/2025, alterada pela 2.306/2026).
    A CSLL so recebe o acrescimo a partir do 2o trimestre de 2026.
    ATENCAO: a regra de ajuste anual do limite deve ser conferida na IN antes de usar.
    """
    receita, outras = D(receita), D(outras_receitas)
    excedente = max(receita - LP_LIMITE_TRIM, D(0))
    normal = receita - excedente
    base_irpj = normal * D(pct_irpj) + excedente * D(pct_irpj) * LP_ACRESCIMO + outras
    ac_csll = LP_ACRESCIMO if trimestre >= 2 else D(1)
    base_csll = normal * D(pct_csll) + excedente * D(pct_csll) * ac_csll + outras
    irpj = base_irpj * D("0.15")
    adicional = max(base_irpj - D(60000), D(0)) * D("0.10")
    csll = base_csll * D("0.09")
    return {"excedente_lc224": r2(excedente), "base_irpj": r2(base_irpj), "irpj": r2(irpj),
            "adicional": r2(adicional), "irpj_a_pagar": r2(irpj + adicional - D(irrf_compensar)),
            "base_csll": r2(base_csll), "csll": r2(csll)}


# ---------- Lucros e dividendos / alta renda (Lei 15.270/2025) ----------
DIV_LIMITE_MES = D("50000")


def dividendos_irrf(total_pago_no_mes):
    """Total que UMA pessoa juridica pagou a UMA pessoa fisica no mes.
    Acima de R$ 50.000, 10% sobre o total (DARF 1841). Ate R$ 50.000, zero."""
    t = D(total_pago_no_mes)
    return r2(t * D("0.10")) if t > DIV_LIMITE_MES else D("0.00")


def irpfm_aliquota(renda_anual_total):
    """Aliquota (%) do IRPF minimo: 0 ate 600 mil; linear ate 10% em 1,2 milhao."""
    r = D(renda_anual_total)
    if r <= D("600000"):
        return D("0")
    return min(r / D("60000") - D("10"), D("10")).quantize(D("0.0001"))


def pis_cofins_cumulativo(receita_base):
    b = D(receita_base)
    return {"pis": r2(b * D("0.0065")), "cofins": r2(b * D("0.03"))}


def pis_cofins_nao_cumulativo(receita_base, base_creditos, receitas_financeiras=0):
    b, c, f = D(receita_base), D(base_creditos), D(receitas_financeiras)
    return {"pis": r2(b * D("0.0165") + f * D("0.0065") - c * D("0.0165")),
            "cofins": r2(b * D("0.076") + f * D("0.04") - c * D("0.076"))}


def _main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    s = p.add_subparsers(dest="cmd", required=True)
    a = s.add_parser("inss"); a.add_argument("salario")
    a = s.add_parser("irrf"); a.add_argument("rendimento"); a.add_argument("--inss", default=0)
    a.add_argument("--dependentes", default=0); a.add_argument("--pensao", default=0)
    a = s.add_parser("simples"); a.add_argument("anexo"); a.add_argument("rbt12"); a.add_argument("receita_mes")
    a = s.add_parser("presumido"); a.add_argument("receita"); a.add_argument("--irpj", required=True)
    a.add_argument("--csll", required=True); a.add_argument("--outras", default=0)
    a.add_argument("--trimestre", type=int, default=1)
    g = p.parse_args()
    if g.cmd == "inss":
        print(inss_segurado(g.salario))
    elif g.cmd == "irrf":
        print(irrf_mensal(g.rendimento, g.inss, g.dependentes, g.pensao))
    elif g.cmd == "simples":
        print(simples(g.anexo, g.rbt12, g.receita_mes))
    else:
        print(presumido_trimestre(g.receita, g.irpj, g.csll, g.outras, g.trimestre))


if __name__ == "__main__":
    _main()
