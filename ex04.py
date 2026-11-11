#4. Calcule a altura de uma BST.

def altura(raiz):
    if raiz is None:
        return 0
    return 1 + max(altura(raiz.esquerda), altura(raiz.direita))