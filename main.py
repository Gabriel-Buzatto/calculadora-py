# importando tkinter

from tkinter import *
from tkinter import ttk

# cores

cor1 = '#403938'
cor2 = '#fafafa'
cor3 = '#0c394d'
cor4 = '#98acb5'
cor5 = '#fc6900'

# janela

janela =Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=cor1)

# frames

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# variável todos valores

todos_valores = ''

# label

valor_texto = StringVar()

# funções

def valor_entrada(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    
    # passar o valor pra tela
    valor_texto.set(todos_valores)

# função para calcular
    
def calcular():

    global todos_valores

    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# função para limpar a tela
    
def limpar_tela():

    global todos_valores

    todos_valores = ''
    valor_texto.set('')


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# botões

b_1 = Button(frame_corpo, text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command= limpar_tela)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text='%', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('%'))
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, text='/', width=5, height=2, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('/'))
b_3.place(x=177, y=0)


b_4 = Button(frame_corpo, text='7', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('7'))
b_4.place(x=0, y=52)

b_5 = Button(frame_corpo, text='8', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('8'))
b_5.place(x=59, y=52)

b_6 = Button(frame_corpo, text='9', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('9'))
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo, text='*', width=5, height=2, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('*'))
b_7.place(x=177, y=52)


b_8 = Button(frame_corpo, text='4', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('4'))
b_8.place(x=0, y=104)

b_9 = Button(frame_corpo, text='5', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('5'))
b_9.place(x=59, y=104)

b_10 = Button(frame_corpo, text='6', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('6'))
b_10.place(x=118, y=104)

b_11 = Button(frame_corpo, text='-', width=5, height=2, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('-'))
b_11.place(x=177, y=104)


b_12 = Button(frame_corpo, text='1', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('1'))
b_12.place(x=0, y=156)

b_13 = Button(frame_corpo, text='2', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('2'))
b_13.place(x=59, y=156)

b_14 = Button(frame_corpo, text='3', width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('3'))
b_14.place(x=118, y=156)

b_15 = Button(frame_corpo, text='+', width=5, height=2, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('+'))
b_15.place(x=177, y=156)


b_16 = Button(frame_corpo, text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('0'))
b_16.place(x=0, y=208)

b_17 = Button(frame_corpo, text='.', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: valor_entrada('.'))
b_17.place(x=118, y=208)

b_18 = Button(frame_corpo, text='=', width=5, height=2, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = calcular)
b_18.place(x=177, y=208)


janela.mainloop()