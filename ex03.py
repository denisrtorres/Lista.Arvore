#3. Verifique se duas árvores binárias são idênticas.

def identicas(a, b):
    # Ambas vazias
    if a is None and b is None:
        return True
    # Só uma é vazia
    if a is None or b is None:
        return False
    # Compara chave e sub-árvores
    return (a.chave == b.chave
            and identicas(a.esquerda, b.esquerda)
            and identicas(a.direita, b.direita))