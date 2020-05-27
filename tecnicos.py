from objects_glac import *

class Tecnicos(Objects_Glac):
    def cadtec(self):
        self.multiGlacx()
        self.cores()

        self.janelaTec = Toplevel()
        self.janelaTec.title(self.m_Tecnico)
        self.janelaTec.configure(background=self.fundo_do_frame)
        self.janelaTec.geometry("650x210")
        self.janelaTec.transient(self.janela)
        self.janelaTec.focus_force()
        self.janelaTec.grab_set()

        self.janelaTec.resizable(FALSE, FALSE)
        self.tech_obj()

        self.servicos_canvas2 = Canvas(self.janelaTec, width=650, height=42, bd=0, bg=self.fundo_da_tela,
                                       highlightbackground="#45e0fc", highlightthickness=1)
        self.servicos_canvas2.place(x=0, y=0)
        self.servicos_canvas2 = Canvas(self.janelaTec, width=5, height=210, bd=0, bg=self.fundo_da_tela,
                                       highlightbackground="#45e0fc", highlightthickness=1)
        self.servicos_canvas2.place(x=0, y=0)

        self.descrServicos = Label(self.janelaTec, text=self.m_Tecnico, fg='gray85', bg=self.fundo_da_tela,
                                   font=('Arial', '28', 'bold', 'italic'))
        self.descrServicos.place(x=250, y=1, height=40)

        self.descrCod = Label(self.janelaTec, text=self.m_Codigo, fg='darkblue', bg=self.fundo_do_frame,
                              font=('Verdana', '10', 'bold'))
        self.descrCod.place(x=16, y=50)
        self.entradaCod = Entry(self.janelaTec, width=6, fg='brown', font=('Verdana', '8', 'bold'))
        self.entradaCod.place(x=80, y=53)

        ###  Botao Carrega servico
        self.botaoCarregar.configure(command=self.carrega_servicoT)
        self.botaoCarregar.place(x=135, y=50, width=130)
        ###  Botao limpa servico
        self.botaolimpa.configure(command=self.limpa_servicoT)
        self.botaolimpa.place(x=270, y=50, width=70)

        self.descrServ = Label(self.janelaTec, text=self.m_Tecnico, fg='darkblue', bg=self.fundo_do_frame,
                               font=('Verdana', '10', 'bold'))
        self.descrServ.place(x=15, y=80)
        self.entradaServ = Entry(self.janelaTec, width=33, fg='brown', font=('Verdana', '7', 'bold'))
        self.entradaServ.place(x=80, y=83)

        ###  Botao busca SERVICO
        self.botaobusca.configure(command=self.busca_servicoT)
        self.botaobusca.place(x=290, y=80, width=50)

        self.botaoAdd.configure(command=self.add_servT)
        self.botaoAdd.place(x=30, y=140, width=80)

        self.botaoMud.configure(command=self.mud_servT)
        self.botaoMud.place(x=130, y=140, width=80)

        self.botaoDel.configure(command=self.del_servT)
        self.botaoDel.place(x=230, y=140, width=80)

        ### Widgets - Listar veiculos ###

        self.listaServ = ttk.Treeview(self.janelaTec, height=6, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Tecnico)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=35)
        self.listaServ.column("#2", width=230)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaTec, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=610, y=50, width=30, height=147)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickT)

        self.conecta_Glac()

        lista = self.cursor.execute("""
                    SELECT cod, tecnico FROM tecnico  ORDER BY tecnico ASC;
                    """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.place(x=345, y=50)

        self.desconecta_Glac()

        self.janelaTec.mainloop()
    def add_tecnicobind(self, event):
        self.codServ1.delete(0, END)

        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaTecnico.insert(END, col2)

        # self.add_servico1()
        self.listatec.destroy()
    def OnTec(self, *args):
        self.listaServ.yview(*args)
    def limpa_servicoT(self):
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)
    def mud_servT(self):
        self.conecta_Glac()

        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()

        self.cursor.execute("""
            UPDATE tecnico SET tecnico = ? WHERE cod = ?""", (servprod, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        SELECT * FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def OnDoubleClickT(self, event):
        self.limpa_servicoT()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_servicoT()
    def del_servT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        cod_sp = self.entradaCod.get()
        self.cursor.execute("""
        DELETE FROM tecnico WHERE cod = ? """, (cod_sp,))
        self.conn.commit()

        lista = self.cursor.execute("""
        SELECT cod, tecnico FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()
    def carrega_servicoT(self):
        cod_sp = self.entradaCod.get()
        self.conecta_Glac()

        sp = self.cursor

        self.entradaServ.delete(0, END)

        sp.execute("SELECT tecnico FROM tecnico WHERE cod = '%s'" % cod_sp)
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

        self.desconecta_Glac()
    def busca_servicoT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        self.entradaServ.insert(END, '%')
        servprod = self.entradaServ.get()
        servico = self.cursor

        servico.execute("""SELECT cod, tecnico FROM tecnico WHERE tecnico LIKE '%s'  """ % servprod)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()
    def add_servT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        codinf = self.cursor.execute("""select MAX(cod) + 1 from tecnico """)
        for i in codinf:
            self.entradaCod.insert(END, i)

        servprod = self.entradaServ.get()
        cod_sp = self.entradaCod.get()

        self.cursor.execute("""
    		INSERT INTO tecnico (cod, tecnico) VALUES (?, ?)""", (cod_sp, servprod))
        self.conn.commit()

        lista = self.cursor.execute("""
        SELECT * FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()
