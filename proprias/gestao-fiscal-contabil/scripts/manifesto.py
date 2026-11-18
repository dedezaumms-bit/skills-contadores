#!/usr/bin/env python3
"""Congela um fechamento: grava MANIFESTO.csv com tamanho e SHA-256 de cada arquivo da pasta.

  python manifesto.py gerar  <pasta>     cria MANIFESTO.csv (recusa se ja existir)
  python manifesto.py conferir <pasta>   compara os arquivos com o manifesto e lista diferencas

Fechamento congelado nao se altera: correcao posterior vai em nova pasta de ajuste.
"""
import csv, hashlib, os, sys
from datetime import datetime

NOME = "MANIFESTO.csv"


def sha(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def listar(pasta):
    itens = {}
    for raiz, _, arquivos in os.walk(pasta):
        for a in sorted(arquivos):
            if a == NOME:
                continue
            c = os.path.join(raiz, a)
            itens[os.path.relpath(c, pasta).replace(os.sep, "/")] = (os.path.getsize(c), sha(c))
    return itens


def gerar(pasta):
    destino = os.path.join(pasta, NOME)
    if os.path.exists(destino):
        sys.exit("Ja existe manifesto nesta pasta: fechamento congelado nao e regravado.")
    itens = listar(pasta)
    with open(destino, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["arquivo", "bytes", "sha256", "congelado_em"])
        agora = datetime.now().isoformat(timespec="seconds")
        for nome, (tam, h) in sorted(itens.items()):
            w.writerow([nome, tam, h, agora])
    print(f"{len(itens)} arquivos congelados em {destino}")


def conferir(pasta):
    with open(os.path.join(pasta, NOME), newline="", encoding="utf-8") as f:
        antigo = {l["arquivo"]: l["sha256"] for l in csv.DictReader(f, delimiter=";")}
    atual = {n: h for n, (_, h) in listar(pasta).items()}
    dif = ([f"ALTERADO  {n}" for n in antigo if n in atual and atual[n] != antigo[n]] +
           [f"REMOVIDO  {n}" for n in antigo if n not in atual] +
           [f"NOVO      {n}" for n in atual if n not in antigo])
    print("\n".join(dif) if dif else "Integro: nenhum arquivo mudou desde o congelamento.")
    return not dif


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("gerar", "conferir"):
        sys.exit(__doc__)
    if sys.argv[1] == "gerar":
        gerar(sys.argv[2])
    else:
        sys.exit(0 if conferir(sys.argv[2]) else 1)
