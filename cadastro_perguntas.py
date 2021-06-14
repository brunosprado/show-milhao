from tkinter import *


class PerguntaCadastro():

    def __init__(self, toplevel):

        self.toplevel = toplevel
        self.framePrinc = toplevel
        self.label = Label(self.framePrinc, text='$how do Milhão', font=('Verdana', '36', 'bold'))
        self.label.pack(anchor=N, pady=10)
        self.framePerg = Frame(self.framePrinc)
        self.framePerg.pack(padx=10, pady=10)
        self.labelPerg = Label(self.framePerg, text='Pergunta', font=('Arial', '18', 'bold'))
        self.labelPerg.pack(anchor=N, pady=10)
        self.EntradaPerg = Entry(self.framePerg)
        self.EntradaPerg.pack(side=LEFT)
        self.EntradaPerg.focus()
        self.frameList = Frame(self.framePrinc)
        self.frameList.pack(side=RIGHT)
        self.frameList.scrollarea = (10, 10, 10, 10)
        self.valorRadio = IntVar()

        for index in range(1, 5):

            self.frameEntrada = Frame(self.framePrinc)
            self.frameEntrada.pack()
            self.labelEntrada = Label(self.frameEntrada, text='Resposta %i' % index)
            self.labelEntrada.pack(side=LEFT, anchor=SW)

            if index == 1:
                self.Entrada1 = Entry(self.frameEntrada)
                self.Entrada1.pack(side=LEFT, anchor=W)
                self.radioButton1 = Radiobutton(self.frameEntrada, value=1, variable=self.valorRadio)
                self.radioButton1.pack(side=LEFT)

            if index == 2:
                self.Entrada2 = Entry(self.frameEntrada)
                self.Entrada2.pack(side=LEFT, anchor=W)
                self.radioButton2 = Radiobutton(self.frameEntrada, value=2, variable=self.valorRadio)
                self.radioButton2.pack(side=LEFT)
            if index == 3:
                self.Entrada3 = Entry(self.frameEntrada)
                self.Entrada3.pack(side=LEFT, anchor=W)
                self.radioButton3 = Radiobutton(self.frameEntrada, value=3, variable=self.valorRadio)
                self.radioButton3.pack(side=LEFT)
            if index == 4:
                self.Entrada4 = Entry(self.frameEntrada)
                self.Entrada4.pack(side=LEFT, anchor=W)
                self.radioButton4 = Radiobutton(self.frameEntrada, value=4, variable=self.valorRadio)
                self.radioButton4.pack(side=LEFT)

        self.valorRadio.set(1)
        self.labelExplicativa = Label(self.framePrinc, text='Marque a opção correta')
        self.labelExplicativa.pack()
        self.frameButton = Frame(self.framePrinc)
        self.frameButton.pack(anchor=S)
        self.buttonEnviar = Button(self.frameButton, text='Enviar', command=self.registro)
        self.buttonEnviar.pack(side=LEFT)
        self.buttonVoltar = Button(self.frameButton, text='Voltar', command=self.voltar)
        self.buttonVoltar.pack(side=LEFT)

    def voltar(self):
        self.toplevel.destroy()

    def registro(self):
        pergunta = self.EntradaPerg.get()
        resposta_correta = self.valorRadio.get()
        resposta_1 = self.Entrada1.get()
        resposta_2 = self.Entrada2.get()
        resposta_3 = self.Entrada3.get()
        resposta_4 = self.Entrada4.get()

        if resposta_1 != '':
            if resposta_2 != '':
                if resposta_3 != '':
                    if resposta_4 != '':
                        if pergunta != '':
                            with open('perguntas.txt', 'w') as arquivo:
                                arquivo.write(f'P{pergunta}\n')
                                if resposta_correta == 1:
                                    arquivo.write(f'RC{resposta_1}\n')
                                    arquivo.write(f'RE{resposta_2}\n')
                                    arquivo.write(f'RE{resposta_3}\n')
                                    arquivo.write(f'RE{resposta_4}\n')
                                if resposta_correta == 2:
                                    arquivo.write(f'RE{resposta_1}\n')
                                    arquivo.write(f'RC{resposta_2}\n')
                                    arquivo.write(f'RE{resposta_3}\n')
                                    arquivo.write(f'RE{resposta_4}\n')
                                if resposta_correta == 3:
                                    arquivo.write(f'RE{resposta_1}\n')
                                    arquivo.write(f'RE{resposta_2}\n')
                                    arquivo.write(f'RC{resposta_3}\n')
                                    arquivo.write(f'RE{resposta_4}\n')
                                if resposta_correta == 4:
                                    arquivo.write(f'RE{resposta_1}\n')
                                    arquivo.write(f'RE{resposta_2}\n')
                                    arquivo.write(f'RE{resposta_3}\n')
                                    arquivo.write(f'RC{resposta_4}\n')

                            self.buttonEnviar.destroy()
                            self.buttonVoltar.destroy()
                            self.label2 = Label(self.frameButton, text='Deseja Cadastrar Mais Perguntas')
                            self.label2.pack()
                            self.button = Button(self.frameButton, text='Sim', command=self.de_novo)
                            self.button.pack(side=LEFT)
                            self.button = Button(self.frameButton, text='Não', command=self.voltar)
                            self.button.pack(side=LEFT)

    def de_novo(self):
        self.toplevel.destroy()
        raiz = Tk(className='Cadrastro de perguntas')
        PerguntaCadastro(raiz)
        raiz.mainloop()

    def preencha(self, n):
        self.toplevel = Tk(className='Inválido')
        self.container = Frame(self.toplevel)
        self.container.pack()

        if n == 0:
            self.outraLabel = Label(self.container, text='Preencha Todos Os Campos')
            self.outraLabel.pack(padx=50, pady=50)
            self.outraLabel.focus()

        self.botao = Button(self.container, text='OK', command=self.destroy)
        self.botao.pack()

    def destroy(self):
        self.toplevel.destroy()


raiz = Tk(className='Cadrastro de perguntas')
PerguntaCadastro(raiz)
raiz.mainloop()
