from objects_glac import *

class Automoveis(Objects_Glac):
    def cadaut(self):
        def abreJanela():
            self.janelaAut = Toplevel()
            self.janelaAut.title('Glac')
            self.janelaAut.configure(background=self.fundo_da_tela)
            self.janelaAut.geometry("800x235")
            self.janelaAut.resizable(FALSE, FALSE)
            self.janelaAut.transient(self.janela)
            self.janelaAut.focus_force()
            self.janelaAut.grab_set()

        def canvasAut():
            self.cliente_canvas2 = Canvas(self.janelaAut, width=790, height=200, cursor='X_cursor', bd=2,
                                          bg=self.fundo_da_tela, highlightbackground="gray75", highlightthickness=2)
            self.cliente_canvas2.place(x=0, y=28)
            self.cliente_canvas2 = Canvas(self.janelaAut, width=340, height=180, cursor='X_cursor', bd=2,
                                          bg=self.fundo_do_frame, highlightbackground="#45e0fc",
                                          highlightthickness=2)
            self.cliente_canvas2.place(x=8, y=38)
        def widgets():
            ####
            self.descrNomeServ.place(x=307, y=0, relheight=0.1)
            ###  Descrição e Entrada codigo
            self.descrCod_aut.place(x=10, y=52)
            self.entradaCod_autA.place(x=85, y=52)
            ###  Descrição e Entrada Automovel
            self.descrAut.place(x=10, y=90)
            self.entradaAutA.place(x=85, y=90)
            ###  Descrição e Entrada Marca
            self.entradaMarcaA.place(x=85, y=130)
        def botoes():
            ###  Botao busca automovel
            self.botaoBuscaAut.configure(command=self.busca_automovelA)
            self.botaoBuscaAut.place(x=290, y=89, width=55, height=23)
            ###  Botao Carrega automovel
            self.botaoCarregaAut.configure(command=self.carrega_automovelA)
            self.botaoCarregaAut.place(x=150, y=50, width=90)
            ###  Botao limpa automovel
            self.botaoLimpaAut.configure(command=self.limpa_automovelA)
            self.botaoLimpaAut.place(x=250, y=50, width=90)
            ###  Botao busca marca
            self.botaoMarcaAut.configure(command=self.busca_autoA)
            self.botaoMarcaAut.place(x=10, y=128, width=72, height=23)
            ###  Botao Novo Cliente
            self.botaoNovoAut.configure(command=self.add_automovelA)
            self.botaoNovoAut.place(x=30, y=180, width=80)
            ### Botao Altera dados do Cliente
            self.botaoAlterarAut.configure(command=self.mud_automovelA)
            self.botaoAlterarAut.place(x=130, y=180, width=80)
            ### Botao Deletar Cliente
            self.botaoApagarAut.configure(command=self.del_automovelA)
            self.botaoApagarAut.place(x=230, y=180, width=80)
        def listaAut():
            # Cria barra de rolagem
            self.barra = Scrollbar(self.janelaAut, orient='vertical', command=self.OnVsbA)

            ### Widgets - Listar veiculos ###
            self.listaServ = ttk.Treeview(self.janelaAut, height=8, column=("col1", "col2", "col3"))
            self.listaServ.heading("#0", text="")
            self.listaServ.heading("#1", text=self.m_Codigo)
            self.listaServ.heading("#2", text=self.m_Automovel)
            self.listaServ.heading("#3", text=self.m_Marca)

            self.listaServ.column("#0", width=0)
            self.listaServ.column("#1", width=45)
            self.listaServ.column("#2", width=170)
            self.listaServ.column("#3", width=170)

            # Adiciona barra de rolagem
            self.listaServ.configure(yscroll=self.barra.set)
            self.barra.place(x=755, y=40, width=30, height=185)

            self.conecta_Glac()

            lista = self.cursor.execute("""
                         SELECT  automoveis.cod_aut, automoveis.automovel, montadora.marca FROM automoveis, montadora
                         WHERE montadora.cod = automoveis.montad  ORDER BY automovel ASC;
                         """)
            for i in lista:
                self.listaServ.insert("", END, values=i)

            self.desconecta_Glac()

            self.listaServ.place(x=365, y=40)
            self.listaServ.bind("<Double-1>", self.OnDoubleClickA)
        self.cores();  self.multiGlacx();  abreJanela();  canvasAut(); self.model_car_obj();
        widgets(); botoes(); listaAut()
        self.janelaAut.mainloop()
    def add_automovelA(self):

        cod_aut = self.entradaCod_autA.get()
        automovel = self.entradaAutA.get()
        montad = self.entradaMarca2A.get()
        self.conecta_Glac()

        self.cursor.execute("""
       		INSERT INTO automoveis ( automovel, montad)
       		VALUES ( ?, ?)""",
                       (automovel, montad))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())

        lista = self.cursor.execute("""
               SELECT  automoveis.cod_aut, automoveis.automovel, montadora.marca FROM automoveis, montadora
           	WHERE montadora.cod = automoveis.montad  ORDER BY automoveis.cod_aut DESC;
               """)
        for i in lista:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        self.limpa_automovelA()
        msg = self.m_msgAutAdd
        msg += ""
        messagebox.showinfo("GLAC - Automovel", msg)
    def add_autobindA(self, event):

        pos = int(self.listatec1.curselection()[0])
        cod = self.listatec1.get(pos)
        self.conecta_Glac()

        addserv1cod = self.cursor
        addserv1cod.execute("""SELECT cod FROM montadora WHERE cod LIKE '%s'""" % cod)
        addservico1cod = self.cursor.fetchall()
        for i in addservico1cod:
            self.entradaMarca2A.insert(END, i)

        addserv1cod = self.cursor
        addserv1cod.execute("""SELECT marca FROM montadora WHERE cod LIKE '%s'""" % cod)
        addservico1cod = self.cursor.fetchall()
        for i in addservico1cod:
            self.entradaMarcaA.insert(END, i)

        self.listatec.destroy()

        self.desconecta_Glac()
    def busca_automovelA(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.conecta_Glac()


        self.entradaAutA.insert(END, '%')
        autom = self.entradaAutA.get()

        lista = self.cursor.execute("""SELECT  automoveis.cod_aut, automoveis.automovel, montadora.marca FROM automoveis, montadora
       	WHERE montadora.cod = automoveis.montad  AND automoveis.automovel LIKE '%s'  ORDER BY automovel ASC;
       		""" % autom)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.entradaAutA.delete(0, END)

        self.desconecta_Glac()
    def busca_autoA(self):
        ### Widgets - Listar tecnicos ###
        self.entradaMarcaA.insert(END, '%')

        veicAuto = self.entradaMarcaA.get()
        self.conecta_Glac()

        self.listatec = Tk()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("320x220")
        self.listatec.resizable(FALSE, FALSE)
        self.listatec1 = Listbox(self.listatec, width=5, height=12, bd=4, fg='brown', font=('Verdana', '9', 'bold'))
        self.listatec1.place(x=7, y=22)
        self.listatec12 = Listbox(self.listatec, width=25, height=12, bd=4, fg='brown', font=('Verdana', '9', 'bold'))
        self.listatec12.place(x=50, y=22)

        self.barra12 = Scrollbar(self.listatec, orient='vertical', command=self.OnTecA)
        self.barra12.place(x=280, y=22, width=25, height=190)
        self.listatec1.configure(yscroll=self.barra12.set)

        # Binding da listbox
        self.listatec1.bind('<Button-1>', self.add_autobindA)

        self.CabSP = Label(self.listatec, text="Cod        ", fg='darkblue', bg='gray75',
                           font=('Century', '10', 'bold', 'italic'))
        self.CabSP.place(x=2, y=1)

        tec = self.cursor

        tec.execute("""SELECT cod FROM montadora WHERE marca LIKE '%s' ORDER BY marca ASC""" % veicAuto)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listatec1.insert(END, i)

        tec12 = self.cursor

        tec12.execute("""SELECT marca FROM montadora WHERE marca LIKE '%s' ORDER BY marca ASC""" % veicAuto)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listatec12.insert(END, i)

        tec22 = self.cursor

        self.entradaMarcaA.delete(0, END)
        self.entradaMarca2A.delete(0, END)

        self.desconecta_Glac()
    def carrega_automovelA(self):
        cod_aut = self.entradaCod_autA.get()
        self.conecta_Glac()

        nomeaut = self.cursor

        self.entradaAutA.delete(0, END)

        self.entradaMarcaA.delete(0, END)
        self.entradaMarca2A.delete(0, END)

        nomeaut.execute(
            "SELECT automovel FROM automoveis, montadora WHERE montadora.cod = automoveis.montad AND cod_aut = '%s'" % cod_aut)
        consultaautomovel = self.cursor.fetchall()
        for i in consultaautomovel:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaAutA.insert(END, i)

        nomemarca = self.cursor
        nomemarca.execute(
            "SELECT marca FROM automoveis, montadora WHERE montadora.cod = automoveis.montad AND cod_aut = '%s'" % cod_aut)
        consultamarca = self.cursor.fetchall()
        for i in consultamarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarcaA.insert(END, i)

        nomemarca2 = self.cursor
        nomemarca2.execute(
            "SELECT montad FROM automoveis, montadora WHERE montadora.cod = automoveis.montad AND cod_aut = '%s'" % cod_aut)
        consultamarca2 = self.cursor.fetchall()
        for i in consultamarca2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarca2A.insert(END, i)

        self.desconecta_Glac()
    def del_automovelA(self):

        cod_aut = self.entradaCod_autA.get()
        self.conecta_Glac()

        self.cursor.execute(""" DELETE FROM automoveis WHERE cod_aut=?;""", (cod_aut,))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor
        self.cursor.execute("""SELECT automoveis.cod_aut, automoveis.automovel, montadora.marca FROM automoveis, montadora
       		WHERE montadora.cod = automoveis.montad  ORDER BY automovel ASC;
       		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        self.limpa_automovelA()
        msg = self.m_msgAutDel
        msg += ""
        messagebox.showinfo("GLAC - Altera Automovel", msg)
    def limpa_automovelA(self):
        self.entradaCod_autA.delete(0, END)
        self.entradaAutA.delete(0, END)

        self.entradaMarcaA.delete(0, END)
        self.entradaMarca2A.delete(0, END)
    def mud_automovelA(self):

        cod_aut = self.entradaCod_autA.get()
        automovel = self.entradaAutA.get()
        montad = self.entradaMarca2A.get()
        self.conecta_Glac()

        self.cursor.execute("""
       		UPDATE automoveis SET automovel = ? WHERE cod_aut = ?""", (automovel, cod_aut))
        self.conn.commit()

        self.cursor.execute("""
       		UPDATE automoveis SET montad = ? WHERE cod_aut = ?""", (montad, cod_aut))
        self.conn.commit()

        lista = self.cursor.execute("""SELECT  automoveis.cod_aut, automoveis.automovel, montadora.marca FROM automoveis, montadora
               	WHERE montadora.cod = automoveis.montad  AND automoveis.automovel LIKE '%s'  ORDER BY automovel ASC;
               		""" % automovel)
        lista = self.cursor.fetchall()
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        msg = self.m_msgAutAlt
        msg += ""
        messagebox.showinfo("GLAC - Altera Automovel", msg)
    def OnTecA(self, *args):
        self.listatec1.yview(*args)
        self.listatec12.yview(*args)
    def OnDoubleClickA(self, event):
        self.limpa_automovelA()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3 = self.listaServ.item(n, 'values')
            self.entradaCod_autA.insert(END, col1)

        self.carrega_automovelA()
    def OnVsbA(self, *args):
        self.listaServ.yview(*args)