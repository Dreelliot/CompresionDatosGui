import matplotlib.pyplot as plt
import graphviz as gv
import collections 
import heapq
import os

codigo ={}

frec = collections.defaultdict(int)

class nodoMinHeap:
    def __init__(self,sym,frec):
        self.izq=None
        self.der=None
        self.sym=sym
        self.frec=frec
    
    def __lt__(self,other):
        return self.frec<other.frec
    
def printCodigo(raiz,str):
    if raiz is None:
        return
    if raiz.sym !='$':
        print(raiz.sym+':'+str)
    printCodigo(raiz.izq,str+'0')
    printCodigo(raiz.der,str+'1')

def guardaCodigo(raiz,str): 
    if raiz is None:
        return
    if raiz.sym !='$':
        codigo[raiz.sym]=str
    guardaCodigo(raiz.izq,str+'0')
    guardaCodigo(raiz.der,str+'1')

def Huffman():
    global minHeap
    for key in frec:
        minHeap.append(nodoMinHeap(key,frec[key]))
    heapq.heapify(minHeap)
    while len(minHeap)!=1:
        izq = heapq.heappop(minHeap)
        der = heapq.heappop(minHeap)
        top = nodoMinHeap('$',izq.frec+der.frec)
        top.izq = izq
        top.der = der
        heapq.heappush(minHeap,top)
    guardaCodigo(minHeap[0],'')

def calcFrec(string):
    n = len(string)
    for i in range(n):
        frec[string[i]]+=1
        #print(frec)
    return frec

def plotFrec(frec):
    tabla_frecuencia= plt.bar([sym for sym  in frec.keys()], [ cant for cant in frec.values()],fc='Turquoise',ec='Black')
    plt.bar_label(tabla_frecuencia,labels=[cant for cant in frec.values()], label_type='edge',fontsize=12,padding=3)
    plt.title('Frecuencia Caracteres', fontsize=20)
    plt.xlabel('Caracteres')
    plt.ylabel('Frecuencia')
    plt.show()

def printArbolPre(raiz):
    if raiz is None:
        return
    print(raiz.sym,end='') 
    if raiz.izq is None:
        print('-1',end='')
    if raiz.der is None:
        print('-1',end='')
    printArbolPre(raiz.izq)
    printArbolPre(raiz.der)

def writeArbolPre(raiz,fp):    
        if raiz is None:
            return
        fp.write(raiz.sym) 
        if raiz.izq is None:
            fp.write('-1')
        if raiz.der is None:
            fp.write('-1')
        writeArbolPre(raiz.izq,fp)
        writeArbolPre(raiz.der,fp)

def writeCodificado(string,fp):
    codificado=''
    for i in string:
        codificado+=codigo[i]
    fp.write('\n'+codificado)
    return codificado


def mkFile(raiz,str):
    #Raiz=raiz
    archActual = os.getcwd()
    sub = 'Comprimido'
    file = 'compresion.huf'
    newsub = os.path.join(archActual, sub)
    file_path = os.path.join(newsub, file)
    if not os.path.exists(newsub):
        os.makedirs(newsub)
    with open(file_path, 'w') as fp:
        writeArbolPre(raiz, fp)
        writeCodificado(str,fp)
        
        
def codificar(string):
    codificado=''
    for i in string:
        codificado+=codigo[i]
    print('Codigo Huffman: \n',codificado)
    return codificado

def decodificar_archivo(raiz,s):
    ans=''
    actual=raiz
    n=len(s)
    for i in range(n):
        if s[i]=='0':
            actual=actual.izq
        else:
            actual=actual.der

        if actual.izq is None and actual.der is None:
            ans+=actual.sym
            actual=raiz
    return ans

if __name__ == '__main__':
    minHeap=[]
    string='mama amo a mamama'
    #string='tres tristes tigres tragaban trigo en un trigal en tres tristes trastos'
    decodificado= ''
    frec= calcFrec(string)
    plotFrec(frec)
    Huffman()
    printArbolPre(minHeap[0])
    printCodigo(minHeap[0],'')
    codificado = codificar(string)
    mkFile(minHeap[0],string)
   
    decodificado=decodificar_archivo(minHeap[0],codificado)
    print('Decodificado: \n',decodificado)