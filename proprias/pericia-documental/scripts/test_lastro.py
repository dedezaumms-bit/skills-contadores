"""Rode: python test_lastro.py"""
from decimal import Decimal as D
from lastro import cruzar, resumo

M = lambda i, d, v, c="", n="", h="": {"id": i, "conta": "1", "data": d, "valor": v, "contraparte_doc": c,
                                       "contraparte_nome": n, "historico": h}
Dc = lambda i, d, v, c, s, t="NF": {"id": i, "tipo": t, "numero": i, "data": d, "valor": v,
                                    "contraparte_doc": c, "contraparte_nome": "", "sentido": s}
movs = [
    M("m1", "2026-03-10", "-1500.00", "11.111.111/0001-11"),            # nota exata
    M("m2", "2026-03-12", "-3000.00", "22222222000122"),                # 2 notas somadas
    M("m3", "2026-03-15", "-5000.00", "", "", "SAQUE EM ESPECIE"),      # sem nada
    M("m4", "2026-03-20", "-8000.00", "12345678901", "FULANO SOCIO"),   # socio, sem documento
    M("m5", "2026-03-22", "10000.00", "33333333000133"),                # entrada com nota
    M("m6", "2026-03-25", "7000.00", "44444444000144"),                 # entrada sem nota
    M("m7", "2026-03-27", "-900.00", "55555555000155"),                 # valor divergente
    M("m8", "2026-03-28", "-420.00"),                                   # so valor -> conferir
]
docs = [
    Dc("d1", "2026-03-08", "1500.00", "11111111000111", "S"),
    Dc("d2", "2026-03-05", "1200.00", "22222222000122", "S"),
    Dc("d3", "2026-03-06", "1800.00", "22222222000122", "S"),
    Dc("d5", "2026-03-20", "10000.00", "33333333000133", "E"),
    Dc("d7", "2026-03-26", "950.00", "55555555000155", "S"),
    Dc("d8", "2026-03-28", "420.00", "", "S", "RECIBO"),
    Dc("d9", "2026-03-30", "25000.00", "66666666000166", "E"),          # nota emitida sem recebimento
]
partes = [{"doc": "123.456.789-01", "nome": "Fulano Socio", "relacao": "socio"}]
movs, sobra = cruzar(movs, docs, partes)
s = {m["id"]: m for m in movs}
assert s["m1"]["status"] == "COM_DOCUMENTO" and s["m1"]["documentos"] == "d1"
assert s["m2"]["status"] == "COM_DOCUMENTO" and s["m2"]["criterio"] == "soma de 2 documentos"
assert s["m3"]["status"] == "SEM_DOCUMENTO" and "especie" in s["m3"]["sinais"] and "valor redondo" in s["m3"]["sinais"]
assert s["m4"]["status"] == "SEM_DOCUMENTO" and "parte relacionada (socio)" in s["m4"]["sinais"]
assert s["m5"]["status"] == "COM_DOCUMENTO"
assert s["m6"]["status"] == "SEM_DOCUMENTO"
assert s["m7"]["status"] == "VALOR_DIVERGENTE"
assert s["m8"]["status"] == "CONFERIR"
assert [d["id"] for d in sobra] == ["d7", "d9"]  # d7 fica pendente: valor nao bate
r = resumo(movs); assert any(x["status"] == "SEM_DOCUMENTO" and x["sentido"] == "saida" and x["valor"] == "13000.00" for x in r)
print("ok")
