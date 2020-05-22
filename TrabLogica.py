
__all__=['stringParser','percorrerlista','testalista','encontracontraex']


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
                
def encontracontraex(lista):
    for ramo in lista:
        valordict = {}
        for obj in ramo:
            if obj[1] in valordict:
                if obj[0] != valordict[obj[1]]:
                    lista.remove(ramo)
            else:
                valordict[obj[1]] = obj[0]
    print("Inválido, contraexemplo:")
    print([list(tupl) for tupl in {tuple(item) for item in lista[0] }])
    return







