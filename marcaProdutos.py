from objects_glac import *

class MarcaProdutos(Objects_Glac):
    def cadmarcaprod(self):
        self.multiGlacx()
        self.cores()

        self.janelaM = Toplevel()
        self.janelaM.title(self.m_Marca + ' ' + self.m_Produtos)
        self.janelaM.configure(background=self.fundo_do_frame)
        self.janelaM.geometry("870x250")
        self.janelaM.resizable(FALSE, FALSE)
        self.janelaM.transient(self.janela)
        self.janelaM.focus_force()
        self.janelaM.grab_set()

        self.descrTitulo = Label(self.janelaM, bg= self.fundo_da_tela)
        self.descrTitulo.place(x=1, y=1, width= 868, height = 55)

        self.descrServicos = Label(self.janelaM, text= self.m_Marca + ' ' + self.m_Produtos, fg='gray75',
                                   bg= self.fundo_da_tela, font=('Times', '22', 'bold'))
        self.descrServicos.place(x=15, y=10)

        self.servicos_canvas2 = Canvas(self.janelaM, width=600, height=2, cursor='X_cursor', bd=2, bg='gray75')
        self.servicos_canvas2.place(x=230, y=25)

        self.descrCod = Label(self.janelaM, text= self.m_Codigo, fg='darkblue', bg = self.fundo_do_frame,
                              font=('Verdana', '10', 'bold'))
        self.descrCod.place(x=18, y=70)
        self.entradaCod = Entry(self.janelaM, width=6, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaCod.place(x=80, y=73)

        ###  Botao Carrega marca
        self.botaoAdd = Button(self.janelaM, text= self.m_Carregar, bd=2, bg='#6d6789', fg='white',
                               font=('Verdana', '9', 'bold'), command=self.carrega_marca_prod)
        self.botaoAdd.place(x=135, y=70, width=130)
        ###  Botao limpa automovel
        self.botaolimpa = Button(self.janelaM, text= self.m_Limpar, bd=2, bg='#6d6789', fg='white',
                               font=('Verdana', '9', 'bold'), command=self.limpa_marca_prod)
        self.botaolimpa.place(x=270, y=70, width=70)

        self.descrMarca = Label(self.janelaM, text= self.m_Marca, fg='darkblue', bg = self.fundo_do_frame,
                                font=('Verdana', '10', 'bold'))
        self.descrMarca.place(x=25, y=100)
        self.entradaMarca = Entry(self.janelaM, width=30, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaMarca.place(x=80, y=103)
        ###  Botao busca automovel
        self.botaobusca = Button(self.janelaM, text= self.m_Buscar, bd=2, bg='#6d6789', fg='white',
                               font=('Verdana', '9', 'bold'), command=self.busca_marca_prod)
        self.botaobusca.place(x=270, y=100, width=70)

        self.descrDescricao = Label(self.janelaM, text= self.m_Descricao, fg='darkblue', bg = self.fundo_do_frame,
                                    font=('Verdana', '10', 'bold'))
        self.descrDescricao.place(x=1, y=130)
        self.entradaDescricao = Entry(self.janelaM, width=40, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaDescricao.place(x=80, y=133)

        self.botaoAdd = Button(self.janelaM, text= self.m_Novo,bd=2, bg='#6d6789', fg='white',
                               font=('Verdana', '9', 'bold'), command=self.add_marca_prod)
        self.botaoAdd.place(x=50, y=210, width=85)

        self.botaoMud = Button(self.janelaM, text= self.m_Alterar, bd=2, bg='#6d6789', fg='white',
                               font=('Verdana', '9', 'bold'), command=self.mud_marca_prod)
        self.botaoMud.place(x=150, y=210, width=85)

        # botaoDel = Button(janelaM, text=" Apagar ", bd=4, fg='darkblue', command=del_marca_prod, font=('Verdana', '10', 'bold'))
        # botaoDel.place(x=250, y=210, width=85)

        ### Widgets - Listar produtos ###

        self.listaServ = ttk.Treeview(self.janelaM, height=7, column=("col1", "col2", "col3"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text= self.m_Codigo)
        self.listaServ.heading("#2", text= self.m_Marca)
        self.listaServ.heading("#3", text= self.m_Descricao)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=35)
        self.listaServ.column("#2", width=200)
        self.listaServ.column("#3", width=250)

        self.conecta_Glac()

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaM, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=845, y=70, width=30, height=180)

        lista = self.cursor.execute("""
            SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=360, y=70)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickMarc)

        self.desconecta_Glac()

        self.janelaM.mainloop()
    def OnDoubleClickMarc(self, event):
        self.limpa_marca_prod()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_marca_prod()
    def mud_marca_prod(self):
        self.conecta_Glac()

        cod_marca = self.entradaCod.get()
        marca = self.entradaMarca.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
     		UPDATE marcaprod SET marca = ? WHERE cod_marca = ?""", (marca, cod_marca))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE marcaprod SET descricao = ? WHERE cod_marca = ?""", (descricao, cod_marca))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        listacod = self.cursor.execute("""SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in listacod:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def carrega_marca_prod(self):
        cod_marca = self.entradaCod.get()
        self.conecta_Glac()

        marcaprod = self.cursor

        self.entradaMarca.delete(0, END)
        self.entradaDescricao.delete(0, END)

        marcaprod.execute("SELECT marca FROM marcaprod WHERE cod_marca = '%s'" % cod_marca)
        consultamarcaprod = self.cursor.fetchall()
        for i in consultamarcaprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarca.insert(END, i)

        descricao = self.cursor
        descricao.execute("SELECT descricao FROM marcaprod WHERE cod_marca = '%s'" % cod_marca)
        consultadescricao = self.cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

        self.desconecta_Glac()
    def del_marca_prod(self):

        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()
        cod_marca = self.entradaCod.get()
        self.cursor.execute("""
     		DELETE FROM marcaprod WHERE cod_marca=?""", (cod_marca,))
        conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)
        conn.close()
    def limpa_marca_prod(self):
        self.entradaCod.delete(0, END)
        self.entradaMarca.delete(0, END)
        self.entradaDescricao.delete(0, END)
    def add_marca_prod(self):
        self.conecta_Glac()

        cod_marca = self.entradaCod.get()
        marca = self.entradaMarca.get()
        descricao = self.entradaDescricao.get()
        self.listaServ.delete(*self.listaServ.get_children())
        self.cursor.execute("""
     		INSERT INTO marcaprod ( marca, descricao)
     		VALUES ( ?, ?)""",  (marca, descricao))
        self.conn.commit()
        lista = self.cursor.execute("""
             SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def busca_marca_prod(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaMarca.insert(END, '%')
        self.conecta_Glac()
        marca = self.entradaMarca.get()
        marcap = self.cursor

        marcap.execute("SELECT * FROM marcaprod WHERE marca LIKE '%s'" % marca)
        buscamarca = self.cursor.fetchall()
        for i in buscamarca:
            self.listaServ.insert("", END, values=i)
        self.entradaMarca.delete(0, END)

        self.desconecta_Glac()
