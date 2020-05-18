string = "(A.b).(b.c)"
def stringParser(expr):
    def _helper(iter):
        items = []
        for item in iter:
            if item == '(':
                result, closeparen = _helper(iter)
                if not closeparen:
                    raise ValueError("bad expression -- unbalanced parentheses")
                items.append(result)
            elif item == ')':
                return items, True
            else:
                items.append(item)
        return items, False
    return _helper(iter(expr))[0]
def testalista(lista):
    for ramo in lista:
        for item in ramo:
            #print(item)
            if (isinstance(item[1],list)):
                return False
    return True
def percorrerlista(lista):
    #print("lista: ",lista)
    while testalista(lista) == False:
        for ramo in lista:
            #print("lista: ",lista)
            #print("ramo: ",ramo)
            for item in ramo:
                #print("item: ",item)
                if (isinstance(item[1],list)) and (item[0] == "F"):
                    novoramo = ramo[:]
                    novoramo.remove(item)
                    novoramo += ["V",item[1][0]],["F",item[1][-1]]
                    lista.append(novoramo)
                    lista.remove(ramo)
                    break
                if (isinstance(item[1],list)) and (item[0] == "V"):
                    novoramo = ramo[:]
                    novoramo.remove(item)
                    novoramo.append(["F",item[1][0]])
                    lista.append(novoramo)
                    novoramo2 = ramo[:]
                    novoramo2.remove(item)
                    novoramo2.append(["V",item[1][-1]])
                    lista += [novoramo2]
                    lista.remove(ramo)
                    break


def verificaInput(texto): #ERRO!!!!!
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
          'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E',
          'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
          'V','W','Y','Z']
    
    simb=['(',')','>']
    for el in texto: 
        if el not in letra:#verifica simbolos permitidos
            if el not in simb:
                raise Exception('Formula contem simbolos não permitidos. Favor usar apenas letras, paranteses e ">" para implicação')
    
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
                    
lista = stringParser(string)
listaderamos = []
listaderamos += [[["V",lista[0]],["F",lista[-1]]]]
percorrerlista(listaderamos)
print("ramos:")
for i in listaderamos:
    print(i)


 
