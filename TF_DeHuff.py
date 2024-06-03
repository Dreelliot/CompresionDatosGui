import os 
class Nodo:
    def __init__(self, sym, izq=None, der=None):
        self.sym = sym
        self.izq = izq
        self.der = der

def evaluarPreOrden(preOrden):
    resultado = []
    i = 0
    while i < len(preOrden):
        if preOrden[i] == '-' and preOrden[i+1] == '1':
            resultado.append('-1')
            i += 2  # skip over '-1'
        else:
            resultado.append(preOrden[i])
            i += 1
    return resultado

def reconstruirArbol(preOrden):
    def helper(it):
        sym = next(it, None)
        if sym is None or sym == '-1':
            return None
        nodo = Nodo(sym)
        nodo.izq = helper(it)
        nodo.der = helper(it)
        return nodo
    PreOrdenEvaluado = evaluarPreOrden(preOrden)
    it = iter(PreOrdenEvaluado)
    raiz = helper(it)
    return raiz

def DecodificarCodigo(raiz, codificado):
    Decodificado = ''
    nodoActual = raiz
    for bit in codificado:
        if bit == '0':
            nodoActual = nodoActual.izq
        elif bit == '1':
            nodoActual = nodoActual.der
        if nodoActual and nodoActual.izq is None and nodoActual.der is None:
            Decodificado += nodoActual.sym
            nodoActual = raiz
    return Decodificado

def leerArchivo(path):
    with open(path, 'r') as file:
        lines = file.readlines()   
    if len(lines) < 2:
        raise ValueError("The file does not contain enough lines.")  
    arbolPreOrden = lines[0].strip()
    codificado = lines[1].strip()
    return arbolPreOrden, codificado

actual = os.getcwd()
path = os.path.join(actual, 'Comprimido','compresion.huf')
arbolPreOrden, codificado = leerArchivo(path)
raiz = reconstruirArbol(arbolPreOrden)
Decodificado = DecodificarCodigo(raiz, codificado)
print("Mensaje Decodificado:", Decodificado)
