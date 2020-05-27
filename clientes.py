from objects_glac import *

class Clientes(Objects_Glac):
    def cadcli(self):
        def abreJanela():
            self.janelaCli = Toplevel()
            self.janelaCli.title(self.m_Cadastro + ' ' + self.m_de + ' ' + self.m_Clientes)
            self.janelaCli.configure(background=self.fundo_do_frame)
            self.janelaCli.focus_force()
            self.janelaCli.geometry("800x600")
            self.janelaCli.resizable(TRUE, TRUE)
            self.janelaCli.minsize(width=780, height=450)
            self.janelaCli.transient(self.janela)
            self.janelaCli.focus_force()
            self.janelaCli.grab_set()
        def molduras():
            top2 = Canvas(self.janelaCli, bd=0, bg='#1e3743', highlightbackground= self.borda_frame,
                          highlightthickness=3);
            top2.place(relx=0, rely=0, relwidth=0.0165, relheight=1)
            top3 = Canvas(self.janelaCli, bd=0, bg='#1e3743', highlightbackground=self.borda_frame,
                          highlightthickness=3);
            top3.place(relx=0, rely=0, relwidth=1, relheight=0.1)
            top4 = Canvas(self.janelaCli, bd=0, bg='#1e3743', highlightbackground=self.borda_frame,
                          highlightthickness=3);
            top4.place(relx=0, rely=0.98, relwidth=1, relheight=0.02)
            top5 = Canvas(self.janelaCli, bd=0, bg='#1e3743', highlightbackground=self.borda_frame,
                          highlightthickness=3);
            top5.place(relx=0.98, rely=0.095, relwidth=0.02, relheight=0.905)
            top6 = Canvas(self.janelaCli, bd=0, bg='#1e3743', highlightbackground=self.borda_frame,
                          highlightthickness=3);
            top6.place(relx=0.016, rely=0.5, relwidth=0.967, relheight=0.04)
            top7 = Canvas(self.janelaCli, bd=0, bg='#1e3743', highlightbackground=self.borda_frame,
                          highlightthickness=3);
            top7.place(relx=0.48, rely=0.095, relwidth=0.02, relheight=0.41)

            top2l = Label(self.janelaCli, bd=0, bg='#1e3743');
            top2l.place(relx=0.002, rely=0.01, relwidth=0.012, relheight=0.98)
            top4l = Label(self.janelaCli, bd=0, bg='#1e3743');
            top4l.place(relx=0.002, rely=0.982, relwidth=0.985, relheight=0.016)
            top5l = Label(self.janelaCli, bd=0, bg='#1e3743');
            top5l.place(relx=0.982, rely=0.0945, relwidth=0.017, relheight=0.905)
            top6l = Label(self.janelaCli, bd=0, bg='#1e3743');
            top6l.place(relx=0.014, rely=0.503, relwidth=0.985, relheight=0.033)
            top7l = Label(self.janelaCli, bd=0, bg='#1e3743');
            top7l.place(relx=0.482, rely=0.094, relwidth=0.017, relheight=0.43)
        def tituloCadCli():
            labelTitulo = Label(self.janelaCli, text=self.m_Clientes,
                                bg=self.fundo_do_frame, fg='gray45', font=('Verdana', '12', 'bold'))
            labelTitulo.place(relx=0.016, rely=0.066, relwidth=0.2, relheight=0.03)
        def caixaClientes():
            ##############################################################################
            ###         MOLDURA CLIENTE
            ##############################################################################
            # Label e entry Codigo
            ###############################
            self.codPeLabel.place(relx=0.02, rely=0.102, relwidth=0.06, relheight=0.02)
            self.codPeEntry.place(relx=0.02, rely=0.122, relwidth=0.05, relheight=0.026)
            ###############################
            # Label e entry Nome
            ##############################
            self.nomePeLabel.place(relx=0.02, rely=0.15, relwidth=0.06, relheight=0.02)
            self.nomePeEntry.place(relx=0.02, rely=0.17, relwidth=0.35, relheight=0.03)
            ##############################
            # Label e entry Nasc
            #############################
            self.nascPeLabel.place(relx=0.39, rely=0.15, relwidth=0.05, relheight=0.02)
            self.nascDiaPeEntry.place(relx=0.39, rely=0.17, relwidth=0.02, relheight=0.03)
            self.nascMesPeEntry.place(relx=0.41, rely=0.17, relwidth=0.02, relheight=0.03)
            self.nascAnoPeEntry.place(relx=0.43, rely=0.17, relwidth=0.04, relheight=0.03)
            ###############################
            #    Endereço
            ###############################
            self.logradPeLabel.place(relx=0.02, rely=0.2, relwidth=0.08, relheight=0.02)
            self.logradPeEntry.place(relx=0.02, rely=0.22, relwidth=0.38, relheight=0.03)

            ###############################
            # numero
            self.numPeLabel.place(relx=0.41, rely=0.2, relwidth=0.07, relheight=0.02)
            self.numPeEntry.place(relx=0.41, rely=0.22, relwidth=0.06, relheight=0.03)
            ###############################
            # Complemento
            self.complemPeLabel.place(relx=0.02, rely=0.25, relwidth=0.12, relheight=0.02)
            self.complemPeEntry.place(relx=0.02, rely=0.27, relwidth=0.22, relheight=0.03)
            ###############################
            # Bairro
            self.bairroPeLabel.place(relx=0.25, rely=0.25, relwidth=0.06, relheight=0.02)
            self.bairroPeEntry.place(relx=0.25, rely=0.27, relwidth=0.22, relheight=0.03)
            #################################
            # Cidade
            self.cidadePeLabel.place(relx=0.02, rely=0.3, relwidth=0.06, relheight=0.02)
            self.cidadePeEntry.place(relx=0.02, rely=0.32, relwidth=0.41, relheight=0.03)
            ################################
            # UF
            self.ufPeLabel.place(relx=0.44, rely=0.3, relwidth=0.03, relheight=0.02)
            self.ufPeEntry.place(relx=0.44, rely=0.32, relwidth=0.03, relheight=0.03)
            #################################
            # Fones
            self.fone1Pelabel.place(relx=0.02, rely=0.35, relwidth=0.06, relheight=0.02)
            self.fone1PeEntry.place(relx=0.02, rely=0.37, relwidth=0.03, relheight=0.03)
            self.fone1PeEntry2.place(relx=0.06, rely=0.37, relwidth=0.12, relheight=0.03)

            self.fone2Pelabel.place(relx=0.24, rely=0.35, relwidth=0.06, relheight=0.02)
            self.fone2PeEntry.place(relx=0.24, rely=0.37, relwidth=0.03, relheight=0.03)
            self.fone2PeEntry2.place(relx=0.28, rely=0.37, relwidth=0.12, relheight=0.03)
            ################################
            # Cep
            self.cepPeLabel.place(relx=0.02, rely=0.4, relwidth=0.06, relheight=0.02)
            self.cepPeBt.place(relx=0.02, rely=0.42, relwidth=0.04, relheight=0.03)
            self.cepPeEntry.place(relx=0.06, rely=0.42, relwidth=0.07, relheight=0.03)
            ###############################
            # cpf cnpj
            self.cnpjPeLabel.place(relx=0.14, rely=0.4, relwidth=0.05, relheight=0.02)
            self.cnpjPeEntry.place(relx=0.14, rely=0.42, relwidth=0.16, relheight=0.03)

            self.cpfPeLabel.place(relx=0.31, rely=0.4, relwidth=0.05, relheight=0.02)
            self.cpfPeEntry.place(relx=0.31, rely=0.42, relwidth=0.16, relheight=0.03)
            ################################
            # Obs
            self.obsPeLabel.place(relx=0.02, rely=0.45, relwidth=0.05, relheight=0.02)
            self.obsPeEntry.place(relx=0.02, rely=0.47, relwidth=0.22, relheight=0.028)
            ################################
            # E-mail
            self.emailPeLabel.place(relx=0.25, rely=0.45, relwidth=0.05, relheight=0.02)
            self.emailPeEntry.place(relx=0.25, rely=0.47, relwidth=0.22, relheight=0.028)
        def botoesCliente():
            ##############################################################################################
            ###             BOTOES CLIENTE
            ###  Botao Novo Cliente
            self.botaoAdd.configure(command=self.add_clienteC)
            self.botaoAdd.place(relx=0.24, rely=0.11, relwidth=0.07, relheight=0.04)
            ##############################################################################################
            ### Botao Altera dados do Cliente
            self.botaoMud.configure(command=self.mud_clienteC)
            self.botaoMud.place(relx=0.32, rely=0.11, relwidth=0.07, relheight=0.04)
            ##############################################################################################
            ### Botao deletar dados do Cliente
            self.botaoDel.configure(command=self.deletar_windowC)
            self.botaoDel.place(relx=0.4, rely=0.11, relwidth=0.07, relheight=0.04)
            ##############################################################################################
            ##  Botao limpa
            self.botaolimpa.configure(command=self.limpa_clienteC)
            self.botaolimpa.place(relx=0.075, rely=0.11, relwidth=0.06, relheight=0.04)
            ##############################################################################################
            ###  Botao busca Cabeça
            self.botaobusca.configure(command=self.busca_clienteC)
            self.botaobusca.place(relx=0.15, rely=0.11, width=35)
        def listaClientes():
            ##################################################################################
            ###             MOLDURA TREEVIEW CLIENTE
            self.barracliente = Scrollbar(self.janelaCli, orient='vertical', command=self.OnVsbC)

            self.listaServ = ttk.Treeview(self.janelaCli, height=6, yscrollcommand=self.barracliente.set,
                                          column=("col1", "col2", "col3", "col4"))

            self.listaServ.heading("#0", text="")
            self.listaServ.heading("#1", text=self.m_Codigo)
            self.listaServ.heading("#2", text=self.m_Nome)
            self.listaServ.heading("#3", text='DDD')
            self.listaServ.heading("#4", text=self.m_Fone)

            self.listaServ.column("#0", width=0)
            self.listaServ.column("#1", width=45)
            self.listaServ.column("#2", width=180)
            self.listaServ.column("#3", width=45)
            self.listaServ.column("#4", width=100)

            self.listaServ.place(relx=0.5, rely=0.13, relwidth=0.465, relheight=0.37)

            self.listaServ.configure(yscroll=self.barracliente.set)
            self.barracliente.place(relx=0.965, rely=0.1, relwidth=0.015, relheight=0.4)

            self.listaServ.bind("<Double-1>", self.OnDoubleClickC)
            self.lista1 = self.cursor.execute("""
                                                    SELECT  cod_cli, nome, fone1ddd, fone1 FROM clientes  ORDER BY nome ASC;
                                                    """)
            for i in self.lista1:
                self.listaServ.insert("", END, values=i)
        def tituloListaClientes():
            labelTitulo = Label(self.janelaCli, text=self.m_lista + ' ' + self.m_de + ' ' + self.m_Clientes,
                                bg=self.fundo_do_frame, fg='gray45', font=('Verdana', '12', 'bold'))
            labelTitulo.place(relx=0.5, rely=0.066, relwidth=0.3, relheight=0.03)
        def caixaEquip():
            ###################################################################################
            ####             AUTOMOVEIS

            labelTitulo = Label(self.janelaCli, text=self.m_Automoveis,
                                bg=self.fundo_do_frame, fg='gray45', font=('Verdana', '12', 'bold'))
            labelTitulo.place(relx=0.016, rely=0.51, relwidth=0.2, relheight=0.028)

            ##### Placa
            self.serialEquipLabel.place(relx=0.02, rely=0.55, relwidth=0.1, relheight=0.04)
            self.serialEquipEntry.place(relx=0.02, rely=0.59, relwidth=0.1, relheight=0.04)

            ##### Veiculo
            self.descrVeiculo = Button(self.janelaCli, bd=2, text=self.m_Veiculo, bg='#37609b', fg='white',
                                       font=('Verdana', '8', 'bold'), command=self.busca_autoC)
            self.descrVeiculo.place(relx=0.13, rely=0.55, relwidth=0.1, relheight=0.04)

            self.nomeEquipEntry.place(relx=0.13, rely=0.59, relwidth=0.1, relheight=0.04)

            #### Fabricante
            self.marcaEquipLabel.place(relx=0.24, rely=0.55, relwidth=0.1, relheight=0.04)

            self.marcaEquipEntry.place(relx=0.24, rely=0.59, relwidth=0.1, relheight=0.04)

            #### Cor
            self.corEquipLabel.place(relx=0.35, rely=0.55, relwidth=0.1, relheight=0.04)

            self.corEquipEntry.place(relx=0.35, rely=0.58, relwidth=0.1, relheight=0.06)

            ### Combustivel
            self.combEquipLabel.place(relx=0.46, rely=0.55, relwidth=0.1, relheight=0.04)

            self.combEquipEntry.place(relx=0.46, rely=0.58, relwidth=0.1, relheight=0.06)

            #### Ano
            self.fabrAnoEquipLabel.place(relx=0.57, rely=0.55, relwidth=0.1, relheight=0.04)

            self.fabrAnoEquipEntry.place(relx=0.57, rely=0.59, relwidth=0.1, relheight=0.04)
        def botoesEquip():
            ################################################################################
            ####  Botoes automoveis
            self.botaoAdd2.configure(command=self.add_veiculoC)
            self.botaoAdd2.place(relx=0.68, rely=0.59, relwidth=0.07, relheight=0.04)

            self.botaoMud2.configure(command=self.mud_autoC)
            self.botaoMud2.place(relx=0.76, rely=0.59, relwidth=0.07, relheight=0.04)

            self.botaoDel2.configure(command=self.deletar_windowPlacaC)
            self.botaoDel2.place(relx=0.84, rely=0.59, relwidth=0.07, relheight=0.04)
        def listaEquip():
            ######################################################################################
            ### Widgets - Listar veiculos ###

            self.listaPlaca = ttk.Treeview(self.janelaCli, height=5,
                                           column=("col1", "col2", "col3", "col4", "col5", "col6"))
            self.listaPlaca.heading("#0", text="")
            self.listaPlaca.heading("#1", text=self.m_Placa)
            self.listaPlaca.heading("#2", text=self.m_Veiculo)
            self.listaPlaca.heading("#3", text=self.m_Montadora)
            self.listaPlaca.heading("#4", text=self.m_Cor)
            self.listaPlaca.heading("#5", text=self.m_Combustivel)
            self.listaPlaca.heading("#6", text=self.m_Ano)

            self.listaPlaca.column("#0", width=0)
            self.listaPlaca.column("#1", width=80)
            self.listaPlaca.column("#2", width=120)
            self.listaPlaca.column("#3", width=170)
            self.listaPlaca.column("#4", width=100)
            self.listaPlaca.column("#5", width=100)
            self.listaPlaca.column("#6", width=80)

            # Cria barra de rolagem
            self.barra = Scrollbar(self.janelaCli, orient='vertical', command=self.listaPlaca.yview)

            # Adiciona barra de rolagem
            self.listaPlaca.configure(yscroll=self.barra.set)
            self.barra.place(relx=0.855, rely=0.65, relwidth=0.02, relheight=0.3)

            self.listaPlaca.place(relx=0.05, rely=0.65, relwidth=0.81, relheight=0.3)
            #    Binding da listbox
            self.listaPlaca.bind('<Double-1>', self.bind_autoC)
            ############################################################################
        self.cores();   self.multiGlacx();   abreJanela();  self.custommer_obj();  self.conecta_Glac()
        molduras();  tituloCadCli(); caixaClientes();  botoesCliente(); listaClientes(); tituloListaClientes();
        caixaEquip();  botoesEquip(); listaEquip(); self.desconecta_Glac()

        self.janelaCli.mainloop()
    def carrega_cliente(self):

        self.listNome.delete(0, END)
        self.listEndereco.delete(0, END)
        self.listBairro.delete(0, END)
        self.listMunicipio.delete(0, END)
        self.listCpf.delete(0, END)
        self.listFone.delete(0, END)
        self.listUf.delete(0, END)
        self.listObs.delete(0, END)
        self.entradaCod_aut.delete(0, END)
        self.listAut.delete(0, END)
        self.listAno.delete(0, END)
        self.listMarca.delete(0, END)
        self.listCombustivel.delete(0, END)
        self.listCor.delete(0, END)
        self.placa.delete(0, END)

        self.conecta_Glac()


        cod_cli = self.entradaCod_cli.get()
        nomecur = self.cursor

        nomecur.execute("SELECT UPPER(nome) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultanome = self.cursor.fetchall()
        for i in consultanome:
            i = str(i); i = i.replace('(',''); i = i.replace(')',''); i = i.replace("'",""); i = i.replace(',','')
            self.listNome.insert(END, i)
            print(i)

        nomeend = self.cursor
        nomeend.execute("""SELECT UPPER(endereco), "Nº", numcasa
            FROM clientes WHERE cod_cli = '%s' """ % cod_cli)
        consultaend = self.cursor.fetchall()
        for i in consultaend:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listEndereco.insert(END, i)
            print(i)

        nomebairro = self.cursor
        nomebairro.execute("SELECT UPPER(bairro) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultabairro = self.cursor.fetchall()
        for i in consultabairro:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listBairro.insert(END, i)
            print(i)

        nomemunicipio = self.cursor
        nomemunicipio.execute("SELECT UPPER(municipio) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultamunicipio = self.cursor.fetchall()
        for i in consultamunicipio:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listMunicipio.insert(END, i)
            print(i)

        nomecpf = self.cursor
        nomecpf.execute("SELECT cpf FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacpf = self.cursor.fetchall()
        for i in consultacpf:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCpf.insert(END, i)
            print(i)

        nomefone = self.cursor
        nomefone.execute("SELECT fone1ddd, fone1 FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone = self.cursor.fetchall()
        for i in consultafone:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listFone.insert(END, i)
            print(i)

        nomeuf = self.cursor
        nomeuf.execute("SELECT UPPER(uf) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultauf = self.cursor.fetchall()
        for i in consultauf:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listUf.insert(END, i)
            print(i)

        nomeobs = self.cursor
        nomeobs.execute("SELECT obs FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaobs = self.cursor.fetchall()
        for i in consultaobs:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listObs.insert(END, i)
            print(i)

        pla = self.cursor
        pla.execute("SELECT placa FROM frota, clientes WHERE idcliente = cod_cli and cod_cli = '%s'" % cod_cli)
        consultapla = self.cursor.fetchall()
        for i in consultapla:
            self.entradaCod_aut.insert(END, i)

        self.desconecta_Glac()

        def carrega_cliente_a(event):
            self.carrega_cliente()
    def add_autobindC(self, event):
        # codServ1.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.listatec1.selection()
        for n in self.listatec1.selection():
            col1, col2, col3 = self.listatec1.item(n, 'values')
            self.nomeEquipEntry.insert(END, col2)
            self.marcaEquipEntry.insert(END, col3)
            self.entradaVeiculo2.insert(END, col1)

        cod = self.entradaVeiculo2.get()

        self.conecta_Glac()

        self.cursor.execute(
            """SELECT montad FROM automoveis WHERE cod_aut LIKE '%s'""" % cod)
        addservico1cod = self.cursor.fetchall()
        for i in addservico1cod:
            self.marcaEquipEntry.insert(END, i)

        self.desconecta_Glac()

        self.listatec.destroy()
        ###############
    def add_clienteC(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        self.variaveisCliente()
        self.variaveisVeiculo()

        self.cursor.execute("""
              	INSERT INTO clientes ( nome, nascdia, nascmes, nascano, endereco, numcasa,
           	    complemento, bairro, municipio, uf, fone1ddd, fone1, fone2ddd, fone2, cep,
           	    cpf, rg, email, obs)
           	    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (self.cadcli_nome, self.cadcli_nascdia, self.cadcli_nascmes, self.cadcli_nascano,
                        self.cadcli_endereco, self.cadcli_numcasa, self.cadcli_complemento, self.cadcli_bairro,
                        self.cadcli_municipio, self.cadcli_uf, self.cadcli_fone1ddd, self.cadcli_fone1,
                        self.cadcli_fone2ddd, self.cadcli_fone2, self.cadcli_cep, self.cadcli_cpf,
                        self.cadcli_cnpj, self.cadcli_email, self.cadcli_obs))
        self.conn.commit()

        msg = self.m_msgClienteAdd
        msg += ""
        messagebox.showinfo("GLAC ", msg)

        lista1 = self.cursor.execute("""
        	  	SELECT  cod_cli, nome, fone1ddd, fone1 FROM clientes  ORDER BY nome ASC;
            """)
        for i in lista1:
            self.listaServ.insert("", END, values=i)
        self.conn.commit()
        self.limpa_clienteC()
        self.desconecta_Glac()
        self.janelaCli.destroy()
        self.cadcli()
    def add_veiculoC(self):
        self.variaveisCliente()
        self.variaveisVeiculo()

        cod_cli = self.codPeEntry.get()

        motor = '0'

        self.conecta_Glac()

        self.cursor.execute("""
    	    	INSERT INTO frota ( idcliente, placa, veiculo, montadora, ano, combust, cor)
    	    	VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                       (self.cadcli_cod, self.cadcli_placa, self.cadcli_montadora,
                        self.cadcli_veiculo, self.cadcli_ano, self.cadcli_combust, self.cadcli_cor))
        self.conn.commit()

        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
                    	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()

        msg = self.m_msgAutAdd
        messagebox.showinfo("GLAC ", msg)
        self.janelaCli.destroy()
        self.cadcli()
    def busca_clienteC(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        self.nomePeEntry.insert(END, '%')
        nome = self.nomePeEntry.get()
        self.cursor.execute(
            """SELECT cod_cli, nome, fone1ddd, fone1 FROM clientes WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome)
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listaServ.insert("", END, values=i)

        self.limpa_clienteC()

        self.desconecta_Glac()
    def busca_autoC(self, *args):
        # self.listatec1.yview(*args)

        ### Widgets - Listar tecnicos ###

        self.nomeEquipEntry.insert(END, '%')

        veicAuto = self.nomeEquipEntry.get()

        self.listatec = Tk()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("420x240")
        self.listatec.resizable(FALSE, FALSE)
        ##########
        self.listatec1 = ttk.Treeview(self.listatec, height=10, column=("col1", "col2", "col3"))
        self.listatec1.heading("#0", text="")
        self.listatec1.heading("#1", text= 'Cod')
        self.listatec1.heading("#2", text= self.m_Automovel)
        self.listatec1.heading("#3", text= self.m_Marca)

        self.listatec1.column("#0", width=0)
        self.listatec1.column("#1", width=40)
        self.listatec1.column("#2", width=180)
        self.listatec1.column("#3", width=150)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.listatec, orient='vertical', command=self.listatec1.yview)

        # Adiciona barra de rolagem
        self.listatec1.configure(yscroll=self.barra.set)
        self.barra.place(x=377, y=6, width=30, height=225)

        self.listatec1.place(x=5, y=5)
        self.conecta_Glac()


        self.cursor.execute("""SELECT cod_aut, automovel, marca FROM automoveis, montadora WHERE montadora.cod = automoveis.montad
             AND automovel LIKE '%s' ORDER BY automovel ASC""" % veicAuto)

        rows = self.cursor.fetchall()
        for row in rows:
            self.listatec1.insert("", END, values=row)

        # Binding da listbox
        self.listatec1.bind('<Double-1>', self.add_autobindC)

        self.desconecta_Glac()

    def bind_autoC(self, event):
        #codServ1.delete(0, END)
        self.limpa_entryautoC()
        self.listaPlaca.selection()

        for n in self.listaPlaca.selection():
            col1, col2, col3, col4, col5, col6 = self.listaPlaca.item(n, 'values')

        self.serialEquipEntry.insert(END, col1)
        self.nomeEquipEntry.insert(END, col3)
        self.marcaEquipEntry.insert(END, col2)
        self.entradaVeiculo2.insert(END, 0)
        #self.entradaMontadora2.insert(END, col8)
        self.codEquipEntry.insert(END, 0)
        self.corvar.set(col4)
        self.combvar.set(col5)
        self.fabrAnoEquipEntry.insert(END, col6)
    def carrega_clienteC(self):
        cod_cli = self.codPeEntry.get()
        self.limpa_clienteC2()

        self.conecta_Glac()

        self.cursor.execute("SELECT UPPER(nome) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacli = self.cursor.fetchall()
        for i in consultacli:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.nomePeEntry.insert(END, i)

        self.cursor.execute("SELECT nascdia FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultadia = self.cursor.fetchall()
        for i in consultadia:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.nascDiaPeEntry.insert(END, i)

        self.cursor.execute("SELECT nascmes FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultames = self.cursor.fetchall()
        for i in consultames:
            self.nascMesPeEntry.insert(END, i)

        self.cursor.execute("SELECT nascano FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultano = self.cursor.fetchall()
        for i in consultano:
            self.nascAnoPeEntry.insert(END, i)

        self.cursor.execute("SELECT numcasa FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultanum = self.cursor.fetchall()
        for i in consultanum:
            self.numPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(complemento) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacompl = self.cursor.fetchall()
        for i in consultacompl:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.complemPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(email) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaemail = self.cursor.fetchall()
        for i in consultaemail:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.emailPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(endereco) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaend = self.cursor.fetchall()
        for i in consultaend:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.logradPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(bairro) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultabairro = self.cursor.fetchall()
        for i in consultabairro:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.bairroPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(municipio) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultamunicipio = self.cursor.fetchall()
        for i in consultamunicipio:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.cidadePeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(uf) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultauf = self.cursor.fetchall()
        for i in consultauf:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.ufPeEntry.insert(END, i)

        self.cursor.execute("SELECT fone1ddd FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone1ddd = self.cursor.fetchall()
        for i in consultafone1ddd:
            self.fone1PeEntry.insert(END, i)

        self.cursor.execute("SELECT fone1 FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone1 = self.cursor.fetchall()
        for i in consultafone1:
            self.fone1PeEntry2.insert(END, i)

        self.cursor.execute("SELECT fone2ddd FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone2ddd = self.cursor.fetchall()
        for i in consultafone2ddd:
            self.fone2PeEntry.insert(END, i)

        self.cursor.execute("SELECT fone2 FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultafone2 = self.cursor.fetchall()
        for i in consultafone2:
            self.fone2PeEntry2.insert(END, i)

        self.cursor.execute("SELECT cep FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacep = self.cursor.fetchall()
        for i in consultacep:
            self.cepPeEntry.insert(END, i)

        self.cursor.execute("SELECT cpf FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacpf = self.cursor.fetchall()
        for i in consultacpf:
            self.cpfPeEntry.insert(END, i)

        self.cursor.execute("SELECT rg FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultarg = self.cursor.fetchall()
        for i in consultarg:
            self.cnpjPeEntry.insert(END, i)

        self.cursor.execute("SELECT UPPER(obs) FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultaobs = self.cursor.fetchall()
        for i in consultaobs:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.obsPeEntry.insert(END, i)


        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
    	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
    def OnVsbC(self, *args):
        self.listaServ.yview(*args)
    def OnMouseWheelC(self, event):
        self.listaServ.yview("scroll", event.delta, "units")

        return "break"
    def OnDoubleClickC(self, *args):
        self.limpa_clienteC()

        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1,col2, col3, col4 = self.listaServ.item(n, 'values')
            self.codPeEntry.insert(END, col1)

        self.carrega_clienteC()
    def mud_autoC(self):
        self.variaveisCliente()
        self.variaveisVeiculo()

        cod_cli = self.codPeEntry.get()
        self.conecta_Glac()

        self.cursor.execute(""" UPDATE frota SET veiculo = ?, ano = ?, placa = ?,
            idcliente = ?, combust = ?, montadora = ?, cor = ? WHERE placa = ? AND idcliente = ?""",
                       (self.cadcli_veiculo, self.cadcli_ano, self.cadcli_placa, cod_cli,
                        self.cadcli_combust, self.cadcli_montadora,
                        self.cadcli_cor, self.cadcli_placa, cod_cli))
        self.conn.commit()

        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
            	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
        msg = self.m_msgVeiculoAlt
        msg += ""
        messagebox.showinfo("GLAC ", msg)
        self.carrega_clienteC()
        self.janelaCli.destroy()
        self.cadcli()
    def mud_clienteC(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.conecta_Glac()

        self.variaveisCliente()
        self.variaveisVeiculo()

        self.cursor.execute("""
    	    UPDATE clientes SET nome = ?, endereco = ?, bairro = ?, municipio = ?,
    	    uf = ?, cep = ?, cpf = ?, rg = ?, obs = ?, email = ?, fone1ddd = ?, fone1 = ?,
    	    fone2ddd = ?, fone2 = ?, complemento = ?, numcasa = ?, nascdia = ?, nascmes = ?, nascano = ?
    	    WHERE cod_cli = ?""",
                       (self.cadcli_nome, self.cadcli_endereco, self.cadcli_bairro, self.cadcli_municipio,
                        self.cadcli_uf, self.cadcli_cep, self.cadcli_cpf, self.cadcli_cnpj, self.cadcli_obs,
                        self.cadcli_email, self.cadcli_fone1ddd, self.cadcli_fone1, self.cadcli_fone2ddd,
                        self.cadcli_fone2, self.cadcli_complemento, self.cadcli_numcasa, self.cadcli_nascdia,
                        self.cadcli_nascmes, self.cadcli_nascano, self.cadcli_cod))
        self.conn.commit()

        lista = self.cursor.execute("""SELECT cod_cli, nome, fone1ddd, fone1 FROM clientes ORDER BY nome ASC;
    	    	""")

        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()

        msg = self.m_msgClienteAlt
        msg += ""
        messagebox.showinfo("GLAC - Clientes", msg)
        self.janelaCli.destroy()
        self.cadcli()
    def limpa_entryautoC(self):
        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        #self.corEquipEntry.delete(0, END)
        #self.combEquipEntry.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
    def limpa_clienteC(self):
        self.codPeEntry.delete(0, END)
        self.nomePeEntry.delete(0, END)
        self.nascDiaPeEntry.delete(0, END)
        self.nascMesPeEntry.delete(0, END)
        self.nascAnoPeEntry.delete(0, END)
        self.logradPeEntry.delete(0, END)
        self.numPeEntry.delete(0, END)
        self.complemPeEntry.delete(0, END)
        self.bairroPeEntry.delete(0, END)
        self.cidadePeEntry.delete(0, END)
        self.ufPeEntry.delete(0, END)
        self.fone1PeEntry.delete(0, END)
        self.fone1PeEntry2.delete(0, END)
        self.fone2PeEntry.delete(0, END)
        self.fone2PeEntry2.delete(0, END)
        self.cepPeEntry.delete(0, END)
        self.cnpjPeEntry.delete(0, END)
        self.cpfPeEntry.delete(0, END)
        self.obsPeEntry.delete(0, END)
        self.emailPeEntry.delete(0, END)

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.limpa_entryautoC()
    def limpa_clienteC2(self):
        #self.codPeEntry.delete(0, END)
        self.nomePeEntry.delete(0, END)
        self.nascDiaPeEntry.delete(0, END)
        self.nascMesPeEntry.delete(0, END)
        self.nascAnoPeEntry.delete(0, END)
        self.logradPeEntry.delete(0, END)
        self.numPeEntry.delete(0, END)
        self.complemPeEntry.delete(0, END)
        self.bairroPeEntry.delete(0, END)
        self.cidadePeEntry.delete(0, END)
        self.ufPeEntry.delete(0, END)
        self.fone1PeEntry.delete(0, END)
        self.fone1PeEntry2.delete(0, END)
        self.fone2PeEntry.delete(0, END)
        self.fone2PeEntry2.delete(0, END)
        self.cepPeEntry.delete(0, END)
        self.cnpjPeEntry.delete(0, END)
        self.cpfPeEntry.delete(0, END)
        self.obsPeEntry.delete(0, END)
        self.emailPeEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.limpa_entryautoC()
    def del_clienteC(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        cod_cli = self.codPeEntry.get()

        self.cursor.execute("""
            	DELETE FROM frota WHERE idcliente=?""", (cod_cli,))
        self.conn.commit()
        self.cursor.execute("""
    	        DELETE FROM clientes WHERE cod_cli=?""", (cod_cli,))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        lista = self.cursor.execute("""
    		SELECT cod_cli, nome, fone1ddd, fone1 FROM clientes  ORDER BY nome ASC
    	""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.limpa_clienteC()

        self.desconecta_Glac()
        self.listatec.destroy()
    def deletar_windowC(self):
        self.listatec = Tk()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("270x85")
        self.listatec.resizable(FALSE, FALSE)
        ##########
        def btnao():
            self.listatec.destroy()

        self.MensLabel = Label(self.listatec, text = self.m_msgCertezaDel, bg = 'gray75'
                               , font=('Verdana', '7', 'bold'))
        self.MensLabel.place(x=10, y=10)

        self.BtSim = Button(self.listatec,text= self.m_Sim, bd=2, bg = '#37609b', fg ='white',
                            font=('Verdana', '10', 'bold'), command=self.del_clienteC)
        self.BtSim.place(x=50, y=50, width = 70)

        self.BtNao = Button(self.listatec,text= self.m_Nao, bd=2, bg = 'gray25', fg ='white',
                            font=('Verdana', '10', 'bold'), command= btnao)
        self.BtNao.place(x=150, y=50, width = 70)
    def del_placaC(self):
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        cod_cli = self.codPeEntry.get()
        placa = self.serialEquipEntry.get()
        self.conecta_Glac()

        self.cursor.execute("""
            	DELETE FROM frota WHERE placa =? AND idcliente = ?""", ( placa, cod_cli))
        self.conn.commit()

        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
            	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
        self.limpa_entryautoC()
        self.listatec.destroy()
    def deletar_windowPlacaC(self):
        self.listatec = Tk()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("270x85")
        self.listatec.resizable(FALSE, FALSE)
        ##########

        def btnao():
            self.listatec.destroy()

        self.MensLabel = Label(self.listatec, text = self.m_msgCertezaDel, bg = 'gray75'
                               , font=('Verdana', '7', 'bold'))
        self.MensLabel.place(x=10, y=10)

        self.BtSim = Button(self.listatec,text= self.m_Sim, bd=2, bg = '#37609b', fg ='white',
                            font=('Verdana', '10', 'bold'), command=self.del_placaC)
        self.BtSim.place(x=50, y=50, width = 70)

        self.BtNao = Button(self.listatec,text= self.m_Nao, bd=2, bg = 'gray25', fg ='white',
                            font=('Verdana', '10', 'bold'), command= btnao)
        self.BtNao.place(x=150, y=50, width = 70)
    def variaveisCliente(self):
        self.cadcli_cod = self.codPeEntry.get()
        self.cadcli_nome = self.nomePeEntry.get()
        self.cadcli_nascdia = self.nascDiaPeEntry.get()
        self.cadcli_nascmes = self.nascMesPeEntry.get()
        self.cadcli_nascano = self.nascAnoPeEntry.get()
        self.cadcli_endereco = self.logradPeEntry.get()
        self.cadcli_numcasa = self.numPeEntry.get()
        self.cadcli_complemento = self.complemPeEntry.get()
        self.cadcli_bairro = self.bairroPeEntry.get()
        self.cadcli_municipio = self.cidadePeEntry.get()
        self.cadcli_uf = self.ufPeEntry.get()
        self.cadcli_fone1ddd = self.fone1PeEntry.get()
        self.cadcli_fone1 = self.fone1PeEntry2.get()
        self.cadcli_fone2ddd = self.fone2PeEntry.get()
        self.cadcli_fone2 = self.fone2PeEntry2.get()
        self.cadcli_cep = self.cepPeEntry.get()
        self.cadcli_cpf = self.cpfPeEntry.get()
        self.cadcli_cnpj = self.cnpjPeEntry.get()
        self.cadcli_email = self.emailPeEntry.get()
        self.cadcli_obs = self.obsPeEntry.get()
    def variaveisVeiculo(self):
        self.cadcli_veiculoId = self.codEquipEntry.get()
        self.cadcli_MontadoraId = self.entradaMontadora2.get()
        self.cadcli_veiculo = self.nomeEquipEntry.get()
        self.cadcli_ano = self.fabrAnoEquipEntry.get()
        self.cadcli_placa = self.serialEquipEntry.get()
        self.cadcli_montadora = self.marcaEquipEntry.get()
        self.cadcli_combust = self.combvar.get()
        self.cadcli_cor = self.corvar.get()
    def cep(self):
            self.logradPeEntry.delete(0, END)
            self.bairroPeEntry.delete(0, END)
            self.cidadePeEntry.delete(0, END)
            self.ufPeEntry.delete(0, END)
            try:
                self.cep = self.cepPeEntry.get()
                endcep = pycep_correios.consultar_cep(self.cep)

                self.logradPeEntry.insert(END, endcep['end'])
                self.bairroPeEntry.insert(END, endcep['bairro'])
                self.cidadePeEntry.insert(END, endcep['cidade'])
                self.ufPeEntry.insert(END, endcep['uf'])

            except ExcecaoPyCEPCorreios as exc:
                msg = 'Not find - Não encontrado'
                messagebox.showinfo("GLAC", msg)
