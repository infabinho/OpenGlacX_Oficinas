from objects_glac import *

class Financeiro(Objects_Glac):
    def cadfinan(self):
        self.multiGlacx()
        self.cores()

        self.janelaFin = Toplevel()
        self.janelaFin.configure(background=self.fundo_da_tela)
        self.janelaFin.title(self.m_Financeiro)
        self.janelaFin.geometry("800x385")
        self.janelaFin.resizable(FALSE, FALSE)
        self.janelaFin.transient(self.janela)
        self.janelaFin.focus_force()
        self.janelaFin.grab_set()

        self.vcmd6 = (self.janelaFin.register(self.validate_entry6), "%P")
        self.vcmd4 = (self.janelaFin.register(self.validate_entry4), "%P")
        self.vcmd2 = (self.janelaFin.register(self.validate_entry2), "%P")
        self.vcmd8float = (self.janelaFin.register(self.validate_entry8float), "%P")

        ###  A B A S

        self.abas = Notebook(self.janelaFin)
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba2 = Frame(self.abas)

        self.frame_aba1.configure(background='gray75')
        self.frame_aba2.configure(background='lightgray')

        self.label1 = Label(self.frame_aba1)
        self.label1.pack(padx=385, pady=160)
        self.label2 = Label(self.frame_aba2)
        self.label2.pack(padx=385, pady=160)

        self.abas.add(self.frame_aba1, text=self.m_Receitas)

        self.abas.place(x=10, y=5)

        ####################################################################
        ####  Descrição dos problemas apresentados pelo veiculo - Aba 1
        ####################################################################
        self.frameProb = Frame(self.frame_aba1, width=755, height=320, bd=4, relief=SUNKEN)
        self.frameProb.place(x=10, y=10)


        self.descrCodprod = Label(self.frame_aba1, text='Ano...........', font=('Verdana', '8', 'bold'))
        self.descrCodprod.place(x=14, y=15, width=90)
        self.entradaCodprod = Entry(self.frame_aba1, bd=3, width=4, fg='brown', validate="key",
                                    validatecommand=self.vcmd4, font=('Verdana', '8', 'bold'))
        self.entradaCodprod.place(x=75, y=18)

        self.descrProd = Label(self.frame_aba1, text='Mês...........', font=('Verdana', '8', 'bold'))
        self.descrProd.place(x=14, y=43, width=90)
        self.entradaProd = Entry(self.frame_aba1, width=2, fg='brown', validate="key", validatecommand=self.vcmd2,
                                 bd=3, font=('Verdana', '8', 'bold'))
        self.entradaProd.place(x=75, y=43)

        ###  Botao Carrega
        self.botaoAdd = Button(self.frame_aba1, text=self.m_Carregar, bd=1, command= self.carrega_produto,
                               bg='#6d6789', fg='white', font=('Verdana', '8', 'bold'))
        self.botaoAdd.place(x=25, y=73, width=110, height=25)
        ###  Botao limpa
        self.botaolimpa = Button(self.frame_aba1, text=self.m_Limpar, bd=1, command= self.limpa_produto,
                                 bg='#6d6789', fg='white', font=('Verdana', '8', 'bold'))
        self.botaolimpa.place(x=25, y=103, width=110, height=25)

        ### Widgets - Listar produtos ###
        self.frameProb2 = Frame(self.frame_aba1, bg='gray70', width=565, height=240, bd=4, relief=SUNKEN)
        self.frameProb2.place(x=190, y=13)

        self.listaServ = ttk.Treeview(self.frame_aba1, height=10,
                                      column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Placa)
        self.listaServ.heading("#3", text=self.m_Dia)
        self.listaServ.heading("#4", text=self.m_Mes)
        self.listaServ.heading("#5", text=self.m_Ano)
        self.listaServ.heading("#6", text="")
        self.listaServ.heading("#7", text=self.m_Valor_R)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=60)
        self.listaServ.column("#2", width=150)
        self.listaServ.column("#3", width=55)
        self.listaServ.column("#4", width=55)
        self.listaServ.column("#5", width=75)
        self.listaServ.column("#6", width=20)
        self.listaServ.column("#7", width=100)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.frame_aba1, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=718, y=17, width=28, height=228)
        self.listaServ.place(x=200, y=18)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickFinan)

        ### Widgets - Listar produtos ###

        self.listaServ2 = ttk.Treeview(self.frame_aba1, height=1,
                                       column=("col1", "col2", "col3"))
        self.listaServ2.heading("#0", text="")
        self.listaServ2.heading("#1", text=self.m_Ano)
        self.listaServ2.heading("#2", text=self.m_Mes)
        self.listaServ2.heading("#3", text=self.m_Total)

        self.listaServ2.column("#0", width=0)
        self.listaServ2.column("#1", width=60)
        self.listaServ2.column("#2", width=60)
        self.listaServ2.column("#3", width=100)

        self.listaServ2.place(x=320, y=270)
        self.janelaFin.mainloop()
    def OnDoubleClickFinan(self, event):
        self.limpa_produto()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)

            self.carrega_produto()
    def carrega_produto(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        self.listaServ2.delete(*self.listaServ2.get_children())

        ano = self.entradaCodprod.get()
        mes = self.entradaProd.get()

        lista = self.cursor.execute("""select id_orc1, placa_orc, dia, mes, ano, "R$",
            trim(replace(totalizador, ',', '.'),'R$') from orcamento1 where ano = '%s'
            and mes = '%s' and tipoOrc != 'Orçamento' order by dia asc;	""" % (ano, mes))

        for i in lista:
            print(i)
            self.listaServ.insert("", END, values=i)

        lista2 = self.cursor.execute("""select ano, mes, sum(trim(replace(totalizador, ',', '.'),'R$'))
                                    from orcamento1
                               		where ano = '%s' and mes = '%s'  and tipoOrc != 'Orçamento';
                               		""" % (ano, mes))
        for i in lista2:
            print(i)
            self.listaServ2.insert("", END, values=i)

        def carrega_produto_a(event):
            carrega_produto()

        self.desconecta_Glac()
    def limpa_produto(self):
        self.entradaProd.delete(0, END)
        self.entradaCodprod.delete(0, END)

        def limpa_produto_a(event):
            limpa_produto()
