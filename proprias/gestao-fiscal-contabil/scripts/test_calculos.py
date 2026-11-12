"""Rode: python test_calculos.py  (valores de conferencia conhecidos)."""
from decimal import Decimal as D
from calculos import *

assert inss_segurado(1621) == D("121.58")
assert inss_segurado(8475.55) == D("988.09") == inss_segurado(20000)
assert inss_segurado(3000) == r2(D("121.575") + D("1281.84") * D("0.09") + D("97.16") * D("0.12"))
# Redutor: zera ate 5.000; some em 7.350
assert irrf_mensal(5000)["irrf"] == D("0.00") and irrf_mensal(5000)["imposto_tabela"] == D("312.89")
assert irrf_mensal(2400)["irrf"] == D("0.00")
x = irrf_mensal(6000); assert x["reducao_lei_15270"] == r2(D("978.62") - D("0.133145") * 6000)
assert irrf_mensal(7350)["reducao_lei_15270"] == D("0.00")
assert irrf_mensal(10000)["irrf"] == r2((D(10000) - D("607.20")) * D("0.275") - D("908.73"))
# Simples: TI Anexo III, RBT12 1,8 mi -> 14,02%
s = simples("III", 1800000, 150000); assert s["aliquota_efetiva"] == D("0.140200") and s["das"] == D("21030.00")
assert simples("I", 180000, 10000)["das"] == D("400.00")
assert fator_r(540000, 1800000)["anexo"] == "III"
# Presumido comercio 1 mi + 5 mil financeira (sem excedente)
p = presumido_trimestre(1000000, "0.08", "0.12", 5000)
assert p["irpj"] == D("12750.00") and p["adicional"] == D("2500.00") and p["csll"] == D("11250.00")
# Servicos 2 mi no 2o tri: 750 mil excedem -> 35,2%
p = presumido_trimestre(2000000, "0.32", "0.32", trimestre=2)
assert p["base_irpj"] == D("664000.00") == p["base_csll"]
assert presumido_trimestre(2000000, "0.32", "0.32", trimestre=1)["base_csll"] == D("640000.00")
assert dividendos_irrf(50000) == D("0.00") and dividendos_irrf(50000.01) == D("5000.00")
assert irpfm_aliquota(600000) == D("0") and irpfm_aliquota(750000) == D("2.5000") and irpfm_aliquota(2000000) == D("10")
print("ok")
