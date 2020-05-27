from objects_glac import *

class OthersWindows(Objects_Glac):
    def busca_cliente(self):
        self.listacliente = Toplevel()
        self.listacliente.title("  GLAC  ")
        self.listacliente.configure(background=self.fundo_da_tela)
        self.listacliente.geometry("342x390")
        self.listacliente.resizable(FALSE, FALSE)
        self.listacliente.transient(self.janela)
        self.listacliente.focus_force()
        self.listacliente.grab_set()

        frame1 = Frame(self.listacliente, bg = self.fundo_do_frame)
        frame1.place(relx=0.02, rely=0.01, relwidth = 0.96, relheight =0.97)

        self.LabelCliente = Label(self.listacliente, bd=0, fg = 'gray35', bg =self.fundo_do_frame,
                                  text= self.m_BuscaCliMsg1,
                                  font=('Verdana', '8', 'bold'))
        self.LabelCliente.place(relx=0.04, rely=0.01, relwidth = 0.9, relheight =0.06)
        self.LabelCliente2 = Label(self.listacliente, bd=0, fg = 'gray35', bg =self.fundo_do_frame,
                                  text= self.m_BuscaCliMsg2,
                                  font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(relx=0.04, rely=0.05, relwidth = 0.9, relheight =0.05)

        self.LabelCliente2 = Label(self.listacliente, bd=0, fg='gray35', bg=self.fundo_do_frame, text= self.m_Pesquisa
                                   + self.m_Pontinhos, font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(x=10, y=46)

        self.EntryCliente2 = Entry(self.listacliente, bd=1, fg='brown', bg='gray90', font=('Verdana', '8'))
        self.EntryCliente2.place(x=80, y=45)

        self.ButtonCliente2 = Button(self.listacliente, bd=2, text= self.m_Buscar,bg = '#178bca', fg ='white',
                                     font=('Verdana', '8', 'bold'), command = self.buscaCli)
        self.ButtonCliente2.place(x=240, y=43)


        self.listaServ = ttk.Treeview(self.listacliente, height=12, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text= self.m_Codigo)
        self.listaServ.heading("#2", text= self.m_Nome)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=50)
        self.listaServ.column("#2", width=250)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listacliente, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=310, y=70, width=25, height=265)

        self.listaServ.place(x=7, y=70)

        self.listaServ.bind("<Double-1>", self.carrega_cliente2)

        self.ButtonClienteNovo = Button(self.listacliente, bd=2, bg = '#178bca', fg ='white', text="Novo",
                                   font=('Verdana', '8', 'bold'), command = self.cadcli)
        self.ButtonClienteNovo.place(x=10, y=350)

        self.LabelCliente2 = Label(self.listacliente, bd=0, fg = 'gray35', bg =self.fundo_do_frame,
                                   text= self.m_BuscaCliMsg3,
                                   font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(relx=0.2, rely=0.88, relwidth = 0.75, relheight =0.05)
        self.LabelCliente2 = Label(self.listacliente, bd=0, fg = 'gray35', bg =self.fundo_do_frame,
                                   text= self.m_BuscaCliMsg4, font=('Verdana', '8', 'bold'))
        self.LabelCliente2.place(relx=0.2, rely=0.93, relwidth = 0.75, relheight =0.05)

        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        nome = self.listNome.get()
        nomecod = cursor

        lista = cursor.execute("""SELECT cod_cli, nome FROM clientes """ )
        rows = cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
        conn.close()


        def busca_cliente_a(event):
            busca_cliente()
    def busca_servico(self):
        ### Widgets - Listar Produtos e Serviços ###
        self.listaServP1 = Toplevel(); self.listaServP1.title(self.m_PesquisaServProd)
        self.listaServP1.geometry("950x280"); self.listaServP1.configure(background= self.fg_label)
        self.listaServP1.resizable(FALSE, FALSE)
        self.listaServP1.transient(self.janela)
        self.listaServP1.focus_force()
        self.listaServP1.grab_set()

        self.barra12 = Scrollbar(self.listaServP1, orient='vertical', command=self.OnVsb_S1)
        self.barra12.place(x=920, y=41, width=25, height=226)

        self.listaServ1 = ttk.Treeview(self.listaServP1, height=10, yscrollcommand=self.barra12.set,
                                       column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))

        self.listaServ1.heading("#0", text=""); self.listaServ1.column("#0", width=0)
        self.listaServ1.heading("#1", text= self.m_Codigo);
        self.listaServ1.column("#1", width=45)
        self.listaServ1.heading("#2", text= self.m_Serviços + self.m_barra + self.m_Produtos);
        self.listaServ1.column("#2", width=250)
        self.listaServ1.heading("#3", text= self.m_Tipo);
        self.listaServ1.column("#3", width=120)
        self.listaServ1.heading("#4", text= self.m_Quant);
        self.listaServ1.column("#4", width=50)
        self.listaServ1.heading("#5", text= self.m_Marca);
        self.listaServ1.column("#5", width=90)
        self.listaServ1.heading("#6", text= self.m_Automovel);
        self.listaServ1.column("#6", width=140)
        self.listaServ1.heading("#7", text= self.m_Sistema);
        self.listaServ1.column("#7", width=140)
        self.listaServ1.heading("#8", text= self.m_Valor);
        self.listaServ1.column("#8", width=70)

        self.listaServ1.place(x=15, y=40); self.listaServ1.configure(yscroll=self.barra12.set)
        self.listaServ1.delete(*self.listaServ1.get_children())

        self.descrCod_cli=Label(self.listaServP1,text=self.m_Pesquisa+self.m_Pontinhos, fg= self.fg_label,
                bg= self.bg_label, font=('Verdana', '8', 'bold')).place(x=20, y=7, height = 30)
        self.listaServicos1 = Entry(self.listaServP1, width=20, justify='right', bd=3, fg='brown', font=('Verdana', '12', 'bold'))
        self.listaServicos1.place(x=120, y=7, height = 30)

        self.botaoBuscaServicos1 = Button(self.listaServP1, text= self.m_BuscaServProd, bd=2, bg ='#178bca', fg ='white',
                                          font=('Verdana', '9', 'bold'), command=self.busca_serv)
        self.botaoBuscaServicos1.place(x=350, y=7, width=200, height = 30)

        self.botaoBuscaServicos2 = Button(self.listaServP1, text= self.m_BuscaVeiculos, bd=2, bg ='#178bca', fg ='white',
                                          font=('Verdana', '9', 'bold'), command=self.busca_serv_veic)
        self.botaoBuscaServicos2.place(x=570, y=7, width=120, height = 30)
        servprod = self.listaServicos1.get()

        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        cursor.execute(
            """SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, sistemaserv, valor * hor
            FROM servprod ORDER BY cod_sp ASC""")
        buscaservico12 = cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)
        conn.close()
    def busca_tecnico(self):
        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()
        ### Widgets - Listar tecnicos ###
        self.entradaTecnico.delete(0, END)
        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("360x160")
        self.listatec.resizable(TRUE, TRUE)
        self.listatec.transient(self.janela)
        self.listatec.focus_force()
        self.listatec.grab_set()

        self.listaServ = ttk.Treeview(self.listatec, height=6, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text= self.m_Codigo)
        self.listaServ.heading("#2", text= self.m_Tecnico)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=280)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listatec, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=325, y=5, width=30, height=145)

        self.listaServ.place(x=5, y=5)

        lista = cursor.execute("""
                SELECT cod, tecnico FROM tecnico ORDER BY cod ASC;
                """)
        rows = cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        # Binding da listbox
        self.listaServ.bind('<Double-1>', self.add_tecnicobind)
        conn.close()
    def busca_orc(self):
        ### Widgets - Listar Orçamentos ###
        self.listaOrc = Toplevel(); self.listaOrc.title(" GLAC  ");self.listaOrc.configure(background= self.fg_label, bd=6)
        self.listaOrc.geometry("640x360"); self.listaOrc.resizable(FALSE, FALSE)
        self.listaOrc.transient(self.janela)
        self.listaOrc.focus_force()
        self.listaOrc.grab_set()

        self.cliente_canvas2=Canvas(self.listaOrc,width=600,height=60,cursor='X_cursor',bg= self.fundo_do_frame,
            highlightbackground = self.borda_frame, highlightthickness = 3); self.cliente_canvas2.place(x=10, y=1)

        self.listaNomeO = Entry(self.listaOrc, width=20, justify='right', bd=2, fg=self.fg_entry, bg = self.bg_entry,
            font=('Verdana', '12', 'bold')); self.listaNomeO.place(x=140, y=7)

        self.botaoBuscaNome=Button(self.listaOrc,text=self.m_Buscar + " " + self.m_Nome, bd=1,bg=self.bg_button,
            fg = 'white', font=('verdana', '10', 'bold'), command=self.buscanomeorc)
        self.botaoBuscaNome.place(x=370, y=6, width=110, height = 25)

        self.listaPlaca = Entry(self.listaOrc, width=20, justify='right', bd=2, fg= self.fg_entry, bg= self.bg_entry,
            font=('Verdana', '12', 'bold'));self.listaPlaca.place(x=140, y=37)

        self.botaoBuscaPlaca = Button(self.listaOrc, text= self.m_Buscar + ' ' +self.m_Placa,bd=1,bg=self.bg_button,
                                      fg='white', font=('Verdana', '10', 'bold'), command=self.buscaplacaorc)
        self.botaoBuscaPlaca.place(x=370, y=36, width=110, height = 25)

        conn = sqlite3.connect("glac.db")
        cursor = conn.cursor()

        ### Widgets - Listar veiculos ###

        self.listaServ = ttk.Treeview(self.listaOrc, height=12,
                                      column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text= self.m_Orcamento)
        self.listaServ.heading("#2", text= self.m_Nome)
        self.listaServ.heading("#3", text= self.m_Dia)
        self.listaServ.heading("#4", text= self.m_Mes)
        self.listaServ.heading("#5", text= self.m_Ano)
        self.listaServ.heading("#6", text= self.m_Placa)
        self.listaServ.heading("#7", text= self.m_Tipo)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=200)
        self.listaServ.column("#3", width=35)
        self.listaServ.column("#4", width=35)
        self.listaServ.column("#5", width=55)
        self.listaServ.column("#6", width=80)
        self.listaServ.column("#7", width=137)
        # Cria barra de rolagem
        self.barra = Scrollbar(self.listaOrc, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=595, y=70, width=30, height=270)

        self.listaServ.place(x=10, y=70)

        self.listaServ.bind("<Double-1>", self.carrega_orc)

        lista = cursor.execute("""
                SELECT id_orc1, clientes.nome, dia , mes , ano, placa_orc, tipoOrc FROM orcamento1, clientes WHERE cod_cli =
                cliente_orc ORDER BY id_orc1 DESC;
                """)
        rows = cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        # self.listaO.delete(0, END)
        conn.close()

        def busca_orc_a(event):
            busca_orc()
    def busca_falha(self):
        ### Widgets - Listar Produtos e Serviços ###
        self.conecta_Glac()
        self.listaServP1F = Tk(); self.listaServP1F.title(self.m_Pesquisa)
        self.listaServP1F.geometry("890x280"); self.listaServP1F.resizable(FALSE, FALSE)
        self.listaServP1F.configure(background=self.bg_label)

        self.barra12F = Scrollbar(self.listaServP1F, orient='vertical', command=self.OnVsb_S1F)
        self.barra12F.place(x=850, y=47, width=25, height=230)

        self.listaServ1F = ttk.Treeview(self.listaServP1F, height=10, yscrollcommand=self.barra12F.set,
                                        column=("col1", "col2", "col3"))
        self.listaServ1F.heading("#0", text="")
        self.listaServ1F.heading("#1", text= self.m_Codigo)
        self.listaServ1F.heading("#2", text= self.m_Falhas)
        self.listaServ1F.heading("#3", text= self.m_Obs)

        self.listaServ1F.column("#0", width=0)
        self.listaServ1F.column("#1", width=80)
        self.listaServ1F.column("#2", width=395)
        self.listaServ1F.column("#3", width=350)
        self.listaServ1F.place(x=15, y=40)
        self.listaServ1F.configure(yscroll=self.barra12F.set)
        self.listaServ1F.delete(*self.listaServ1F.get_children())
        self.descrCod_cliF = Label(self.listaServP1F, text= self.m_Pesquisa, fg= self.fg_label, bg= self.bg_label,
                                   font=('Verdana', '8', 'bold'))
        self.descrCod_cliF.place(x=35, y=7)
        self.listaServicos1F = Entry(self.listaServP1F, width=20, justify='right', bd=3, fg='brown',
                                     font=('Verdana', '12', 'bold'))
        self.listaServicos1F.place(x=120, y=7)

        self.botaoBuscaServicos1F = Button(self.listaServP1F, text= self.m_Buscar, bd=3, bg = self.bg_button,
                fg ='white', font=('Verdana', '7', 'bold'), command=self.busca_servF)
        self.botaoBuscaServicos1F.place(x=350, y=7, width=110)
        servprodF = self.listaServicos1F.get()
        self.cursor.execute(
            """SELECT cod_falha, falha, falha2 FROM codfalha ORDER BY cod_falha ASC""")
        buscaservico12F = self.cursor.fetchall()
        for i in buscaservico12F:
            self.listaServ1F.insert("", END, values=i)
        self.desconecta_Glac()
    def calendarioInicio(self):
        self.multiGlacx()
        self.cores();

        self.calendario1 = Calendar(self.top3, fg='gray75', bg=self.fundo_da_tela,
                                    font=('Times', '9', 'bold'),  locale = 'pt_br')
        self.calendario1.place(x=50, y=30)

        self.calDataInicio = Button(self.top3, text='Inserir data inicial', command=self.print_calInicio,
                                      fg='gray35', font=('Times', '10', 'bold'))

        self.calDataInicio.place(x=50, y=215, height=25, width = 200)
    def print_calInicio(self):
        dataInicio = self.calendario1.get_date()
        self.calendario1.destroy()
        self.listInicio.delete(0, END)
        self.listInicio.insert(END, dataInicio)
        self.calDataInicio.destroy()
    def calendarioFim(self):
        self.multiGlacx()
        self.cores();

        self.calendario2 = Calendar(self.top3, text=self.m_Estab, fg='gray75', bg=self.fundo_da_tela, locale = 'pt_br',
                                   font=('Times', '9', 'bold'))
        self.calendario2.place(x=50, y=40)

        self.calDataFim = Button(self.top3, text='Inserir data final', command=self.print_calFim,
                                 fg='gray35', font=('Times', '10', 'bold'))
        self.calDataFim.place(x=50, y=225, height=25, width = 200)
    def print_calFim(self):
        dataFim = self.calendario2.get_date()
        self.listFim.delete(0, END)
        self.listFim.insert(END, dataFim)
        self.calendario2.destroy()
        self.calDataFim.destroy()
