from objects_glac import *

class Estoque(Objects_Glac):
    def cadest(self):
        self.multiGlacx()
        self.cores()
        self.janelaEst = Toplevel()
        self.janelaEst.title(self.m_Estoque)
        self.janelaEst.configure(background=self.fundo_da_tela)
        self.janelaEst.geometry("800x405")
        self.janelaEst.resizable(FALSE, FALSE)
        self.janelaEst.minsize(width=780, height=450)
        self.janelaEst.transient(self.janela)
        self.janelaEst.focus_force()
        self.janelaEst.grab_set()

        self.conecta_Glac()

        self.descrNomeServ = Label(self.janelaEst, text=self.m_ControleEstoque, bg=self.fundo_da_tela, fg='gray75',
                                   font=('Comic', '18', 'bold'))
        self.descrNomeServ.place(x=245, y=1)

        self.vcmd6 = (self.janelaEst.register(self.validate_entry6), "%P")
        self.vcmd4 = (self.janelaEst.register(self.validate_entry4), "%P")
        self.vcmd2 = (self.janelaEst.register(self.validate_entry2), "%P")
        self.vcmd8float = (self.janelaEst.register(self.validate_entry8float), "%P")

        ###  A B A S

        self.abas = Notebook(self.janelaEst)
        self.frame_aba1 = Frame(self.abas)
        self.frame_aba2 = Frame(self.abas)
        self.frame_aba3 = Frame(self.abas)
        self.frame_aba4 = Frame(self.abas)

        self.frame_aba3.configure(background='lightgray')
        self.frame_aba1.configure(background='lightgray')
        self.frame_aba2.configure(background='lightgray')
        self.frame_aba4.configure(background='lightgray')

        self.label1 = Label(self.frame_aba1)
        self.label1.pack(padx=385, pady=160)
        self.label2 = Label(self.frame_aba2)
        self.label2.pack(padx=385, pady=160)
        self.label3 = Label(self.frame_aba3)
        self.label3.pack(padx=385, pady=160)
        self.label4 = Label(self.frame_aba4)
        self.label4.pack(padx=385, pady=160)

        self.abas.add(self.frame_aba1, text=self.m_Cadastro + ' ' + self.m_Produtos)
        self.abas.add(self.frame_aba2, text=self.m_MovimentaEst)

        self.abas.place(x=10, y=30)

        ####################################################################
        ####  Descrição dos problemas apresentados pelo veiculo - Aba 1
        ####################################################################
        self.frameProb = Frame(self.frame_aba1, width=755, height=260, bd=4, relief=SUNKEN)
        self.frameProb.place(x=10, y=10)

        self.descrCodprod = Label(self.frame_aba1, text=self.m_Codigo, font=('Verdana', '8', 'bold'))
        self.descrCodprod.place(x=14, y=15)
        self.entradaCodprod = Entry(self.frame_aba1, width=6, fg='brown', validate="key",
                                    validatecommand=self.vcmd6,
                                    font=('Verdana', '8', 'bold'))
        self.entradaCodprod.place(x=75, y=18)

        ###  Botao Carrega
        self.botaoAdd = Button(self.frame_aba1, text=self.m_Carregar + ' ' + self.m_Produtos, bd=3,
                               fg='darkblue', command=self.carrega_produtoE,
                               font=('Verdana', '7', 'bold'))
        self.botaoAdd.place(x=135, y=17, width=100)
        ###  Botao limpa
        self.botaolimpa = Button(self.frame_aba1, text=self.m_Limpar, bd=3, fg='darkblue',
                                 command=self.limpa_produtoE,
                                 font=('Verdana', '8', 'bold'))
        self.botaolimpa.place(x=275, y=17, width=60, height=22)

        self.descrProd = Label(self.frame_aba1, text=self.m_Produtos, font=('Verdana', '8', 'bold'))
        self.descrProd.place(x=14, y=43)
        self.entradaProd = Entry(self.frame_aba1, width=32, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaProd.place(x=75, y=43)

        ###  Botao busca automovel
        self.botaolimpa = Button(self.frame_aba1, text=self.m_Buscar, bd=3, fg='darkblue',
                                 command=self.busca_produtoE,
                                 font=('Verdana', '8', 'bold'))
        self.botaolimpa.place(x=275, y=40, width=60, height=24)

        self.descrIdMarcaprod = Button(self.frame_aba1, text=self.m_Marca, bg='gray75',
                                       font=('Verdana', '8', 'bold'),
                                       command=self.busca_marcaE)
        self.descrIdMarcaprod.place(x=14, y=65, width=63, height=23)
        self.entradaIdMarcaprod = Entry(self.frame_aba1, width=6)
        # entradaIdMarcaprod.place(x=75, y=63)
        self.entradaMarcaprod = Entry(self.frame_aba1, width=26, fg='brown', font=('Verdana', '8', 'bold'))
        self.entradaMarcaprod.place(x=76, y=68)

        self.descrIdFornec = Button(self.frame_aba1, text=self.m_Fornecedor, bg='gray75',
                                    font=('Verdana', '8', 'bold'),
                                    command=self.busca_fornecE)
        self.descrIdFornec.place(x=14, y=92, width=63, height=23)
        self.entradaIdFornec = Entry(self.frame_aba1, width=6)
        # entradaIdFornec.place(x=85, y=93)
        self.entradaFornec = Entry(self.frame_aba1, width=26, fg='brown', font=('Verdana', '8', 'bold'))
        self.entradaFornec.place(x=75, y=93)

        self.descrCusto = Label(self.frame_aba1, text=self.m_Custo_R, font=('Verdana', '8', 'bold'))
        self.descrCusto.place(x=14, y=122)
        self.entradaCusto = Entry(self.frame_aba1, width=8, fg='brown', font=('Verdana', '8', 'bold'),
                                  validate="key",
                                  validatecommand=self.vcmd8float)
        self.entradaCusto.place(x=75, y=123)

        self.descrValor = Label(self.frame_aba1, text=self.m_Valor_R, font=('Verdana', '8', 'bold'))
        self.descrValor.place(x=150, y=122)
        self.entradaValor = Entry(self.frame_aba1, width=8, fg='brown', font=('Verdana', '8', 'bold'),
                                  validate="key",
                                  validatecommand=self.vcmd8float)
        self.entradaValor.place(x=220, y=123)

        self.descrDescricao = Label(self.frame_aba1, text=self.m_Descricao, font=('Verdana', '9', 'bold'))
        self.descrDescricao.place(x=14, y=150)
        self.entradaDescricao = Entry(self.frame_aba1, width=36, fg='brown', font=('Verdana', '10', 'bold'))
        self.entradaDescricao.place(x=16, y=175)

        self.botaoAdd = Button(self.frame_aba1, text=self.m_Novo, command=self.add_produtoE, bd=3, fg='darkblue',
                               font=('Verdana', '10', 'bold'))
        self.botaoAdd.place(x=50, y=210, width=80)

        self.botaoMudServ = Button(self.frame_aba1, text=self.m_Alterar, command=self.mud_produtoE, bd=3, fg='darkblue',
                                   font=('Verdana', '10', 'bold'))
        self.botaoMudServ.place(x=150, y=210, width=80)

        self.botaoDel = Button(self.frame_aba1, text=self.m_Apagar, command=self.del_produtoE, bd=3, fg='brown',
                               font=('Verdana', '10', 'bold'))
        self.botaoDel.place(x=250, y=210, width=80)

        ### Widgets - Listar produtos ###

        self.listaServ = ttk.Treeview(self.frame_aba1, height=10,
                                      column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Produtos)
        self.listaServ.heading("#3", text="")
        self.listaServ.heading("#4", text=self.m_Custo_R)
        self.listaServ.heading("#5", text="")
        self.listaServ.heading("#6", text=self.m_Valor_R)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=39)
        self.listaServ.column("#2", width=180)
        self.listaServ.column("#3", width=25)
        self.listaServ.column("#4", width=65)
        self.listaServ.column("#5", width=25)
        self.listaServ.column("#6", width=65)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.frame_aba1, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=740, y=15, width=15, height=230)

        lista = self.cursor.execute("""
                            SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
                    	    WHERE sp = "P" ORDER BY servprod ASC ;
                            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=340, y=15)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickE)

        #####################################################################
        #### ABA 2
        #####################################################################
        ### Cabeçalho dos itens_orc 1 A 10 - Aba 2

        self.frameItens = Frame(self.frame_aba2, width=760, height=316, bd=4, bg='gray55')
        self.frameItens.place(x=10, y=8)

        self.frameItens = Frame(self.frame_aba2, width=750, height=307, bd=4, bg='lightgray', relief=SUNKEN)
        self.frameItens.place(x=15, y=15)
        ### Produto
        self.produto_aba2label = Label(self.frame_aba2, text=self.m_Produtos, fg='darkblue',
                                       font=('Verdana', '8', 'bold'), bg='lightgray')
        self.produto_aba2label.place(x=20, y=20)

        self.codproduto2 = Entry(self.frame_aba2)

        self.produto_aba2 = Entry(self.frame_aba2, bd=3, fg='brown', width='30', font=('Verdana', '8', 'bold'))
        self.produto_aba2.place(x=130, y=20)

        #### Entrada
        self.quant_aba2label = Label(self.frame_aba2, text=self.m_Entrada, fg='darkblue',
                                     font=('Verdana', '8', 'bold'), bg='lightgray')
        self.quant_aba2label.place(x=20, y=45)

        self.quant_aba2 = Entry(self.frame_aba2, bd=3, fg='brown', width='10', font=('Verdana', '8', 'bold'),
                                validate="key",
                                validatecommand=self.vcmd8float)
        self.quant_aba2.place(x=130, y=45)
        self.quant_aba2.insert(END, 0)

        #### Saida
        self.saida_aba2label = Label(self.frame_aba2, text=self.m_Saida, fg='darkblue',
                                     font=('Verdana', '8', 'bold'), bg='lightgray')
        self.saida_aba2label.place(x=20, y=70)

        self.saida_aba2 = Entry(self.frame_aba2, bd=3, fg='brown', width='10', font=('Verdana', '8', 'bold'),
                                validate="key",
                                validatecommand=self.vcmd8float)
        self.saida_aba2.place(x=130, y=70)
        self.saida_aba2.insert(END, 0)

        #### Custo
        self.custo_aba2label = Label(self.frame_aba2, text=self.m_Custo_R, fg='darkblue',
                                     font=('Verdana', '8', 'bold'), bg='lightgray')
        self.custo_aba2label.place(x=20, y=95)

        self.custo_aba2 = Entry(self.frame_aba2, bd=3, fg='brown', width='10', font=('Verdana', '8', 'bold'),
                                validate="key",
                                validatecommand=self.vcmd8float)
        self.custo_aba2.place(x=130, y=95)
        #### Data
        self.data_aba2label = Label(self.frame_aba2, text=self.m_Data + self.m_Pontinhos + self.m_Pontinhos +
                                                          self.m_DataMasc, fg='darkblue',
                                    font=('Verdana', '8', 'bold'), bg='lightgray')
        self.data_aba2label.place(x=20, y=120)

        self.dia_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='2', font=('Verdana', '8', 'bold'),
                              validate="key",
                              validatecommand=self.vcmd2)
        self.dia_aba2.place(x=130, y=120)

        self.mes_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='2', font=('Verdana', '8', 'bold'),
                              validate="key",
                              validatecommand=self.vcmd2)
        self.mes_aba2.place(x=155, y=120)

        self.ano_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='4', font=('Verdana', '8', 'bold'),
                              validate="key",
                              validatecommand=self.vcmd4)
        self.ano_aba2.place(x=185, y=120)
        #### Lote
        self.lote_aba2label = Label(self.frame_aba2, text=self.m_Lote, fg='darkblue',
                                    font=('Verdana', '8', 'bold'), bg='lightgray')
        self.lote_aba2label.place(x=20, y=145)

        self.lote_aba2 = Entry(self.frame_aba2, bd=3, fg='brown', width='20', font=('Verdana', '8', 'bold'))
        self.lote_aba2.place(x=130, y=145)
        self.lote_aba2.insert(END, 'xxx')
        #### Validade
        self.valid_aba2label = Label(self.frame_aba2, text=self.m_Validade, fg='darkblue',
                                     font=('Verdana', '8', 'bold'), bg='lightgray')
        self.valid_aba2label.place(x=20, y=170)

        self.diaV_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='2', font=('Verdana', '8', 'bold'),
                               validate="key", validatecommand=self.vcmd2)
        self.diaV_aba2.place(x=130, y=170)

        self.mesV_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='2', font=('Verdana', '8', 'bold'),
                               validate="key", validatecommand=self.vcmd2)
        self.mesV_aba2.place(x=155, y=170)

        self.anoV_aba2 = Entry(self.frame_aba2, bd=0, fg='brown', width='4', font=('Verdana', '8', 'bold')
                               , validate="key", validatecommand=self.vcmd4)
        self.anoV_aba2.place(x=185, y=170)

        self.darEntrada = Button(self.frame_aba2, text=self.m_InserirRegistro, command=self.add_movE)
        self.darEntrada.place(x=130, y=250)

        self.quantestlabel = Label(self.frame_aba2, text=self.m_Quant + ' ' + self.m_Estoque, fg='darkblue',
                                   font=('Verdana', '8', 'bold'), bg='lightgray')
        self.quantestlabel.place(x=430, y=300)

        self.quantest = Entry(self.frame_aba2, bd=0, fg='red', width='4', font=('Verdana', '9', 'bold'))
        self.quantest.place(x=630, y=300)

        ### Widgets - Listar produtos ###

        self.listaMov = ttk.Treeview(self.frame_aba2, height=10,
                                     column=(
                                         "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9",
                                         "col10",
                                         "col11"))
        self.listaMov.heading("#0", text="")
        self.listaMov.heading("#1", text=self.m_Lote)
        self.listaMov.heading("#2", text=self.m_Entrada)
        self.listaMov.heading("#3", text=self.m_Saida)
        self.listaMov.heading("#4", text=self.m_Custo_R)
        self.listaMov.heading("#5", text="")
        self.listaMov.heading("#6", text="")
        self.listaMov.heading("#7", text=self.m_Data)
        self.listaMov.heading("#8", text=self.m_Fornecedor)
        self.listaMov.heading("#9", text="")
        self.listaMov.heading("#10", text="")
        self.listaMov.heading("#11", text=self.m_Validade)

        self.listaMov.column("#0", width=0)
        self.listaMov.column("#1", width=50)
        self.listaMov.column("#2", width=50)
        self.listaMov.column("#3", width=50)
        self.listaMov.column("#4", width=50)
        self.listaMov.column("#5", width=15)
        self.listaMov.column("#6", width=15)
        self.listaMov.column("#7", width=35)
        self.listaMov.column("#8", width=80)
        self.listaMov.column("#9", width=15)
        self.listaMov.column("#10", width=15)
        self.listaMov.column("#11", width=70)

        # Cria barra de rolagem
        self.barraMov = Scrollbar(self.frame_aba2, orient='vertical', command=self.listaMov.yview)
        # Adiciona barra de rolagem
        self.listaMov.configure(yscroll=self.barraMov.set)
        self.barraMov.place(x=750, y=50, width=15, height=230)

        # Cria barra de rolagem
        self.barraMov2 = Scrollbar(self.frame_aba2, orient='horizontal', command=self.listaMov.xview)
        # Adiciona barra de rolagem
        self.listaMov.configure(xscroll=self.barraMov2.set)
        self.barraMov2.place(x=310, y=277, width=420, height=20)

        self.listaMov.place(x=300, y=50)

        self.listaMov.bind("<Double-1>", self.OnDoubleClickE)

        self.desconecta_Glac()
        self.janelaEst.mainloop()
    def add_movE(self):
        self.conecta_Glac()

        cod2 = self.codproduto2.get()
        prod2 = self.produto_aba2.get()
        dia = self.dia_aba2.get()
        mes = self.mes_aba2.get()
        ano = self.ano_aba2.get()
        lote = self.lote_aba2.get()
        diaV = self.diaV_aba2.get()
        mesV = self.mesV_aba2.get()
        anoV = self.anoV_aba2.get()
        quant = self.quant_aba2.get()
        custo = self.custo_aba2.get()
        fornecedor = self.entradaIdFornec.get()
        saida = self.saida_aba2.get()
        self.listaMov.delete(*self.listaMov.get_children())

        self.cursor.execute("""
    		INSERT INTO movim_prod ( cod_p, entrada, custo, dia, mes, ano,
    		lote, diaV, mesV, anoV, fornecedor, saida)
    		VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (cod2, quant, custo, dia, mes, ano, lote, diaV, mesV, anoV,
                        fornecedor, saida))
        self.conn.commit()

        msg = "Movimentação realizada.\n "
        msg += ""
        messagebox.showinfo("GLAC - Estoque", msg)

        lista1 = self.cursor.execute("""
    		SELECT  lote, entrada, saida, custo, dia , mes, ano, fornecedores.fornecedor, diaV, mesV, anoV FROM movim_prod , fornecedores
    		WHERE cod_p = '%s' and movim_prod.fornecedor = fornecedores.cod_forn ORDER BY id ASC;        """ % cod2)
        for i in lista1:
            self.listaMov.insert("", END, values=i)

        self.quantest.delete(0, END)

        lista2 = self.cursor.execute("""select Sum(entrada) - Sum(saida) from movim_prod where cod_p = '%s'""" % cod2)
        consultalista2 = self.cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)

        self.desconecta_Glac()
    def add_produtoE(self):

        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()
        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
            INSERT INTO servprod ( servprod, id_marcaprod, id_fornec, custo, valor, sp, descricao)
        	VALUES ( ?, ?, ?, ?, ?, "P", ?)""",
                       (servprod, id_marcaprod, id_fornec, custo, valor, descricao))
        conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        	SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
        	WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
        	""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        conn.close()
    def OnDoubleClickE(self, event):
        self.limpa_produtoE()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)

        self.carrega_produtoE()
    def mud_produtoE(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()
        self.cursor.execute("""
        	UPDATE servprod SET servprod = ? WHERE cod_sp = ?""", (servprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
        	UPDATE servprod SET id_marcaprod = ? WHERE cod_sp = ?""", (id_marcaprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
            UPDATE servprod SET id_fornec = ? WHERE cod_sp = ?""", (id_fornec, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
        	UPDATE servprod SET custo = ? WHERE cod_sp = ?""", (custo, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
        	UPDATE servprod SET valor = ? WHERE cod_sp = ?""", (valor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
        	UPDATE servprod SET descricao = ? WHERE cod_sp = ?""", (descricao, cod_sp))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        	SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
        	WHERE sp = "P" ORDER BY servprod ASC;
        	""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def limpa_produtoE(self):
        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.entradaCodprod.delete(0, END)
        self.codproduto2.delete(0, END)
        self.produto_aba2.delete(0, END)
        self.custo_aba2.delete(0, END)
    def del_produtoE(self):

        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()
        cod_sp = self.entradaCodprod.get()
        self.cursor.execute("""
        		DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        	SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
        	WHERE sp = "P" ORDER BY servprod ASC;
        	""")
        for i in lista:
            self.listaServ.insert("", END, values=i)
        conn.close()
    def carrega_produtoE(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        prod = self.cursor
        cod2 = self.codproduto2.get()

        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.codproduto2.delete(0, END)
        self.produto_aba2.delete(0, END)
        self.custo_aba2.delete(0, END)
        self.quantest.delete(0, END)
        self.listaMov.delete(*self.listaMov.get_children())

        prod.execute("SELECT servprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaprod = self.cursor.fetchall()
        for i in consultaprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaProd.insert(END, i)
            self.produto_aba2.insert(END, i)

        self.codproduto2.insert(END, cod_sp)

        idmarca = self.cursor
        idmarca.execute("SELECT id_marcaprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaidmarca = self.cursor.fetchall()
        for i in consultaidmarca:
            self.entradaIdMarcaprod.insert(END, i)

        mm = self.entradaIdMarcaprod.get()
        marca = self.cursor
        marca.execute("SELECT marca FROM marcaprod WHERE cod_marca = '%s'" % mm)
        consultaidmarca = self.cursor.fetchall()
        for i in consultaidmarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaMarcaprod.insert(END, i)

        idfornec = self.cursor
        idfornec.execute("SELECT id_fornec FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            self.entradaIdFornec.insert(END, i)

        ff = self.entradaIdFornec.get()
        fornec = self.cursor
        fornec.execute("SELECT fornecedor FROM fornecedores WHERE cod_forn = '%s'" % ff)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaFornec.insert(END, i)

        custo = self.cursor
        custo.execute("SELECT custo FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultacusto = self.cursor.fetchall()
        for i in consultacusto:
            self.entradaCusto.insert(END, i)
            self.custo_aba2.insert(END, i)

        valor = self.cursor
        valor.execute("SELECT valor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultavalor = self.cursor.fetchall()
        for i in consultavalor:
            self.entradaValor.insert(END, i)

        descrprod = self.cursor
        descrprod.execute("SELECT descricao FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultadescrprod = self.cursor.fetchall()
        for i in consultadescrprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaDescricao.insert(END, i)

        lista = self.cursor.execute("""SELECT  lote, entrada, saida, custo, dia , mes, ano, fornecedores.fornecedor, diaV, mesV, anoV FROM movim_prod , fornecedores
    	    WHERE cod_p = '%s' and movim_prod.fornecedor = fornecedores.cod_forn ORDER BY id ASC;        """ % cod_sp)
        for i in lista:
            self.listaMov.insert("", END, values=i)

        lista2 = self.cursor.execute("""select Sum(entrada) - Sum(saida) from movim_prod where cod_p = '%s'""" % cod_sp)
        consultalista2 = self.cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)
    def busca_produtoE(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaProd.insert(END, '%')
        servprod = self.entradaProd.get()

        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()

        lista = self.cursor.execute("""
       		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
       		WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
       		""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaProd.delete(0, END)

        conn.close()
    def busca_fornecE(self):
        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()

        def add_autobind(event):
            listatec1.selection()

            for n in listatec1.selection():
                col1, col2 = listatec1.item(n, 'values')
                self.entradaFornec.insert(END, col2)
                self.entradaIdFornec.insert(END, col1)

            listatec.destroy()

        def OnTec(*args):
            listatec1.yview(*args)


            ### Widgets - Listar tecnicos ###

        self.entradaFornec.insert(END, '%')

        veicAuto = self.entradaFornec.get()

        listatec = Tk()
        listatec.title("Fornecedores - GLAC  ")
        listatec.configure(background='gray75')
        listatec.geometry("310x240")
        listatec.resizable(TRUE, TRUE)
        ##########
        listatec1 = ttk.Treeview(listatec, height=10, column=("col1", "col2"))
        listatec1.heading("#0", text="")
        listatec1.heading("#1", text="Cod")
        listatec1.heading("#2", text="Fornecedor")

        listatec1.column("#0", width=0)
        listatec1.column("#1", width=60)
        listatec1.column("#2", width=220)

        # Cria barra de rolagem
        barra = Scrollbar(listatec, orient='vertical', command=listatec1.yview)

        # Adiciona barra de rolagem
        listatec1.configure(yscroll=barra.set)
        barra.place(x=280, y=12, width=25, height=220)

        listatec1.place(x=5, y=5)

        lista = self.cursor.execute("""SELECT cod_forn, fornecedor FROM fornecedores ORDER BY fornecedor ASC""")

        rows = cursor.fetchall()
        for row in rows:
            listatec1.insert("", END, values=row)

            # Binding da listbox
        listatec1.bind('<Double-1>', add_autobind)

        self.entradaFornec.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        conn.close
    def busca_marcaE(self):
        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()

        def add_autobind(event):

            listatec1.selection()

            for n in listatec1.selection():
                col1, col2 = listatec1.item(n, 'values')
                self.entradaMarcaprod.insert(END, col2)
                self.entradaIdMarcaprod.insert(END, col1)

            listatec.destroy()

        def OnTec(*args):
            listatec1.yview(*args)

            ### Widgets - Listar tecnicos ###

        self.entradaMarcaprod.insert(END, '%')

        veicAuto = self.entradaMarcaprod.get()

        listatec = Tk()
        listatec.title("Marcas - GLAC  ")
        listatec.configure(background='gray75')
        listatec.geometry("310x240")
        listatec.resizable(TRUE, TRUE)

        ##########
        listatec1 = ttk.Treeview(listatec, height=10, column=("col1", "col2"))
        listatec1.heading("#0", text="")
        listatec1.heading("#1", text="Cod")
        listatec1.heading("#2", text="Marca")

        listatec1.column("#0", width=0)
        listatec1.column("#1", width=60)
        listatec1.column("#2", width=220)

        # Cria barra de rolagem
        barra = Scrollbar(listatec, orient='vertical', command=listatec1.yview)

        # Adiciona barra de rolagem
        listatec1.configure(yscroll=barra.set)
        barra.place(x=280, y=6, width=30, height=225)

        listatec1.place(x=5, y=5)

        lista = self.cursor.execute("""SELECT cod_marca, marca FROM marcaprod ORDER BY marca ASC""")

        rows = cursor.fetchall()
        for row in rows:
            listatec1.insert("", END, values=row)

            # Binding da listbox
        listatec1.bind('<Double-1>', add_autobind)

        self.entradaMarcaprod.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        conn.close()
