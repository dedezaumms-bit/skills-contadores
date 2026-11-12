#!/usr/bin/env python3
"""Cruza movimentos bancarios com documentos e aponta o que esta sem lastro.

Entradas (CSV com cabecalho, separador ';', valores com ponto decimal, datas AAAA-MM-DD):

  movimentos.csv : id;conta;data;valor;contraparte_doc;contraparte_nome;historico
                   valor > 0 = entrada, valor < 0 = saida
  documentos.csv : id;tipo;numero;data;valor;contraparte_doc;contraparte_nome;sentido
                   sentido = E (documento que justifica ENTRADA: nota emitida, contrato de mutuo recebido...)
                             S (documento que justifica SAIDA: nota recebida, folha, guia, recibo, contrato...)
                   valor sempre positivo
  partes.csv (opcional): doc;nome;relacao   (socios, administrador, familiares, empresas ligadas)

Saidas (na pasta --saida): movimentos_classificados.csv, documentos_sem_movimento.csv, resumo_mensal.csv

Uso: python lastro.py movimentos.csv documentos.csv --partes partes.csv --saida out/ [--dias 10] [--tolerancia 0.05]

O script so LE os arquivos de entrada. Nao decide nada: 'SEM_DOCUMENTO' significa
'nao encontrei documento nas tabelas fornecidas', e nao 'o documento nao existe'.
"""
import argparse, csv, os, re
from collections import defaultdict
from datetime import date
from decimal import Decimal as D
from itertools import combinations

ESPECIE = re.compile(r"\b(saque|especie|dinheiro|cheque avulso|retirada)\b", re.I)


def so_digitos(s):
    return re.sub(r"\D", "", s or "")


def ler(caminho):
    with open(caminho, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f, delimiter=";"))


def dia(s):
    return date.fromisoformat(s.strip())


def cruzar(movs, docs, partes=(), dias=10, tol=D("0.05")):
    partes_doc = {so_digitos(p["doc"]): p.get("relacao", "") for p in partes if so_digitos(p.get("doc"))}
    partes_nome = {p["nome"].strip().upper(): p.get("relacao", "") for p in partes if p.get("nome")}
    for d in docs:
        d["_v"], d["_d"], d["_c"], d["_uso"] = D(d["valor"]), dia(d["data"]), so_digitos(d["contraparte_doc"]), None
    livres = lambda sentido: [d for d in docs if d["_uso"] is None and d["sentido"].strip().upper() == sentido]

    for m in sorted(movs, key=lambda x: -abs(D(x["valor"]))):
        v, dm, c = D(m["valor"]), dia(m["data"]), so_digitos(m["contraparte_doc"])
        sentido = "E" if v > 0 else "S"
        alvo = abs(v)
        cand = [d for d in livres(sentido) if abs((d["_d"] - dm).days) <= dias]
        achado, como = None, ""
        # 1) mesmo valor e mesma contraparte  2) mesmo valor, contraparte nao informada em um dos lados
        for regra, filtro in (("valor+contraparte", lambda d: c and d["_c"] == c),
                              ("so valor", lambda d: not c or not d["_c"])):
            ok = [d for d in cand if abs(d["_v"] - alvo) <= tol and filtro(d)]
            if ok:
                achado, como = [min(ok, key=lambda d: abs((d["_d"] - dm).days))], regra
                break
        # 3) um pagamento cobrindo 2 a 4 documentos da mesma contraparte
        if not achado and c:
            mesmos = [d for d in cand if d["_c"] == c][:12]
            for n in (2, 3, 4):
                combo = next((k for k in combinations(mesmos, n) if abs(sum(d["_v"] for d in k) - alvo) <= tol), None)
                if combo:
                    achado, como = list(combo), f"soma de {n} documentos"
                    break
        parcial = None
        if not achado and c:
            parcial = [d for d in cand if d["_c"] == c]
        if achado:
            for d in achado:
                d["_uso"] = m["id"]
            m["status"] = "COM_DOCUMENTO" if como != "so valor" else "CONFERIR"
            m["documentos"] = ",".join(d["id"] for d in achado)
            m["criterio"] = como
        elif parcial:
            m["status"], m["criterio"] = "VALOR_DIVERGENTE", "mesma contraparte, valor diferente"
            m["documentos"] = ",".join(d["id"] for d in parcial[:5])
        else:
            m["status"], m["documentos"], m["criterio"] = "SEM_DOCUMENTO", "", ""
        sinais = []
        rel = partes_doc.get(c) or partes_nome.get((m.get("contraparte_nome") or "").strip().upper())
        if rel:
            sinais.append(f"parte relacionada ({rel})")
        if ESPECIE.search(m.get("historico") or ""):
            sinais.append("especie")
        if alvo >= 1000 and alvo % 1000 == 0:
            sinais.append("valor redondo")
        if not c and not (m.get("contraparte_nome") or "").strip():
            sinais.append("contraparte nao identificada")
        m["sinais"] = "; ".join(sinais)
    return movs, [d for d in docs if d["_uso"] is None]


def resumo(movs):
    r = defaultdict(lambda: defaultdict(lambda: [0, D(0)]))
    for m in movs:
        chave = (m["data"][:7], "entrada" if D(m["valor"]) > 0 else "saida")
        r[chave][m["status"]][0] += 1
        r[chave][m["status"]][1] += abs(D(m["valor"]))
    linhas = []
    for (mes, sentido), st in sorted(r.items()):
        total = sum(v[1] for v in st.values())
        for status, (q, v) in sorted(st.items()):
            linhas.append({"mes": mes, "sentido": sentido, "status": status, "qtd": q, "valor": f"{v:.2f}",
                           "pct_valor": f"{(v / total * 100 if total else 0):.1f}"})
    return linhas


def gravar(caminho, linhas, campos):
    with open(caminho, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos, delimiter=";", extrasaction="ignore")
        w.writeheader(); w.writerows(linhas)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument("movimentos"); p.add_argument("documentos")
    p.add_argument("--partes"); p.add_argument("--saida", default="saida")
    p.add_argument("--dias", type=int, default=10); p.add_argument("--tolerancia", default="0.05")
    a = p.parse_args()
    movs, docs = ler(a.movimentos), ler(a.documentos)
    partes = ler(a.partes) if a.partes else []
    movs, sobra = cruzar(movs, docs, partes, a.dias, D(a.tolerancia))
    os.makedirs(a.saida, exist_ok=True)
    cm = ["id", "conta", "data", "valor", "contraparte_doc", "contraparte_nome", "historico",
          "status", "documentos", "criterio", "sinais"]
    gravar(os.path.join(a.saida, "movimentos_classificados.csv"), movs, cm)
    gravar(os.path.join(a.saida, "documentos_sem_movimento.csv"), sobra,
           ["id", "tipo", "numero", "data", "valor", "contraparte_doc", "contraparte_nome", "sentido"])
    gravar(os.path.join(a.saida, "resumo_mensal.csv"), resumo(movs),
           ["mes", "sentido", "status", "qtd", "valor", "pct_valor"])
    print(f"{len(movs)} movimentos; {sum(m['status']=='SEM_DOCUMENTO' for m in movs)} sem documento; "
          f"{len(sobra)} documentos sem movimento. Saida em {a.saida}/")


if __name__ == "__main__":
    main()
