#1. Encontre o menor elemento em uma BST.

def menor(raiz):
    if raiz is None:
        return None
    if raiz.esquerda is None:
        return raiz.chave
    return menor(raiz.esquerda)