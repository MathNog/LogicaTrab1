from tkinter import *
from TrabLogica import *

string = "((((a>b)>(c>d))>d)>(a>d))"
teste=''

def verificaFormula(entradaLb,botaoGerar):
    global teste
    teste=entradaLb.get()
    #print(teste)
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
          'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E',
          'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
          'V','W','Y','Z']
    
    simb=['(',')','>']
    for el in teste: 
        if el not in letra:#verifica simbolos permitidos
            if el not in simb:
                entradaLb.delete(0,END)
                entradaLb.focus_set()
                print('Formula contem simbolos não permitidos. Favor usar apenas letras, paranteses e ">" para implicação')
        else:
            botaoGerar['state']=NORMAL
            botaoGerar.focus_set()
    '''
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
    '''

def list2string(lista): #Arrumar no controle para exibir o contra exemplo
    texto=''
    for el in lista:
        texto+=el
    return texto


def controle(teste):
    print(teste)
    lista = stringParser(teste)
    #print(lista)
    listaderamos = []
    listaderamos += [[["V",lista[0][0]],["F",lista[0][-1]]]]
    #print(listaderamos)
    percorrerlista(listaderamos)
    print("ramos:")
    for i in listaderamos:
        print(i)
    contraex = encontracontraex(listaderamos)
    contra=list2string(contraex)#arrumar
    #controla exibicao na janela
    if contraex!=[]:
        lbC1=Label(root,text="Fórmula Falsificavel. Contra exemplo:",width=40,anchor="nw")
        lbC1.place(x=10,y=240)
        lbC2=Label(root,text=contra,width=20,anchor='nw')
        lbC1.place(x=10,y=250)
    else:
        lbD1=label(root,text='Fórmula Válida!',width=20,anchor='nw')
        lbD1.place(x=10,y=240)


#----Janela Principal---- OK!!!!

root=Tk()
root.geometry('400x400')
root.title("Tableaux Generator")

#---Label para inserir fórmula--- OK!!!!

lb=Label(root,text="Insira Fórmula:",width=12,anchor='nw')
lb.place(x=150,y=10)
entradaLb=Entry(root,width=60)
entradaLb.place(x=10,y=40)
entradaLb.focus_set()


#-------Label para resultado------ 0K!!!
lbRes=Label(root,text="Resultado do Tableaux:",width=20,anchor="nw")
lbRes.place(x=10,y=230)


#----Botao Validar Fórmula---- OK!!!!
botaoValidar=Button(root,text='Validar',width=12)
botaoValidar.place(x=150,y=80)
botaoValidar.config(command=lambda:verificaFormula(entradaLb,botaoGerar))


#---Botao gerar Tableaux---- OK!!!!
botaoGerar=Button(root,text='Gerar Tableaux',width=12,height=5,state=DISABLED)
botaoGerar.place(x=150,y=120)
botaoGerar.config(command=lambda:controle(teste))




#----Loop----

root.mainloop()
