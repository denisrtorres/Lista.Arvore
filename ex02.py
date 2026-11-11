#2. Encontre o maior elemento em uma BST.

def maior(raiz):
    if raiz is None:
        return None
    if raiz.direita is None:
        return raiz.chave
    return maior(raiz.direita)