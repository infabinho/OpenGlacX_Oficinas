from objects_glac import *

class Servicos(Objects_Glac):
    def cadserv(self):
        self.multiGlacx()
        self.cores()

        self.janelaServ = Toplevel()
        self.janelaServ.title(self.m_Serviços)
        self.janelaServ.configure(background= self.fundo_da_tela)
        self.janelaServ.geometry("1000x410")
        self.janelaServ.resizable(FALSE, FALSE)
        self.janelaServ.transient(self.janela)
        self.janelaServ.focus_force()
        self.janelaServ.grab_set()

        top3 = Canvas(self.janelaServ, bd=0, bg=self.fundo_do_frame, highlightbackground="gray70",
                      highlightthickness=2);
        top3.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.96)

        self.servicos_canvas2 = Canvas(self.janelaServ, width=835, height=2, cursor='X_cursor', bd=2, bg='gray55')
        self.servicos_canvas2.place(x=130, y=25)

        self.descrServicos = Label(self.janelaServ, text= self.m_Serviços, fg= 'gray45', bg = self.fundo_do_frame,
                                   font=('Times', '18', 'bold'))
        self.descrServicos.place(x=15, y=15)

        self.descrCod = Label(self.janelaServ, text= self.m_Codigo + self.m_Pontinhos,fg = 'darkblue',
                              bg = self.fundo_do_frame, font=('Verdana', '10', 'bold'))
        self.descrCod.place(x=16, y=50)
        self.entradaCod = Entry(self.janelaServ, width=6, fg='brown', font=('Verdana', '8', 'bold'))
        self.entradaCod.place(x=80, y=53)

        ###  Botao Carrega servico
        self.botaoAdd = Button(self.janelaServ, text= self.m_Carregar, bg ='#37609b', fg ='white',
                               font=('Verdana', '8', 'bold'),  command=self.carrega_servicoS)
        self.botaoAdd.place(x=135, y=50, width=130)
        ###  Botao limpa servico
        self.botaolimpa = Button(self.janelaServ, text= self.m_Limpar, bg ='#37609b', fg ='white',
                                 font=('Verdana', '8', 'bold'), command=self.limpa_servicoS)
        self.botaolimpa.place(x=270, y=50, width=70)

        self.descrServ = Label(self.janelaServ, text= self.m_Serviços, fg = 'darkblue', bg = self.fundo_do_frame,
                               font=('Verdana', '10', 'bold'))
        self.descrServ.place(x=15, y=80)
        self.entradaServ = Entry(self.janelaServ, width=45, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaServ.place(x=80, y=83)

        ###  Botao busca SERVICO
        self.botaolimpa = Button(self.janelaServ, text= self.m_Buscar, bg ='#37609b', fg ='white',
                                 font=('Verdana', '8', 'bold'), command=self.busca_servicoS)
        self.botaolimpa.place(x=350, y=80, width=50)

        self.descrHor = Label(self.janelaServ, text= self.m_Horas, fg = 'darkblue', bg = self.fundo_do_frame,
                              font=('Verdana', '10', 'bold'))
        self.descrHor.place(x=24, y=110)
        self.entradaHor = Entry(self.janelaServ, width=5, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaHor.place(x=80, y=113)

        self.descrCustohora = Label(self.janelaServ, text= self.m_Custo_R, fg ='darkblue', bg = self.fundo_do_frame,
                                    font=('Verdana', '10', 'bold'))
        self.descrCustohora.place(x=110, y=110)
        self.entradaCustohora = Entry(self.janelaServ, width=6, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaCustohora.place(x=180, y=113)

        self.descrValorhora = Label(self.janelaServ, text= self.m_Valor_R, fg ='darkblue', bg = self.fundo_do_frame,
                                    font=('Verdana', '10', 'bold'))
        self.descrValorhora.place(x=230, y=110)
        self.entradaValorhora = Entry(self.janelaServ, width=6, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaValorhora.place(x=295, y=113)

        self.descrTipoServ = Label(self.janelaServ, text= self.m_Tipo, fg ='darkblue', bg = self.fundo_do_frame,
                                   font=('Verdana', '10', 'bold'))
        self.descrTipoServ.place(x=445, y=40)
        self.entradaTipoServ = Entry(self.janelaServ, width=42, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaTipoServ.place(x=525, y=43)

        self.descrSistemaServ = Label(self.janelaServ, text= self.m_Sistema, fg ='darkblue', bg = self.fundo_do_frame,
                                      font=('Verdana', '10', 'bold'))
        self.descrSistemaServ.place(x=445, y=60)
        self.entradaSistemaServ = Entry(self.janelaServ, width=42, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaSistemaServ.place(x=525, y=63)

        self.descrDescricao = Label(self.janelaServ, text= self.m_Marca, fg ='darkblue', bg = self.fundo_do_frame,
                                    font=('Verdana', '10', 'bold'))
        self.descrDescricao.place(x=445, y=80)
        self.entradaDescricao = Entry(self.janelaServ, width=42, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaDescricao.place(x=525, y=83)

        self.descrVeic = Button(self.janelaServ, text= self.m_Veiculo, bg ='#37609b', fg ='white',
                                command=self.busca_serv_veicS,
                                font=('Verdana', '10', 'bold'))
        self.descrVeic.place(x=445, y=100)
        self.entradaVeic = Entry(self.janelaServ, width=42, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaVeic.place(x=525, y=103)

        self.botaoAdd = Button(self.janelaServ, text= self.m_Novo, command=self.add_servS, bg ='#37609b', fg ='white',
                               font=('Verdana', '10', 'bold'))
        self.botaoAdd.place(x=800, y=50, width=80)

        self.botaoMudServ = Button(self.janelaServ, text= self.m_Alterar, command=self.mud_servS, bg ='#37609b', fg ='white',
                                   font=('Verdana', '10', 'bold'))
        self.botaoMudServ.place(x=800, y=80, width=80)

        self.botaoDel = Button(self.janelaServ, text= self.m_Apagar, command=self.del_servS, fg='brown', font=('Verdana', '10', 'bold'))
        self.botaoDel.place(x=800, y=110, width=80)

        ### Widgets - Listar veiculos ###

        self.listaServ = ttk.Treeview(self.janelaServ, height=10,
                                 column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text= self.m_Codigo)
        self.listaServ.heading("#2", text= self.m_Serviços)
        self.listaServ.heading("#3", text= self.m_Horas)
        self.listaServ.heading("#4", text= self.m_Custo_R)
        self.listaServ.heading("#5", text= self.m_Valor)
        self.listaServ.heading("#6", text= self.m_Marca)
        self.listaServ.heading("#7", text= self.m_Veiculo)
        self.listaServ.heading("#8", text= self.m_Tipo)
        self.listaServ.heading("#9", text= self.m_Sistema)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=40)
        self.listaServ.column("#2", width=230)
        self.listaServ.column("#3", width=45)
        self.listaServ.column("#4", width=57)
        self.listaServ.column("#5", width=55)
        self.listaServ.column("#6", width=120)
        self.listaServ.column("#7", width=145)
        self.listaServ.column("#8", width=110)
        self.listaServ.column("#9", width=145)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaServ, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=960, y=150, width=20, height=230)

        self.conecta_Glac()

        lista = self.cursor.execute("""
            SELECT cod_sp, servprod, hor, custo , valor, descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod  WHERE sp = "s" ORDER BY servprod ASC;
            """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=15, y=150)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickS)

        self.desconecta_Glac()

        self.janelaServ.mainloop()
    def OnDoubleClickS(self, event):
        self.limpa_servicoS()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_servicoS()
    def mud_servS(self):
        self.conecta_Glac()

        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()
        hor = self.entradaHor.get()
        custo = self.entradaCustohora.get()
        valor = self.entradaValorhora.get()
        tiposerv = self.entradaTipoServ.get()
        sistemaserv = self.entradaSistemaServ.get()
        descricao = self.entradaDescricao.get()
        veic = self.entradaVeic.get()

        self.cursor.execute("""
     		UPDATE servprod SET servprod = ? WHERE cod_sp = ?""", (servprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET hor = ? WHERE cod_sp = ?""", (hor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET custo = ? WHERE cod_sp = ?""", (custo, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET valor = ? WHERE cod_sp = ?""", (valor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET tiposerv = ? WHERE cod_sp = ?""", (tiposerv, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET sistemaserv = ? WHERE cod_sp = ?""", (sistemaserv, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET descricao = ? WHERE cod_sp = ?""", (descricao, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET id_marcaprod = ? WHERE cod_sp = ?""", (veic, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
         SELECT cod_sp, servprod, hor, custo , valor, descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod  WHERE sp = "S" ORDER BY servprod ASC;
         """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def limpa_servicoS(self):
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)
        self.entradaHor.delete(0, END)
        self.entradaCustohora.delete(0, END)
        self.entradaValorhora.delete(0, END)
        self.entradaTipoServ.delete(0, END)
        self.entradaSistemaServ.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaVeic.delete(0, END)
    def del_servS(self):
        self.conecta_Glac()

        cod_sp = self.entradaCod.get()
        self.listaServ.delete(*self.listaServ.get_children())
        self.cursor.execute("""
     	DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        self.conn.commit()

        lista = self.cursor.execute("""
         SELECT cod_sp, servprod, hor, custo , valor, descricao, tiposerv, sistemaserv FROM servprod  WHERE sp = "S" ORDER BY cod_sp DESC;
         """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def carrega_servicoS(self):
        cod_sp = self.entradaCod.get()
        self.conecta_Glac()

        sp = self.cursor

        self.entradaServ.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaHor.delete(0, END)
        self.entradaCustohora.delete(0, END)
        self.entradaValorhora.delete(0, END)
        self.entradaTipoServ.delete(0, END)
        self.entradaSistemaServ.delete(0, END)
        self.entradaVeic.delete(0, END)

        sp.execute("SELECT servprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaserv = self.cursor.fetchall()
        for i in consultaserv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaServ.insert(END, i)

        hora = self.cursor
        hora.execute("SELECT hor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultahor = self.cursor.fetchall()
        for i in consultahor:
            self.entradaHor.insert(END, i)

        custohora = self.cursor
        custohora.execute("SELECT custo FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultacustohora = self.cursor.fetchall()
        for i in consultacustohora:
            self.entradaCustohora.insert(END, i)

        valorhora = self.cursor
        valorhora.execute("SELECT valor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultavalorhora = self.cursor.fetchall()
        for i in consultavalorhora:
            self.entradaValorhora.insert(END, i)

        tiposerv = self.cursor
        tiposerv.execute("SELECT tiposerv FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultatiposerv = self.cursor.fetchall()
        for i in consultatiposerv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaTipoServ.insert(END, i)

        sistemaserv = self.cursor
        sistemaserv.execute("SELECT sistemaserv FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultasistemaserv = self.cursor.fetchall()
        for i in consultasistemaserv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaSistemaServ.insert(END, i)

        descricao = self.cursor
        descricao.execute("SELECT descricao FROM servprod WHERE cod_sp = '%s'" % cod_sp)
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

        self.cursor.execute("SELECT id_marcaprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultadescricao = self.cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaVeic.insert(END, i)

            self.desconecta_Glac()
    def busca_serv_veicS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaVeic.insert(END, '%')
        veic = self.entradaVeic.get()

        self.conecta_Glac()

        servico = self.cursor

        servico.execute("""SELECT cod_sp, servprod, hor, custo, valor, descricao, id_marcaprod, tiposerv, sistemaserv
     	FROM servprod WHERE id_marcaprod LIKE '%s'  """ % veic)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaVeic.delete(0, END)

        self.desconecta_Glac()
    def busca_servicoS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaServ.insert(END, '%')
        self.conecta_Glac()

        servprod = self.entradaServ.get()
        servico = self.cursor

        servico.execute(
            """SELECT cod_sp, servprod, hor, custo, valor, descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod WHERE servprod LIKE '%s'  """ % servprod)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()
    def add_servS(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()
        hor = self.entradaHor.get()
        custo = self.entradaCustohora.get()
        valor = self.entradaValorhora.get()
        tiposerv = self.entradaTipoServ.get()
        sistemaserv = self.entradaSistemaServ.get()
        descricao = self.entradaDescricao.get()
        veic = self.entradaVeic.get()
        id_marcaprod = self.entradaDescricao.get()

        self.cursor.execute("""
     		INSERT INTO servprod ( servprod, hor, custo, valor, tiposerv, sistemaserv, sp, descricao, id_marcaprod)
     		VALUES ( ?, ?, ?, ?, ?, ?, "S", ?, ?)""",
                       (servprod, hor, custo, valor, tiposerv, sistemaserv, descricao, id_marcaprod))
        self.conn.commit()
        lista = self.cursor.execute("""
         SELECT cod_sp, servprod, hor, custo , valor, descricao , id_marcaprod, tiposerv, sistemaserv FROM servprod  WHERE sp = "S" ORDER BY cod_sp DESC;
         """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
