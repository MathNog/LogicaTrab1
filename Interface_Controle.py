from tkinter import *
from tkinter import messagebox
from Funcoes_Tableaux import *

#-----Variáveis Globais-------
teste=''

#-------Funções----------
def verificaFormula(entradaLb,botaoGerar):
    global teste
    
    teste=entradaLb.get()
    
    letra=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
          'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E',
          'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
          'V','W','Y','Z']
    simb=['(',')','>']
    
    #verifica simbolos permitidos
    for el in teste:
        if el not in letra:
            if el not in simb:
                entradaLb.delete(0,END)
                entradaLb.focus_set()
                messagebox.showinfo("", "Formula contem símbolos não permitidos. Usar apenas letras, parênteses e '>' para implicação")
        else:
            botaoGerar['state']=NORMAL
            botaoGerar.focus_set()
    
    #começo e fim com parênteses 
    if teste[0]!='(' or teste[-1]!=')':
        entradaLb.delete(0,END)
        entradaLb.focus_set()
        messagebox.showinfo("", "Fórmula precisa começar e terminar com parênteses")
        botaoGerar['state']=DISABLED
        
    for i in range(1,len(teste)-1):
        if teste[i]== '>' and teste[i+1]==')':
            entradaLb.delete(0,END)
            entradaLb.focus_set()
            messagebox.showinfo("", "Fórmula mal formada: '>' logo antes de ')'")
            botaoGerar['state']=DISABLED
            
        if teste[i] in letra and teste[i+1]in letra:
            entradaLb.delete(0,END)
            entradaLb.focus_set()
            messagebox.showinfo("", "Fórmula mal formada: duas letras juntas ")
            botaoGerar['state']=DISABLED
            
        if teste[i] in letra and teste[i+1]=='(':
            entradaLb.delete(0,END)
            entradaLb.focus_set()
            messagebox.showinfo("", "Fórmula mal formada: letra logo antes de '('")
            botaoGerar['state']=DISABLED
            
        if teste[i] =='(' and teste[i+1]=='>':
            entradaLb.delete(0,END)
            entradaLb.focus_set()
            messagebox.showinfo("", "Fórmula mal formada: '(' logo antes de '>'")
            botaoGerar['state']=DISABLED
            
        if teste[i] =='>' and teste[i+1]=='>':
            entradaLb.delete(0,END)
            entradaLb.focus_set()
            messagebox.showinfo("", "Fórmula mal formada: duas '>' juntas")
            botaoGerar['state']=DISABLED

    
    
def list2string(lista): 
    texto=''
    for el in lista:
        for ele in el:
            texto+=' '
            texto+=ele
        texto+=','
    novo=''
    for i in range (0,len(texto)-1): #retira ultima virgula
        novo+=texto[i] 
    return novo


def controle(teste):#função principal de controle da aplicação
    global botaoGerar
    var=StringVar()
    
    lista = stringParser(teste)
    
    listaderamos = []
    listaderamos += [[["V",lista[0][0]],["F",lista[0][-1]]]]
    
    percorrerlista(listaderamos)
    
    contraex = encontracontraex(listaderamos)
    
    contra=list2string(contraex)
    var.set(contra)
    
    
    #controla exibicao na janela
    if contraex!=[]:
        lbC1=Label(root,text="Fórmula Falsificavel. Contra exemplo:",width=40,anchor="nw")
        lbC1.place(x=10,y=310)
        lbC2=Label(root,textvariable=var,width=20,anchor='nw')
        lbC2.place(x=10,y=330)
    else:
        lbD1=Label(root,text='Fórmula Válida!',width=40,anchor='nw')
        lbD1.place(x=10,y=310)
        lbD2=Label(root,text='',width=20,anchor='nw')
        lbD2.place(x=10,y=330)

    #desabilita botao gerador de tableuax -> preciso sempre validar a formula antes de gerar
    botaoGerar['state']=DISABLED


#----------Tratamento da Interface Gráfica-----------


#----Janela Principal---- OK!!!!

root=Tk()
root.geometry('400x400')
root.title("Tableaux Generator")


#---Label para inserir fórmula--- OK!!!!

lb=Label(root,text="Insira Fórmula:",width=12,anchor='nw',font="Helvetica 10 bold")
lb.place(x=150,y=10)
entradaLb=Entry(root,width=60)
entradaLb.place(x=10,y=40)
entradaLb.focus_set()

#-----Label para Informações--------
lbInf=Label(root,text='Informação Importante:',width=20,anchor='nw',font="Helvetica 10 bold")
lbInf.place(x=10,y=230)
lbInf2=Label(root,text='A fórmula a ser validada precisa estar integralmente de acordo ',width=50,anchor='nw')
lbInf2.place(x=10,y=250)
lbInf3=Label(root,text='com a formalização da lógica proposicional.',width=40,anchor='nw')
lbInf3.place(x=10,y=270)

#-------Label para resultado------ 0K!!!
lbRes=Label(root,text="Resultado do Tableaux:",width=20,anchor="nw",font="Helvetica 10 bold")
lbRes.place(x=10,y=290)


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
