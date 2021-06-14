import random
from tkinter import *
from random import *
import cadastro_perguntas


class Janela():
    def __init__(self, toplevel):
        self.toplevel = toplevel

        self.framePrinc = Frame(toplevel, relief=GROOVE)
        self.framePrinc.pack(pady=125, padx=125)  # frame principal

        self.label = Label(self.framePrinc, text='$how do Milhão', font=('Verdana', '24', 'bold'))
        self.label.pack(anchor=N, pady=10)

        self.framePicture = Frame(self.framePrinc)
        self.framePicture.pack(pady=10, side=LEFT)

        self.frameBotao = Frame(self.framePrinc)
        self.frameBotao.pack()

        self.botao_jogar = Button(self.frameBotao, text='Jogar', command=self.jogar_perguntas(), font='bold', bg="gold")
        self.botao_jogar.pack(anchor=N)

        self.botao_cadastrar = Button(
            self.frameBotao, text='Cadastrar Perguntas', command=self.regista_pergunta(), bg="medium sea green")
        self.botao_cadastrar.pack(anchor=N)

    def regista_pergunta(self):
        self.toplevel.destroy()
        raiz = Tk(className='Cadastrar Perguntas')
        cadastrar = cadastro_perguntas.PerguntaCadastro()
        cadastrar(raiz)
        raiz.mainloop()

    def jogar_perguntas(self):  # Inicia o jogo com as perguntas que voce cadastrou
        self.toplevel.destroy()
        raiz = Tk(className='Show Do Milhão')
        Jogo(raiz)
        raiz.mainloop()


class Jogo:
    def __init__(self, toplevel, nivel):

        self.toplevel = toplevel

        self.frameError = Frame(toplevel)
        self.frameError.pack(pady=50, padx=80)

        with open('jogador.txt', 'r') as jogador:
            usuario = jogador.readline()

        self.framePrinc = Frame(toplevel)
        self.framePrinc.pack(pady=40, padx=40)

        self.labelMoney = Label(self.framePrinc, text='MONEY')
        self.labelMoney.pack(side=RIGHT, anchor=N)

        self.labelPlayer = Label(self.framePrinc, text=usuario)
        self.labelPlayer.pack(side=RIGHT, anchor=NW)

        self.frameAjuste = Frame(self.framePrinc)
        self.frameAjuste.pack(side=BOTTOM, pady=20)

        self.pergunta()


raiz = Tk(className='Painel Principal')
janus = Janela(raiz)
raiz.mainloop()
