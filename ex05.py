#5. Verifique se uma árvore binária é balanceada.

def prof_folhas(raiz, prof=0):
    if raiz is None:
        return (float('inf'), -1)
    if raiz.esquerda is None and raiz.direita is None:
        return (prof, prof)
    min_e, max_e = prof_folhas(raiz.esquerda, prof + 1)
    min_d, max_d = prof_folhas(raiz.direita, prof + 1)
    return (min(min_e, min_d), max(max_e, max_d))

def balanceada(raiz):
    if raiz is None:
        return True
    menor_prof, maior_prof = prof_folhas(raiz)
    return maior_prof - menor_prof <= 1