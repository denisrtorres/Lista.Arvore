#6. Determine se uma árvore é simétrica.

def espelhos(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.chave == b.chave
            and espelhos(a.esquerda, b.direita)
            and espelhos(a.direita, b.esquerda))

def simetrica(raiz):
    if raiz is None:
        return True
    return espelhos(raiz.esquerda, raiz.direita)