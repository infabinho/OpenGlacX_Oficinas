from objects_glac import *

class Fornecedores(Objects_Glac):
    def cadforn(self):
        self.multiGlacx();        self.cores()
        def abre_janela():
            self.janelaFor = Toplevel()
            self.janelaFor.title(self.m_Fornecedores)
            self.janelaFor.configure(background= self.fundo_do_frame)
            self.janelaFor.geometry("720x290")
            self.janelaFor.resizable(FALSE, FALSE)
            self.janelaFor.transient(self.janela)
            self.janelaFor.focus_force()
            self.janelaFor.grab_set()

            top2 = Canvas(self.janelaFor, bd=0, bg=self.fundo_da_tela, highlightbackground="gray70",
                          highlightthickness=2);
            top2.place(relx=0, rely=0, relwidth=1, relheight=0.04)
            top3 = Canvas(self.janelaFor, bd=0, bg=self.fundo_da_tela, highlightbackground="gray70",
                          highlightthickness=2);
            top3.place(relx=0, rely=0.96, relwidth=1, relheight=0.04)
            top3 = Canvas(self.janelaFor, bd=0, bg=self.fundo_da_tela, highlightbackground="gray70",
                          highlightthickness=2);
            top3.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)
        abre_janela()
        self.provider_obj()

        def widgets():
            #################################################################################################
            #####   Codigo
            self.descrCod_forn.place(x=5, y=20)
            self.entradaCod_forn.place(x=80, y=23)
            ####  Fornecedor
            self.descrFornecedor.place(x=1, y=50)
            self.entradaFornecedor.place(x=80, y=53)
            #### Fone
            self.descrFone.place(x=1, y=80)
            self.entradaFone.place(x=80, y=83)
            ####
            self.descrCnpj.place(x=160, y=80)
            self.entradaCnpj.place(x=200, y=83)
            ####
            self.entradaCep.place(x=80, y=113)
            ####
            self.descrEndereco.place(x=1, y=140)
            self.entradaEndereco.place(x=80, y=143)
            ####
            self.descrMunicipio.place(x=1, y=170)
            self.entradaMunicipio.place(x=80, y=173)
            ####
            self.descrDescricao.place(x=5, y=200)
            self.entradaDescricao.place(x=80, y=203)
        widgets()
        def botoes():
            ###  Botao Carrega fornecedor
            self.botaoCarregarForn.configure(command=self.carrega_fornecedor)
            self.botaoCarregarForn.place(x=120, y=20, width=140)
            ###  Botao limpa fornecedor
            self.botaoLimpaForn.configure(command=self.limpa_fornecedor)
            self.botaoLimpaForn.place(x=270, y=20, width=70)
            ###  Botao busca fornecedor
            self.botaoBuscaForn.configure(command=self.busca_fornecedor)
            self.botaoBuscaForn.place(x=270, y=50, width=70)
            #### Botao Cep
            self.botaoCepForn.configure(command=self.cepForn)
            self.botaoCepForn.place(x=30, y=108, width = 50, height = 25)
            #### botao novo fornecedor
            self.botaoNovoForn.configure(command=self.add_fornec)
            self.botaoNovoForn.place(x=50, y=240, width=90)
            #### botao alterar fornecedor
            self.botaoAlterarForn.configure(command=self.mud_fornec)
            self.botaoAlterarForn.place(x=150, y=240, width=90)
            ##### botao apagar fornacedor
            self.botaoApagarFornecedor.configure(command=self.del_fornec)
            self.botaoApagarFornecedor.place(x=250, y=240, width=90)
        botoes()
        ### Widgets - Listar veiculos ###
        self.listaServ = ttk.Treeview(self.janelaFor, height=12, column=("col1", "col2", "col3", "col4"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Fornecedores)
        self.listaServ.heading("#3", text=self.m_Fone)
        self.listaServ.heading("#4", text=self.m_Cidade)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=120)
        self.listaServ.column("#3", width=70)
        self.listaServ.column("#4", width=90)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaFor, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=678, y=12, width=30, height=268)
        self.listaServ.place(x=355, y=12)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickForn)

        self.conn = sqlite3.connect("glac.db")
        self.cursor = self.conn.cursor()
        lista = self.cursor.execute("""
            SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores ORDER BY fornecedor ASC;
            """)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        self.janelaFor.mainloop()
    def OnDoubleClickForn(self, event):
        self.limpa_fornecedor()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCod_forn.insert(END, col1)
        self.carrega_fornecedor()
    def mud_fornec(self):
        self.conecta_Glac()

        cod_forn = self.entradaCod_forn.get()
        fornecedor = self.entradaFornecedor.get()
        fone = self.entradaFone.get()
        cnpj = self.entradaCnpj.get()
        cep = self.entradaCep.get()
        endereco = self.entradaEndereco.get()
        municipio = self.entradaMunicipio.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
    		UPDATE fornecedores SET fornecedor = ? WHERE cod_forn = ?""", (fornecedor, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET fone = ? WHERE cod_forn = ?""", (fone, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET cnpj = ? WHERE cod_forn = ?""", (cnpj, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET cep = ? WHERE cod_forn = ?""", (cep, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET endereco = ? WHERE cod_forn = ?""", (endereco, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET municipio = ? WHERE cod_forn = ?""", (municipio, cod_forn))
        self.conn.commit()
        self.cursor.execute("""
    		UPDATE fornecedores SET descricao = ? WHERE cod_forn = ?""", (descricao, cod_forn))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores ORDER BY fornecedor ASC;
        """)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
            self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
    		SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores ORDER BY fornecedor ASC;
    		""")
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        self.desconecta_Glac()
        msg = "Dados do fornecedor alterados com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def limpa_fornecedor(self):
        self.conecta_Glac()

        self.entradaCod_forn.delete(0, END)
        self.entradaFornecedor.delete(0, END)
        self.entradaFone.delete(0, END)
        self.entradaCnpj.delete(0, END)
        self.entradaCep.delete(0, END)
        self.entradaEndereco.delete(0, END)
        self.entradaMunicipio.delete(0, END)
        self.entradaDescricao.delete(0, END)

        self.desconecta_Glac()
    def del_fornec(self):
        self.conecta_Glac()

        cod_forn = self.entradaCod_forn.get()
        self.cursor.execute("""
    		DELETE FROM fornecedores WHERE cod_forn=?""", (cod_forn,))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute(
            """SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores ORDER BY fornecedor ASC;""")

        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        self.desconecta_Glac()
        msg = "Fornecedor excluido com sucesso.  :("
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def carrega_fornecedor(self):
        self.conecta_Glac()

        cursor = self.cursor

        cod_forn = self.entradaCod_forn.get()
        fornec = cursor

        self.entradaFornecedor.delete(0, END)
        self.entradaFone.delete(0, END)
        self.entradaCnpj.delete(0, END)
        self.entradaCep.delete(0, END)
        self.entradaEndereco.delete(0, END)
        self.entradaMunicipio.delete(0, END)
        self.entradaDescricao.delete(0, END)

        fornec.execute("SELECT fornecedor FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultafornec = self.cursor.fetchall()
        for i in consultafornec:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaFornecedor.insert(END, i)

        fone = self.cursor
        fone.execute("SELECT fone FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultafone = self.cursor.fetchall()
        for i in consultafone:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaFone.insert(END, i)

        cnpj = self.cursor
        cnpj.execute("SELECT cnpj FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultacnpj = self.cursor.fetchall()
        for i in consultacnpj:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaCnpj.insert(END, i)

        cep = cursor
        cep.execute("SELECT cep FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultacep = cursor.fetchall()
        for i in consultacep:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaCep.insert(END, i)

        endereco = cursor
        endereco.execute("SELECT endereco FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultaendereco = cursor.fetchall()
        for i in consultaendereco:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaEndereco.insert(END, i)

        municipio = cursor
        municipio.execute("SELECT municipio FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultamunicipio = cursor.fetchall()
        for i in consultamunicipio:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMunicipio.insert(END, i)

        descricao = cursor
        descricao.execute("SELECT descricao FROM fornecedores WHERE cod_forn = '%s'" % cod_forn)
        consultadescricao = cursor.fetchall()
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
    def cepForn(self):
        self.entradaEndereco.delete(0, END)

        self.entradaMunicipio.delete(0, END)

        try:
            self.cep = self.entradaCep.get()
            self.endereco = pycep_correios.consultar_cep(self.cep)

            self.entradaEndereco.insert(END, self.endereco['end'])
            self.entradaEndereco.insert(END, ' - ')
            self.entradaEndereco.insert(END, self.endereco ['bairro'])

            self.entradaMunicipio.insert(END, self.endereco['cidade'])
            self.entradaMunicipio.insert(END, ' - ')
            self.entradaMunicipio.insert(END, self.endereco['uf'])


        except ExcecaoPyCEPCorreios as exc:
            msg = multi.CepNotFind
            msg += ""
            messagebox.showinfo("GLAC ", msg)
    def busca_fornecedor(self):
        self.conecta_Glac()

        self.entradaFornecedor.insert(END, '%')
        self.listaServ.delete(*self.listaServ.get_children())
        fornecedor = self.entradaFornecedor.get()

        lista = self.cursor.execute("""
        SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores WHERE fornecedor LIKE '%s'                  ORDER BY fornecedor ASC;
        """ % fornecedor)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
            self.entradaFornecedor.delete(0, END)


        self.desconecta_Glac()
    def add_fornec(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        cod_forn = self.entradaCod_forn.get()
        fornecedor = self.entradaFornecedor.get()
        fone = self.entradaFone.get()
        cnpj = self.entradaCnpj.get()
        cep = self.entradaCep.get()
        endereco = self.entradaEndereco.get()
        municipio = self.entradaMunicipio.get()
        descricao = self.entradaDescricao.get()


        self.cursor.execute("""
    		INSERT INTO fornecedores (fornecedor, fone, cnpj, cep, endereco, municipio, descricao)
    		VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (fornecedor, fone, cnpj, cep, endereco, municipio, descricao))
        self.conn.commit()
        lista = self.cursor.execute("""
    		SELECT cod_forn, fornecedor, fone, cnpj, municipio, descricao FROM fornecedores ORDER BY fornecedor ASC;
    		""")
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)

        msg = "Novo fornecedor incluido com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
        self.desconecta_Glac()
