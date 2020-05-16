'''
Ideia:lista de lista para cada ramo do tablueau
Começamos com apenas um ramo, o input com F adicionado
Sempre que quebramos a expressao, adicionamos o resultado da quebra no ramo
ex: ramo1=[[F (a>b)],Va,Vb]
O problema é para o caso V de implicacao, onde precisamos criar um novo ramo
'''


'''
Problemas a resolver: 
erro na funcao verifica input, na aprte da boa formação -> IndexError: string index out of range
'''


def verificaInput(texto):
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
          'p','q','r','s','t','u','v','w','x','y','z']
    simb=['(',')','>']
    for el in texto: 
        if el not in letra:#verifica simbolos permitidos
            if el not in simb:
                raise Exception('Formula contem simbolos não permitidos. Favor usar apenas letras minúsculas, paranteses e ">" para implicação')
    
    for i in range(0,len(texto)+1):#verifica a boa formação
        
        if texto[i] in letra and texto[i+1]!=')':
            if texto[i+1]!=">":
                raise Exception('Formula mal formada')
                
        if texto[i] == "(" and texto[i+1]!='(':
            if texto[i+1] not in letra:
                raise Exception('Formula mal formada')
                
        if texto[i] == ")" and texto[i+1]!=')':
            if texto[i+1] !='>':
                raise Exception('Formula mal formada')
                
        if texto[i] == ">" and texto[i+1]!='(':
            if texto[i+1] not in letra:
                raise Exception('Formula mal formada')
        


def addF(texto): #adiciona F no primeiro caracter da string
    textoF=[]
    textoF.append("F")
    for el in texto:
        textoF.append(el)
    texto=textoF
    return textoF    


def retornaIndice(texto): #retorna indice do '>' mais externo
    cont=0
    ind=0
    for el in texto:
        
        if el == "(":
            cont+=1
        elif el==")":
            cont=cont-1
        if el==">" and cont==0:
            break
        ind+=1
        
    return ind 

def limpa(texto): #limpa lista
    texto.clear()

#só recebe formulas cuja valorazao e V -> precisa bifurcar
def quebraVerd(texto):
    ind = retornaIndice(texto)
    for i in range(1,ind):
        ant.append(texto[i])
    for j in range (ind+1,len(texto)):
        dps.append(texto[j])

#só recebe formulas cuja valorazao e F -> nao precisa bifurcar
def quebraFal(texto):
    global ant,dps
    ant.append("V")
    dps.append("F")
    ind = retornaIndice(texto)
    for i in range(1,ind):
        ant.append(texto[i])
    for j in range (ind+1,len(texto)):
        dps.append(texto[j])



teste="(a>b)>(b>a)"
ant=[]
dps=[]

verificaInput("(a>b)>c")

testeF=addF(teste)
quebraFal(testeF)

print(retornaIndice(testeF))

print(ant)
print(dps)

limpa(ant)
limpa(dps)


