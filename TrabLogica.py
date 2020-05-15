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
lista = stringParser(string)
print(lista)
listaderamos = []
listaderamos += [[["F",lista[0]],["F",lista[-1]]]]
def percorrerlista(lista):
    for item in lista[0]:
        print(item)
        if (len(item[1]) != 2) and (item[0] == "F"):
            teste = lista[0][:]
            teste.remove(item)
            teste += ["V",item[1][0]],["F",item[1][-1]]
            lista.append(teste)
            lista.remove(lista[0])
            break
percorrerlista(listaderamos)
print(listaderamos)
