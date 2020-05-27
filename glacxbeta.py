####  Carrega todos modulos necessarios a execucao do programa
from modulos import *;from functions import *;import licence;from otherswindows import *;from multilanguage import *
from clientes import *;from automoveis import *;from servicos import *;from estoque import *;from produtos import *
from tecnicos import *;from fornecedores import *;from marcaProdutos import *;from empresa import *;from financeiro import *
from atualizaMaodeObra import *;from pagamentoOrc import *;from printRelatorios import *

### cria variavel que da nome a janela principal
janela = Tk()

##############################################################################################################
#### Criando variavel de consulta dos produtos e serviços para o autocomplete
conn = sqlite3.connect("glac.db")
cursor = conn.cursor()
lista2 = cursor
lista2.execute("""SELECT cod_sp, '*****', LOWER(servprod), ' - ', tiposerv, ' - ' , LOWER(id_marcaprod) 
    FROM servprod """)
lista3 = cursor.fetchall()
zlist = []
for tup in lista3:
    t = str(tup).replace("('","").replace("',)","").replace(")","").replace("'","").replace(",","").replace("(","")
    zlist.append(t)
cursor.close()

##################################################################################################################

class AutocompleteEntrySP(Entry):
    def __init__(self, lista2, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.lista = zlist
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()
        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection); self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)

        self.lb_up = False
    def changed(self, name, index, mode):
        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = Listbox(width = 70, height = 15)
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.lb_up = True
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END, w)

            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
    def selection(self, event):
        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)
    def up(self, event):
        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index) - 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)
    def down(self, event):
        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:
                self.lb.selection_clear(first=index)
                index = str(int(index) + 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)
    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]

### Classe principal que chama todas as outras
class MeuOrc(Validadores, Functions, Formulas, Multilanguage, OthersWindows, Clientes, Automoveis, Servicos, Estoque,
            Produtos, Tecnicos, Fornecedores,MarcaProdutos, Empresa, Financeiro, MaodeObra, PagamentoOrc, PrintRel):
    
    def __init__(self):
        self.multiGlacx();
        self.cores();
        self.images_base64()
        ###########################################################################
        ### Variaveis dos Widgets desenhados
        self.orcamentoLb = PhotoImage(data=base64.b64decode(self.ORCAMENTOLB))
        self.add = PhotoImage(data=base64.b64decode(self.ADD))
        self.seulogo = PhotoImage(data=base64.b64decode(self.SEULOGO))
        self.cadcliBt = PhotoImage(data=base64.b64decode(self.CADCLI_BT))
        self.cadautBt = PhotoImage(data=base64.b64decode(self.CADAUT_BT))
        self.cadprodBt = PhotoImage(data=base64.b64decode(self.CADPROD_BT))
        self.cadfornecBt = PhotoImage(data=base64.b64decode(self.CADFORNEC_BT))
        self.cadservBt = PhotoImage(data=base64.b64decode(self.CADSERV_BT))
        self.button_imprime2 = PhotoImage(data=base64.b64decode(self.BTIMPRIME2))
        self.logo_rf = PhotoImage(data=base64.b64decode(self.LOGORF))
        self.norcLb = PhotoImage(data=base64.b64decode(self.LBNORC))
        self.clientBt = PhotoImage(data=base64.b64decode(self.BTCLIENT))
        self.tecnicoBt = PhotoImage(data=base64.b64decode(self.BTTECNICO))
        self.lupaBt = PhotoImage(data=base64.b64decode(self.BTLUPA))
        
        ### Abrindo tela principal
        self.TelaOrc()
    def TelaOrc(self):
        ### Criação da janela
        def abreJanela():
            ### Montagem da janela
            self.janela = janela
            self.janela.title(self.m_Orcamento + self.m_e + self.m_Ordem + self.m_Glac)
            self.janela.configure(background=self.fg_label);
            self.janela.geometry("1000x600")
            self.janela.resizable(TRUE, TRUE);
            self.janela.minsize(width=800, height=500)
            
            self.background_image = PhotoImage(file='landscape.png')
            self.background_label = Label(self.janela, image= self.background_image)
            self.background_label.place(relwidth=1, relheight=1)
        abreJanela()
        
        def validaEntradas():
            ### Nomeando validadores das entradas
            self.vcmd8 = (self.janela.register(self.validate_entry8), "%P")
            self.vcmd6 = (self.janela.register(self.validate_entry6), "%P")
            self.vcmd4 = (self.janela.register(self.validate_entry4), "%P")
            self.vcmd2 = (self.janela.register(self.validate_entry2), "%P")
            self.vcmd8float = (self.janela.register(self.validate_entry8float), "%P")
            self.vcmd9float = (self.janela.register(self.validate_entry9float), "%P")
            self.vcmd4float = (self.janela.register(self.validate_entry4float), "%P")
        validaEntradas()
        ### Chammando a função dos Menus
        self.Menus()
        ### Criação dos containers da tela principal
        
        def containers():
            ###     Primeiro Container da janela
            top = Frame(self.janela, bd=2, bg= '#49708D', highlightbackground=self.borda_frame, highlightthickness=3)
            top.place(relx=0.01, rely=0.005, relwidth=0.98, relheight=0.13)
            self.top = top
            ### Segundo Container da Janela
            top2 = Frame(self.janela, bd=1, bg=self.fundo_da_tela, highlightbackground=self.borda_frame,
                     highlightthickness=1)
            top2.place(relx=0.01, rely=0.14, relwidth=0.98, relheight=0.2)
            self.top2 = top2
        
            ### Terceiro Container da janela
            top3 = Frame(self.janela, bd=1, bg=self.fundo_do_frame, highlightbackground=self.borda_frame,
                     highlightthickness=3);
            top3.place(relx=0.01, rely=0.35, relwidth=0.98, relheight=0.45)
            self.top3 = top3
            ### Quarto Container da Janela
            top4 = Frame(self.janela, width=95, bd=2, bg=self.fundo_do_frame, highlightbackground=self.borda_frame,
                     highlightthickness=3);
            top4.place(relx=0.01, rely=0.805, relwidth=0.98, relheight=0.09)
            self.top4 = top4
            ### Quinto Container da janela
            top5 = Frame(self.janela, bd=2, bg=self.fundo_do_frame, highlightbackground=self.borda_frame,
                     highlightthickness=3)
            top5.place(relx=0.01, rely=0.905, relwidth=0.98, relheight=0.09)
            self.top5 = top5
        containers()
        def molduras():
            ### Moldura dos dados do cliente
            self.FrameCliente = Frame(self.top2, bd=1, bg=self.fundo_do_frame, highlightbackground=self.borda_frame,
                highlightthickness=3);
            self.FrameCliente.place(relx=0.002, rely=0.002, relwidth=0.45, relheight=1)
            ### Lista das placas de veiculos do cliente
            self.FrameAut2 = Frame(self.top2, width=10, bg=self.fundo_do_frame, bd=1, highlightbackground=self.borda_frame,
                highlightthickness=3); self.FrameAut2.place(relx=0.465, rely=0.002, relwidth=0.1, relheight=1)
            ### Moldura dos dados veiculo
            self.FrameAut = Frame(self.top2, bd=1, bg=self.fundo_do_frame, highlightbackground=self.borda_frame,
                highlightthickness=3); self.FrameAut.place(relx=0.58, rely=0.002, relwidth=0.42, relheight=1)
            ### Moldura dos botoes
            self.FrameBot = Frame(self.top, bg='#49708D');
            self.FrameBot.place(relx=0, rely=0, relwidth=0.5, relheight=1)

            self.FrameAbas = Frame(self.top3, bg=self.fundo_do_frame);
            self.FrameAbas.place(relx=0, rely=0, relwidth=1, relheight=1)
            ######################
            self.FrameTec = Frame(self.top4, bg=self.fundo_do_frame);
            self.FrameTec.place(relx=0.005, rely=0.005, relwidth=1, relheight=1)
            ######################
        molduras()
        
        ###########################################################################################################
        ###  Logotipo GlacX - Tela Superior
        self.logo = Label(self.top, image=self.logo_rf, bd=0, bg='#49708D', relief=SUNKEN)
        self.logo.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)
        self.textoLogo = Label(self.top, bg='#49708D', text=self.m_logorf, bd=0, fg=self.bg_label, font=('Comic', '36', 'bold'))
        self.textoLogo.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.6)
        
        ##########################################################################################################
        ### Container dos dados do cliente
        self.contCliente()
        
        #############################################################################################################################
        #### Tecnico de reparo
        self.tecnico = Label(self.FrameTec, bg=self.fundo_do_frame, fg=self.fg_label, text=self.m_Tecnico);
        self.tecnico.place(relx=0.005, rely=0.05, relwidth=0.15, relheight=0.3);
        self.entradaTecnico = Entry(self.FrameTec, bd=1, width=14, fg=self.fg_entry, font=('Verdana', '9', 'bold'));
        self.entradaTecnico.place(relx=0.005, rely=0.45, relwidth=0.15, relheight=0.3);
        self.entradaTecnico.insert(END, '???');
        self.botaotec = Button(self.FrameTec, image=self.tecnicoBt, bd=0, command=self.busca_tecnico);
        self.botaotec.place(relx=0.15, rely=0.1, relwidth=0.04, relheight=0.77);
        
        ##############################################################################################################################
        ##### label e listbox do numero do orcamento
        self.descrNumOrc = Label(self.FrameTec, text=self.m_Numero, bg=self.fundo_do_frame, fg=self.fg_label,
                                 font=('Verdana', '12', 'bold'))
        self.descrNumOrc.place(relx=0.24, rely=0.05, relwidth=0.08, relheight=0.9)
        self.listaNumOrc = Entry(self.FrameTec, width=6, justify='center', bd=3, fg=self.fg_entry,
                                 font=('Verdana', '12', 'bold'))
        self.listaNumOrc.place(relx=0.32, rely=0.28, relwidth=0.08, relheight=0.4)
        ##############################################################################################################################
        #### Botões Orçamento
        ###  Botao Gravar
        self.botaoAbreOrc = Button(self.FrameTec, text=self.m_Gravar, bd=0, bg=self.bg_button_del, fg=self.fg_button,
                                   font=('Aharoni','14', 'bold'), command=self.abre_orc)
        self.botaoAbreOrc.place(relx=0.4, rely=0.24, relwidth=0.07, relheight=0.5)
        ###  Botao Buscar
        self.botaoCarregaOrc = Button(self.FrameTec, text=self.m_Buscar, bd=0, bg=self.bg_button, fg=self.fg_button,
                                      font=('Aharoni','14', 'bold'), command=self.busca_orc)
        self.botaoCarregaOrc.place(relx=0.48, rely=0.24, relwidth=0.07, relheight=0.5)
        ### Botao Alterar
        self.botaoAlteraOrc = Button(self.FrameTec, text=self.m_Alterar, bd=0, bg=self.bg_button, fg=self.fg_button,
                                     font=('Aharoni','14', 'bold'), command=self.altera_orc)
        self.botaoAlteraOrc.place(relx=0.56, rely=0.24, relwidth=0.07, relheight=0.5)
        
        ############################################################################################################################
        ##  Entrada Total
        self.entradatotal = Entry(self.FrameTec, width=10, justify='right', fg=self.fg_entry, bd=1,
                                  font=('Verdana', '12', 'bold'))
        self.entradatotal.place(relx=0.86, rely=0.3, relwidth=0.12, relheight=0.5);
        self.entradatotal2 = Entry(self.FrameTec)
        ############################################################################################################
        ## Botao Total
        self.descrtotal = Button(self.FrameTec, text=self.m_Total, bg=self.bg_button, fg=self.fg_button,
                                 font=('Verdana', '14', 'bold'), command=self.total_orc)
        self.descrtotal.place(relx=0.75, rely=0.25, relwidth=0.1, relheight=0.6)
        #self.totalbotao()
        ############################################################################################################
        #### Caixa de Seleção de Orçamento ou Ordemm de Serviço
        self.entradaTipoorc = Frame(self.top5, bd=2, width=40, bg=self.fundo_do_frame);
        self.entradaTipoorc.columnconfigure(0, weight=1);
        self.entradaTipoorc.rowconfigure(0, weight=1)
        self.entradaTipoorc.place(relx=0.01, rely=0.01, relwidth=0.16, relheight=0.8);
        self.Tipvar = StringVar(self.top5)
        self.TipV = {self.m_Ordem, self.m_Orcamento};
        self.Tipvar.set(self.m_Orcamento)
        self.popupMenu = OptionMenu(self.entradaTipoorc, self.Tipvar, *self.TipV)
        self.labelTip = Label(self.top5, bd=2, bg='gray95', fg=self.fg_label, font=('Verdana', '8', 'bold'))
        self.popupMenu.grid(row=2, column=1)
        #############################################################################################################
        ###  Label Licença
        self.licenciamento = Label(self.top5, text=licence.Licenca, bd=0, bg=self.fundo_do_frame, fg=self.bg_button,
                                   font=('Verdana', '12', 'bold'));
        self.licenciamento.place(relx=0.3, rely=0.05, relwidth=0.3, relheight=0.4)
        ############################################################################################################
        ## Botao Acesse nossa pagina
        self.licenciamentoBt = Button(self.top5, text=self.m_Acesse, bd=1, bg=self.bg_button, fg=self.fg_button,
                                      font=('Verdana', '10', 'bold'), command=self.PaginaRf)
        self.licenciamentoBt.place(relx=0.3, rely=0.6, relwidth=0.3, relheight=0.4)
        ###############################################################################################################
        ###  Botao Imprimir Orçamento
        self.botaoImprimirOrc = Button(self.top5, image=self.button_imprime2, bd=0, bg=self.fundo_do_frame,
                                       command=self.imprime_orc);
        self.botaoImprimirOrc.place(relx=0.74, rely=0.01, relwidth=0.08, relheight=0.95)
        
        def funcpag():
            if self.listaNumOrc.get() == "":
                msg = "É necessário que um Orçamento ou Ordem de Serviço \n" \
                      "esteja devidamente carregada na tela!!!"
                msg += ""
                messagebox.showinfo("GLAC - Pagamentos", msg)
            else:
                self.pagaOrdem()

        
        ##############################################################################################################
        ## Botao Forma de Pagamento
        self.formapag = Button(self.top5, text=self.m_Forma, bg=self.bg_button, font=('Verdana', '8', 'bold'),
                               fg=self.fg_button,
                               command=funcpag);
        self.formapag.place(relx=0.84, rely=0.03, relwidth=0.15, relheight=0.7)

        ##########################################################################################################
        ###  A B A S
        self.abas = Notebook(self.FrameAbas);
        self.frame_aba1 = Frame(self.abas);
        self.frame_aba2 = Frame(self.abas)
        self.frame_aba3 = Frame(self.abas);
        self.frame_aba4 = Frame(self.abas);
        self.frame_aba5 = Frame(self.abas)

        self.frame_aba1.configure(background=self.fundo_do_frame)
        self.frame_aba2.configure(background=self.fundo_do_frame)
        self.frame_aba4.configure(background=self.fundo_do_frame)
        self.frame_aba5.configure(background=self.fundo_do_frame)
        self.label1 = Label(self.frame_aba1);
        self.label1.pack(padx=850, pady=225)

        self.label3 = Label(self.frame_aba3);
        self.label3.pack(padx=850, pady=225)
        self.label4 = Label(self.frame_aba4);
        self.label4.pack(padx=850, pady=225)
        self.label5 = Label(self.frame_aba5);
        self.label5.pack(padx=850, pady=225)
        self.abas.add(self.frame_aba1, text=self.m_Aba3);
        self.abas.add(self.frame_aba2, text=self.m_Aba1)

        self.abas.add(self.frame_aba4, text=self.m_Aba4)
        #self.abas.add(self.frame_aba5, text=self.m_Aba5)
        self.abas.pack(side="bottom")
        ### ABAS
        self.aba1();
        self.aba2();

        self.aba4();
        self.aba5();

    def contCliente(self):
        ####                Container de cadastro do cliente
        # Label do codigo do cliente
        self.descrCod_cli=Label(self.FrameCliente,text=self.m_Codigo+self.m_Pontinhos,font=('Verdana', '8', 'bold'))
        self.descrCod_cli.configure(fg=self.fg_label,bg=self.fundo_do_frame)
        self.descrCod_cli.place(relx=0.01, rely=0.04, relheight= 0.17)
        # Entrada do Codigo do Cliente
        self.entradaCod_cli=Entry(self.FrameCliente)
        self.entradaCod_cli.configure(validate="key",validatecommand=self.vcmd6)
        self.entradaCod_cli.configure(bd=1, width=6, fg=self.fg_entry, bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.entradaCod_cli.place(relx=0.2, rely=0.04, relwidth = 0.13, relheight= 0.17)
        # Botão Carrega
        self.botaoAdd = Button(self.FrameCliente, text = self.m_Buscar, bd=0, bg=self.bg_button, fg=self.fg_button,
            font=('Aharoni','14','bold'),command=self.busca_cliente)
        self.botaoAdd.place(relx=0.34, rely=0.01, relwidth = 0.17, relheight= 0.23)
        # Botão Limpa
        self.botaoLimp = Button(self.FrameCliente, text = self.m_Limpar, bd=0,  bg=self.bg_button, fg=self.fg_button,
            font=('Aharoni','14', 'bold'), command=self.limpa_cliente)
        self.botaoLimp.place(relx=0.52, rely=0.01, relwidth = 0.17, relheight= 0.23)
        ### Variavel do dia de hoje
        hj = date.today()
        # Label data
        self.descrData = Label(self.FrameCliente, text= self.m_Data)
        self.descrData.configure(fg=self.fg_label, bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrData.place(relx=0.7, rely=0.04, relwidth = 0.1, relheight= 0.17)
        # Entrada Dia
        self.entradaDataorc = Entry(self.FrameCliente, fg='darkred', bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.entradaDataorc.configure(width=2, validate="key", validatecommand=self.vcmd2)
        self.entradaDataorc.place(relx=0.8, rely=0.04, relwidth = 0.05, relheight= 0.17)
        self.entradaDataorc.insert(END, hj.day)
        # Entrada Mês
        self.entradaDataorc2 = Entry(self.FrameCliente, width=2, validate="key", font=('Verdana', '8', 'bold'))
        self.entradaDataorc2.configure(validatecommand=self.vcmd2, bg=self.bg_entry, justify='right', fg='darkred')
        self.entradaDataorc2.place(relx=0.85, rely=0.04, relwidth = 0.05, relheight= 0.17)
        self.entradaDataorc2.insert(END, hj.month)
        # Entrada Ano
        self.entradaDataorc3 = Entry(self.FrameCliente, font=('Verdana', '8', 'bold'), fg='darkred')
        self.entradaDataorc3.configure(width=4, validate="key", bg=self.bg_entry, validatecommand=self.vcmd4)
        self.entradaDataorc3.place(relx=0.9, rely=0.04, relwidth = 0.1, relheight= 0.17)
        self.entradaDataorc3.insert(END, hj.year)
        # Label Cliente
        self.descrNome = Label(self.FrameCliente, text= self.m_Cliente + self.m_Pontinhos, font=('Verdana', '8', 'bold'))
        self.descrNome.configure(justify="right", fg=self.fg_label, bg=self.fundo_do_frame)
        self.descrNome.place(relx=0.01, rely=0.24, relheight= 0.15)
        # Entrada do nome do cliente
        self.listNome = Entry(self.FrameCliente, width=40, bd=1, fg=self.fg_entry)
        self.listNome.configure(bg=self.bg_entry, font=('Verdana', '8', 'italic', 'bold'))
        self.listNome.place(relx=0.2, rely=0.24, relwidth = 0.78, relheight= 0.15)
        # Label do Endereço
        self.descrEndereco=Label(self.FrameCliente,text=self.m_Endereco+self.m_Pontinhos,font=('Verdana','8','bold'))
        self.descrEndereco.configure( fg=self.fg_label, bg=self.fundo_do_frame)
        self.descrEndereco.place(relx=0.01, rely=0.39, relheight= 0.15)
        # Entrada do Endereço
        self.listEndereco=Entry(self.FrameCliente,width=40,bd=1,fg=self.fg_entry,font=('Verdana','8','bold','italic'),
            bg = self.bg_entry);self.listEndereco.place(relx=0.2,rely=0.39,relwidth=0.78,relheight= 0.15)
        ############################################
        # Label Bairro
        self.descrBairro=Label(self.FrameCliente,text=self.m_Bairro+self.m_Pontinhos,font=('Verdana', '8', 'bold'))
        self.descrBairro.configure( fg=self.fg_label, bg=self.fundo_do_frame)
        self.descrBairro.place(relx=0.01, rely=0.54,  relheight= 0.15)
        ############################################
        # Entrada Bairro
        self.listBairro=Entry(self.FrameCliente,width=14,bd=1,fg=self.fg_entry,font=('Verdana','8','bold','italic'),
            bg=self.bg_entry); self.listBairro.place(relx=0.2, rely=0.54, relwidth = 0.25, relheight= 0.15)
        ################################################
        # Label Municipio
        self.descrMunicipio = Label(self.FrameCliente, width=6, text= self.m_Cidade, fg=self.fg_label,
            bg=self.fundo_do_frame); self.descrMunicipio.configure(font=('Verdana', '8', 'bold'))
        self.descrMunicipio.place(relx=0.445, rely=0.54, relheight= 0.15)
        ################################################
        # Entrada Municipio
        self.listMunicipio=Entry(self.FrameCliente,width=14,bd=1,fg=self.fg_entry,bg=self.bg_entry,
            font=('Verdana','8','bold','italic'))
        self.listMunicipio.place(relx=0.57,rely=0.54,relwidth=0.27,relheight= 0.15)
        ###############################################
        # Label UF
        self.descrUf=Label(self.FrameCliente,text=self.m_Uf,fg=self.fg_label,font=('Verdana', '8', 'bold'),
            bg = self.fundo_do_frame); self.descrUf.place(relx=0.85, rely=0.54, relwidth = 0.05, relheight= 0.15)
        ###############################################
        # Entrada UF
        self.listUf=Entry(self.FrameCliente,width=3,bd=1,fg=self.fg_entry,font=('Verdana','8','bold', 'italic'),
            bg = self.bg_entry); self.listUf.place(relx=0.91, rely=0.54, relwidth = 0.07, relheight= 0.15)
        ##############################################
        # Label CPF CNPJ
        self.descrCpf=Label(self.FrameCliente,fg=self.fg_label,text= self.m_Cpf+self.m_barra+self.m_Cnpj+
            self.m_Pontinhos,bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrCpf.place(relx=0.01, rely=0.69, relheight= 0.15)
        #############################################
        # Entrada CPF CNPJ
        self.listCpf=Entry(self.FrameCliente,bd=1,fg=self.fg_entry,bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listCpf.place(relx=0.2, rely=0.69, relwidth = 0.3, relheight= 0.15)
        ##############################################
        # Label Fone
        self.descrFone = Label(self.FrameCliente, fg=self.fg_label, text= self.m_Fone, bg=self.fundo_do_frame,
            font=('Verdana','8','bold'));self.descrFone.place(relx=0.55,rely=0.69,relwidth=0.12,relheight=0.15)
        ############################################
        # Entrada Fone
        self.listFone=Entry(self.FrameCliente,width=15,bd=1,fg=self.fg_entry,bg=self.bg_entry,
            font=('Verdana', '8', 'bold'));self.listFone.place(relx=0.68, rely=0.69, relwidth = 0.3, relheight= 0.15)
        ###########################################
        # Label OBS
        self.descrObs=Label(self.FrameCliente,text=self.m_Observacao+self.m_Pontinhos,bg=self.fundo_do_frame,
            fg=self.fg_label,font=('Verdana', '8', 'bold'));self.descrObs.place(relx=0.01, rely=0.84, relheight= 0.15)
        ##########################################
        # Entrada OBS
        self.listObs=Entry(self.FrameCliente,width=40,bd=1,fg=self.fg_entry,bg=self.bg_entry,
            font=('Verdana', '8', 'bold'));self.listObs.place(relx=0.2, rely=0.84, relwidth = 0.78, relheight= 0.15)

        ###  		AUTOMOVEIS
        ###  Listbox da Placa do Automovel

        ###########################################################################################################
        ####  Lista de placas
        self.entradaCod_aut = Listbox(self.FrameAut2, width=11, height=9, bd=3, bg=self.fundo_do_frame,
                                      fg=self.fg_entry,
                                      font=('Verdana', '8', 'bold'))
        self.entradaCod_aut.pack()

        # Binding da listbox da Placa
        self.entradaCod_aut.bind('<Button-1>', self.carrega_automovel)
        # Placa
        self.descrCod_aut = Label(self.FrameAut, text=self.m_Placa + self.m_Pontinhos, width=9, fg=self.fg_label,
                                  bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrCod_aut.place(relx=0, rely=0.01, relwidth=0.2, relheight=0.17)
        self.placa = Entry(self.FrameAut, width=9, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                           font=('Verdana', '8', 'bold'))
        self.placa.place(relx=0.15, rely=0.01, relwidth=0.2, relheight=0.17)
        ###  Label e Entrada Ano
        self.descrAno = Label(self.FrameAut, text=self.m_Ano, fg=self.fg_label, bg=self.fundo_do_frame,
                              font=('Verdana', '8', 'bold'));
        self.descrAno.place(relx=0.45, rely=0.01, relwidth=0.1, relheight=0.17)
        self.listAno = Entry(self.FrameAut, width=5, validate="key", validatecommand=self.vcmd4, bd=1, fg=self.fg_entry,
                             bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listAno.place(relx=0.55, rely=0.01, relwidth=0.2, relheight=0.17)
        ###  Label e Entrada Veiculo
        self.descrAut = Label(self.FrameAut, text=self.m_Veiculo + self.m_Pontinhos, width=9, fg=self.fg_label,
                              bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrAut.place(relx=0, rely=0.20, relwidth=0.22, relheight=0.17)
        self.listAut = Entry(self.FrameAut, width=22, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                             font=('Verdana', '8', 'bold'));
        self.listAut.place(relx=0.15, rely=0.20, relwidth=0.6, relheight=0.17)
        ###  Label e Entrada Marca
        self.descrMarca = Label(self.FrameAut, text=self.m_Marca + self.m_Pontinhos, width=9, fg=self.fg_label,
                                bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrMarca.place(relx=0, rely=0.4, relwidth=0.2, relheight=0.17)
        self.listMarca = Entry(self.FrameAut, width=22, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                               font=('Verdana', '8', 'bold'));
        self.listMarca.place(relx=0.15, rely=0.4, relwidth=0.6, relheight=0.17)
        ###  Label e Entrada Combustivel
        self.descrCombustivel = Label(self.FrameAut, text=self.m_Combustivel + self.m_Pontinhos, width=9,
                                      fg=self.fg_label,
                                      bg=self.fundo_do_frame, font=('Verdana', '8', 'bold'))
        self.descrCombustivel.place(relx=0, rely=0.6, relwidth=0.28, relheight=0.17)
        self.listCombustivel = Entry(self.FrameAut, width=22, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                     font=('Verdana', '8', 'bold'));
        self.listCombustivel.place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.17)
        #########################################################
        ###  Label e Entrada km
        self.descrObs = Label(self.FrameAut, text=self.m_Km + self.m_Pontinhos);
        self.descrObs.configure(fg=self.fg_label, bg=self.fundo_do_frame, font=('Comic', '10', 'bold'))
        self.descrObs.place(relx=0, rely=0.8, relwidth=0.15, relheight=0.17)
        self.entradaObs = Entry(self.FrameAut, validate="key", validatecommand=self.vcmd9float)
        self.entradaObs.configure(fg='darkred', bg='lightblue', font=('Verdana', '8', 'bold'))
        self.entradaObs.place(relx=0.15, rely=0.8, relwidth=0.2, relheight=0.17)
        ###########################################################################
        ###  Label e Entrada Cor
        self.descrCor = Label(self.FrameAut);
        self.descrCor.configure(text=self.m_Cor, fg=self.fg_label, bg=self.fundo_do_frame,
                                font=('Verdana', '8', 'bold'))
        self.descrCor.place(relx=0.45, rely=0.8, relwidth=0.1, relheight=0.17)
        self.listCor = Entry(self.FrameAut, width=12, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                             font=('Verdana', '8', 'bold'))
        self.listCor.place(relx=0.55, rely=0.8, relwidth=0.2, relheight=0.17)

        ##########################################################################
        #### Botoes
        self.ClientBot = Button(self.FrameBot, image=self.cadcliBt, bd=0, bg= '#49708D', command=self.cadcli)
        self.ClientBot.place(relx=0.03, rely=0, relwidth=0.14, relheight=0.8)
        self.ClientLbBt = Label(self.FrameBot, text=self.m_Clientes, bd=2, bg = '#49708D', fg= 'white',
                                font=('Verdana', '8', 'bold'))
        self.ClientLbBt.place(relx=0.03, rely=0.82, relwidth=0.14, relheight=0.18)

        self.FornecBot = Button(self.FrameBot, image=self.cadfornecBt, bd=0, bg= '#49708D', command=self.cadforn)
        self.FornecBot.place(relx=0.18, rely=0, relwidth=0.14, relheight=0.8)
        self.FornecLbBt = Label(self.FrameBot, text=self.m_Fornecedor, bd=2, bg= '#49708D', fg= 'white',
                                font=('Verdana', '7', 'bold'))
        self.FornecLbBt.place(relx=0.18, rely=0.82, relwidth=0.14, relheight=0.18)

        self.ModelosBot = Button(self.FrameBot, image=self.cadautBt, bd=0, bg= '#49708D', fg=self.fg_button,
                                 command=self.cadaut);
        self.ModelosBot.place(relx=0.33, rely=0, relwidth=0.14, relheight=0.8)
        self.ModelosLbBt = Label(self.FrameBot, text=self.m_Automoveis, bd=2, bg= '#49708D', fg= 'white',
                                font=('Verdana', '7', 'bold'))
        self.ModelosLbBt.place(relx=0.33, rely=0.82, relwidth=0.14, relheight=0.18)

        self.ProdutosBot = Button(self.FrameBot, image=self.cadprodBt, bd=0, bg= '#49708D', fg=self.fg_button,
                                  command=self.cadprod);
        self.ProdutosBot.place(relx=0.48, rely=0, relwidth=0.14, relheight=0.8)
        self.ProdutosLbBt = Label(self.FrameBot, text=self.m_Produtos, bd=2, bg= '#49708D', fg= 'white',
                                font=('Verdana', '7', 'bold'))
        self.ProdutosLbBt.place(relx=0.48, rely=0.82, relwidth=0.14, relheight=0.18)

        self.ServBot = Button(self.FrameBot, image=self.cadservBt, bd=0, bg= '#49708D', fg=self.fg_button,
                              command=self.cadserv);
        self.ServBot.place(relx=0.63, rely=0, relwidth=0.14, relheight=0.8)
        self.ServLbBt = Label(self.FrameBot, text=self.m_Serviços, bd=2, bg= '#49708D', fg= 'white',
                                font=('Verdana', '7', 'bold'))
        self.ServLbBt.place(relx=0.63, rely=0.82, relwidth=0.14, relheight=0.18)
    def aba1(self):

        ##########################################################################
        ####  Descrição dos problemas apresentados pelo veiculo - Aba 1
        self.frameProb = Frame(self.frame_aba1, bg= self.fundo_do_frame, bd=4, relief=SUNKEN)
        self.frameProb.place(relx=0.01, rely=0.01, relwidth=1, relheight=1)
        self.DescrProb=Label(self.frame_aba1,bg=self.bg_button,text=self.m_Atend1,bd=0,fg=self.fg_button,
            font=('Verdana', '12', 'bold'));
        self.DescrProb.place(relx=0.04, rely=0.04, relwidth=0.91, relheight=0.12)
        self.area1=Entry(self.frame_aba1,bd=1,width=77,fg=self.fg_entry,bg=self.bg_entry,font=('Verdana','11','bold'))
        self.area1.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.1)
        self.area2=Entry(self.frame_aba1,bd=1,width=77,fg=self.fg_entry,bg=self.bg_entry,font=('Verdana','11','bold'))
        self.area2.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.1)
        self.DescrProb2=Label(self.frame_aba1,text=self.m_Atend2,bd=0,width=85,fg=self.fg_button,
            font=('Verdana','12','bold'), bg= self.bg_button)
        self.DescrProb2.place(relx=0.04, rely=0.49, relwidth=0.91, relheight=0.12)
        self.area3=Entry(self.frame_aba1,bd=1,width=77,fg=self.fg_entry,bg=self.bg_entry,font=('Verdana','11','bold'))
        self.area3.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.1)
        self.area4=Entry(self.frame_aba1,bd=1,width=77,fg=self.fg_entry,bg=self.bg_entry,font=('Verdana','11','bold'))
        self.area4.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.1)
        ###########################################################################
        ###  Label e Entrada Inicio
        self.descrInicio = Button(self.frame_aba1, font=('Verdana', '8', 'bold'), command = self.calendarioInicio);
        self.descrInicio.configure(text='Data inicial', fg=self.fg_label, bg=self.fundo_do_frame)
        self.descrInicio.place(relx=0.05, rely=0.045, relwidth=0.09, relheight=0.06)
        self.listInicio = Entry(self.frame_aba1, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                font=('Verdana', '8', 'bold'))
        self.listInicio.place(relx=0.05, rely=0.1, relwidth=0.09, relheight=0.05)
        ##########################################################################
        ###########################################################################
        ###  Label e Entrada Fim
        self.descrFim = Button(self.frame_aba1, font=('Verdana', '8', 'bold'), command = self.calendarioFim);
        self.descrFim.configure(text='Data final', fg=self.fg_label, bg=self.fundo_do_frame)

        self.descrFim.place(relx=0.05, rely=0.495, relwidth=0.09, relheight=0.06)
        self.listFim = Entry(self.frame_aba1, bd=1, fg=self.fg_entry, bg=self.bg_entry, font=('Verdana', '8', 'bold'))
        self.listFim.place(relx=0.05, rely=0.55, relwidth=0.09, relheight=0.05)
    def aba2(self):
        ### Cabeçalho dos itens_orc 1 A 10 - Aba 2
        self.frameItens = Frame(self.frame_aba2, bd=4, bg=self.bg_button)
        self.frameItens.place(relx=0.005, rely=0.01, relwidth=0.98, relheight=0.98)
        self.frameSP = Frame(self.frame_aba2,  bg= self.fundo_do_frame, bd=4,relief=SUNKEN)
        self.frameSP.place(relx=0.01, rely=0.03, relwidth=0.96, relheight=0.96)
        #### Label codigo
        self.descrCodI=Label(self.frame_aba2,bg=self.bg_button,fg= self.fg_label,text= self.m_Codigo+self.m_barra
            +self.m_Item,font=('Verdana', '10', 'bold'))
        self.descrCodI.place(relx=0.568, rely=0.05, relwidth=0.12, relheight=0.09)
        ######      Label Servicos Peças
        self.descrCol2 = Label(self.frame_aba2, bg= self.fg_label,text = self.m_Serviços + self.m_barra +
            self.m_Produtos,justify = 'center', fg=self.bg_label, font=('Verdana', '10', 'bold'))
        self.descrCol2.place(relx=0.016, rely=0.05, relwidth=0.55, relheight=0.09)
        ##      Label Valor
        self.descrCol3 = Label(self.frame_aba2, text= self.m_ValorUnit, bg=self.bg_label, fg= self.fg_label,
            font=('Verdana','10','bold'));
        self.descrCol3.place(relx=0.69, rely=0.05, relwidth=0.09, relheight=0.09)
        ###  Quantidade
        self.descrQuant = Button(self.frame_aba2, text= self.m_Quant, bg=self.fg_label, fg=self.bg_label,
            font=('Verdana','10','bold'), command = self.altera_itens_orc_quant2);
        self.descrQuant.place(relx=0.78, rely=0.05, relwidth=0.05, relheight=0.09)
        ###     Total Item
        self.descrTotalItem = Label(self.frame_aba2, text= self.m_Total + ' ' + self.m_Item, bg=self.bg_label,
            fg= self.fg_label, font=('Verdana', '10', 'bold'))
        self.descrTotalItem.place(relx=0.83, rely=0.05, relwidth=0.1, relheight=0.09)
        ###############################
        ### Widgets - Listar item 1 ###

        ####  Descricao do item Col2
        self.listaCol2a = AutocompleteEntrySP(lista2, self.frame_aba2, bd=1, fg=self.fg_entry, bg=self.bg_entry,
                                              font=('Verdana', '8', 'bold'));
        self.listaCol2a.place(relx=0.016, rely=0.14, relwidth=0.53, relheight=0.08)
        ### Codigo do Item
        self.codServ1 = Entry(self.frame_aba2, validate="key", width=6, bd=1, justify='center', fg=self.fg_entry,
                              bg=self.bg_entry, validatecommand=self.vcmd6, font=('Verdana', '8', 'bold'))
        self.codServ1.place(relx=0.571, rely=0.14, relwidth=0.06, relheight=0.08)

        self.botaoAddServicos1 = Button(self.frame_aba2, bd=2, bg=self.bg_label, text= '>>',
                                        command=self.add_servico1)
        self.botaoAddServicos1.place(relx=0.634, rely=0.14, relwidth=0.04, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP1=Button(self.frame_aba2,bd=0,bg=self.bg_label,image=self.lupaBt,command=self.busca_servico1)
        self.botaoBuscaSP1.place(relx=0.549, rely=0.14, relwidth=0.03, relheight=0.08)
        #### Coluna Quantidade
        self.listaCol3a = Entry(self.frame_aba2, width=5, validate="key", bg=self.bg_entry,
            validatecommand=self.vcmd4float, bd=1,justify='center', fg=self.fg_entry, font=('Verdana', '8', 'bold'))
        self.listaCol3a.place(relx=0.78, rely=0.14, relwidth=0.05, relheight=0.08);  self.listaCol3a.insert(END, 1)
        #### Coluna Valor
        self.listaCol4a=Entry(self.frame_aba2,validate="key",bg=self.bg_entry,bd=1,justify='right',fg=self.fg_entry,
            font=('Verdana', '8', 'bold'));
        self.listaCol4a.place(relx=0.68,rely=0.14,relwidth=0.1,relheight=0.08)
        self.listaCol4a.insert(END, 0)
        self.labelCol4a = Label(self.frame_aba2, text=self.m_Reais, fg=self.fg_entry, bg=self.bg_entry, bd=0,
            font=('Verdana', '6', 'bold'));
        self.labelCol4a.place(relx=0.69,rely=0.15,relwidth=0.02,relheight=0.06)
        ###### Coluna Total Unitario
        self.listaCol5a=Entry(self.frame_aba2,validate="key",bg=self.bg_entry,bd=1,justify='right',fg=self.fg_entry,
            font=('Verdana', '8', 'bold'));
        self.listaCol5a.place(relx=0.83, rely=0.14, relwidth=0.1, relheight=0.08)
        self.listaCol5a.insert(END, 0)
        ###### ADD
        self.botaoAddServicos2 = Button(self.frame_aba2, bd=0, bg=self.bg_label, image = self.add,
                                        command = self.add_itens_orc)
        self.botaoAddServicos2.place(relx=0.931, rely=0.14, relwidth=0.04, relheight=0.08)
        ################### treeview ####################
        #################################################
        self.barraServProd = Scrollbar(self.frame_aba2, orient='vertical', command=self.OnVsb_Orc2)

        self.listaServProd = ttk.Treeview(self.frame_aba2, height=10, yscrollcommand=self.barraServProd.set,
                                      column=("col1", "col2", "col3", "col4", "col5","col6"))

        self.listaServProd.heading("#0", text="")
        self.listaServProd.heading("#1", text= self.m_Item)
        self.listaServProd.heading("#2", text=self.m_Serviços)
        self.listaServProd.heading("#3", text= self.m_Codigo)
        self.listaServProd.heading("#4", text=self.m_Valor)
        self.listaServProd.heading("#5", text= self.m_Quant)
        self.listaServProd.heading("#6", text=self.m_Valor + ' ' + self.m_Total)

        self.listaServProd.column("#0", width=1)
        self.listaServProd.column("#1", width=10)
        self.listaServProd.column("#2", width=450)
        self.listaServProd.column("#3", width=45)
        self.listaServProd.column("#4", width=60)
        self.listaServProd.column("#5", width=45)
        self.listaServProd.column("#6", width=60)

        self.listaServProd.place(relx=-0.031, rely=0.24, relwidth=0.98, relheight=0.72)

        self.listaServProd.configure(yscroll=self.barraServProd.set)
        self.barraServProd.place(relx=0.948, rely=0.24, relwidth=0.02, relheight=0.72)
        self.listaServProd.bind('<Double-1>', self.altera_itens_orc)
        self.listaServProd.bind('<Return>', self.altera_itens_orc)
        self.listaServProd.bind('<Delete>', self.altera_itens_orc_deletabt2)

        self.canvas_aba2a = Frame(self.frame_aba2, bd=0, bg=self.borda_frame)
        self.canvas_aba2a.place(relx= 0, rely = 0.01, relheight = 0.98, relwidth = 0.01)
    def aba4(self):
        #####################
        ###Frames da moldura
        self.frameProb = Frame(self.frame_aba4, width=790, height=228, bd=4, bg=self.bg_button)
        self.frameProb.place(relx=0.015, rely=0.03, relwidth=0.97, relheight=0.94)

        self.frameProb = Frame(self.frame_aba4, width=780, height=218, bd=4, bg=self.bg_label, relief=SUNKEN)
        self.frameProb.place(relx=0.017, rely=0.035, relwidth=0.965, relheight=0.935)
        ###########################
        ### Tanque de combustivel
        descrTanq = Label(self.frame_aba4, bd=2, width=22, text= self.m_Tanque, bg= self.bg_button,
                          fg=self.fg_button, font=('Verdana', '8', 'bold'))
        descrTanq.place(relx=0.05, rely=0.1, relwidth=0.18, relheight=0.1)
        self.are1 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry, bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are1.place(relx=0.23, rely=0.1, relwidth=0.18, relheight=0.1)
        ##################
        #### Odometro
        descrOdom = Label(self.frame_aba4, width=22, bd=2, text= self.m_Odometro, bg= self.bg_button,
                          fg=self.fg_button, font=('Verdana', '8', 'bold'))
        descrOdom.place(relx=0.05, rely=0.22, relwidth=0.18, relheight=0.1)
        self.are2 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are2.place(relx=0.23, rely=0.22, relwidth=0.18, relheight=0.1)
        ############################
        ###  Radio Kit Multimidia
        descrRad = Label(self.frame_aba4, bd=2, width=22, text= self.m_Obs , bg= self.bg_button,
                         fg=self.fg_button, font=('Verdana', '8', 'bold'))
        descrRad.place(relx=0.05, rely=0.34, relwidth=0.18, relheight=0.1)
        self.are3 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are3.place(relx=0.23, rely=0.34, relwidth=0.18, relheight=0.1)
        ###################
        ####   Calotas
        descrCalot = Label(self.frame_aba4, bd=2, width=22, text= self.m_Obs , bg= self.bg_button,
                           fg=self.fg_button, font=('Verdana', '8', 'bold'))
        descrCalot.place(relx=0.05, rely=0.46, relwidth=0.18, relheight=0.1)
        self.are4 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are4.place(relx=0.23, rely=0.46, relwidth=0.18, relheight=0.1)
        ###################
        ####  Triangulo
        descrtri = Label(self.frame_aba4, bd=2, width=22, text= self.m_Obs , bg= self.bg_button,
                         fg=self.fg_button, font=('Verdana', '8', 'bold'))
        descrtri.place(relx=0.05, rely=0.58, relwidth=0.18, relheight=0.1)
        self.are5 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are5.place(relx=0.23, rely=0.58, relwidth=0.18, relheight=0.1)
        ################
        ###   Macaco
        descrMacaco = Label(self.frame_aba4, bd=2, width=22, text= self.m_Obs , bg= self.bg_button,
                            fg=self.fg_button, font=('Verdana', '8', 'bold'))
        descrMacaco.place(relx=0.05, rely=0.7, relwidth=0.18, relheight=0.1)
        self.are6 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are6.place(relx=0.23, rely=0.7, relwidth=0.18, relheight=0.1)
        #################
        ####   Estepe
        descrEst = Label(self.frame_aba4, bd=2, width=22, text= self.m_Obs, bg= self.bg_button,
                         fg=self.fg_button, font=('Verdana', '8', 'bold'))
        descrEst.place(relx=0.05, rely=0.82, relwidth=0.18, relheight=0.1)
        self.are7 = Entry(self.frame_aba4, bd=1, width=20, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are7.place(relx=0.23, rely=0.82, relwidth=0.18, relheight=0.1)
        #################
        ####   Are 8
        descrAre8 = Label(self.frame_aba4, bd=2, width=10, text= self.m_Obs, bg= self.bg_button,
                          fg=self.fg_button, font=('Verdana', '8', 'bold'))
        descrAre8.place(relx=0.55, rely=0.1, relwidth=0.18, relheight=0.1)
        self.are8 = Entry(self.frame_aba4, bd=1, width=25, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are8.place(relx=0.73, rely=0.1, relwidth=0.18, relheight=0.1)
        #################
        ####   Are 9
        descrAre9 = Label(self.frame_aba4, bd=2, width=10, text= self.m_Obs, bg= self.bg_button,
                          fg=self.fg_button, font=('Verdana', '8', 'bold'))
        descrAre9.place(relx=0.55, rely=0.22, relwidth=0.18, relheight=0.1)
        self.are9 = Entry(self.frame_aba4, bd=1, width=25, fg=self.fg_entry,  bg=self.bg_entry,
                          font=('Verdana', '9', 'bold'))
        self.are9.place(relx=0.73, rely=0.22, relwidth=0.18, relheight=0.1)

        # Gerar PDF

        vistlabel = Label(self.frame_aba4, bd=2, text= self.m_ImprimirVistoria, bg= self.bg_button,
                          fg=self.fg_button, font=('Verdana', '8', 'bold'))
        vistlabel.place(relx=0.64, rely=0.6, relwidth=0.2, relheight=0.2)
        ###  Botao botaoImprimirVist
        self.botaoImprimirVist = Button(self.frame_aba4, image=self.button_imprime2, compound=LEFT, bd=0,
                                        bg = self.bg_button, command=self.imprime_vist)
        self.botaoImprimirVist.place(relx=0.69, rely=0.43, relwidth=0.1, relheight=0.2)
    def aba5(self):
        #####################################################################
        ### Cabeçalho dos itens_orc 1 A 10 - Aba 5
        self.frameItensF = Frame(self.frame_aba5, bd=2, bg=self.bg_button)
        self.frameItensF.place(relx=0.015, rely=0.015, relwidth=0.97, relheight=0.96)

        self.frameItensF = Frame(self.frame_aba5, bd=2, bg= self.fundo_do_frame,relief=SUNKEN)
        self.frameItensF.place(relx=0.02, rely=0.02, relwidth=0.93, relheight=0.93)
        #### Label codigo
        self.descrCodIF=Label(self.frame_aba5,bg=self.bg_button,text=self.m_Codigo+self.m_barra+self.m_Item,
                                font=('Verdana', '9', 'bold'), fg = self.fg_label)
        self.descrCodIF.place(relx=0.026, rely=0.028, relwidth=0.11, relheight=0.09)
        ###### Label Servicos Peças
        self.descrCol2F = Label(self.frame_aba5, bg=self.fg_label,fg= self.bg_label, text = self.m_DescricaoFalha,
                                font=('Verdana', '12', 'bold'))
        self.descrCol2F.place(relx=0.138, rely=0.028, relwidth=0.45, relheight=0.09)

        ###############################
        ### Widgets - Listar item 1 ###
        ### Codigo do Item
        self.codServ1F = Entry(self.frame_aba5, validate="key", width=6, bg=self.bg_entry, bd=1, justify='center',
                               fg=self.fg_entry , font=('Verdana', '8', 'bold'))
        self.codServ1F.place(relx=0.026, rely=0.12, relwidth=0.055, relheight=0.08)

        self.botaoAddServicos1F = Button(self.frame_aba5, bd=0, bg=self.bg_label,image=self.add, command=self.add_servico1F)
        self.botaoAddServicos1F.place(relx=0.69, rely=0.12, relwidth=0.055, relheight=0.08)

        ####  Descricao do item Col2
        self.listaCol2aF = Entry(self.frame_aba5, width=60, bd=1, bg=self.bg_entry, fg=self.fg_entry,
                                 font=('Verdana', '8', 'bold'))
        self.listaCol2aF.place(relx=0.14, rely=0.12, relwidth=0.45, relheight=0.08)

        #### Botao Busca Item
        self.botaoBuscaSP1F = Button(self.frame_aba5, bd=0, bg=self.bg_label,
                                     image=self.lupaBt, font=('Verdana', '10', 'bold'),command=self.busca_servico1F)
        self.botaoBuscaSP1F.place(relx=0.59, rely=0.12, relwidth=0.05, relheight=0.08)

        ################### treeview ####################
        ##################q###############################
        self.barraServProdF = Scrollbar(self.frame_aba5, orient='vertical', command=self.OnVsb_Orc2)

        self.listaServProdF = ttk.Treeview(self.frame_aba5, height=10, yscrollcommand=self.barraServProd.set,
                                          column=("col1", "col2", "col3"))

        self.listaServProdF.heading("#0", text="")
        self.listaServProdF.heading("#1", text=self.m_Item)
        self.listaServProdF.heading("#2", text=self.m_Falhas)
        self.listaServProdF.heading("#3", text=self.m_Observacao)

        self.listaServProdF.column("#0", width=1)
        self.listaServProdF.column("#1", width=20)
        self.listaServProdF.column("#2", width=350)
        self.listaServProdF.column("#3", width=350)


        self.listaServProdF.place(relx=-0.031, rely=0.24, relwidth=0.98, relheight=0.72)

        self.listaServProdF.configure(yscroll=self.barraServProd.set)
        self.barraServProdF.place(relx=0.948, rely=0.24, relwidth=0.02, relheight=0.72)
        self.listaServProdF.bind('<Double-1>', self.altera_itens_orc)
        self.listaServProdF.bind('<Return>', self.altera_itens_orc)
        self.listaServProdF.bind('<Delete>', self.altera_itens_orc_deletabt2)

        self.canvas_aba2a = Frame(self.frame_aba5, bd=0, bg=self.borda_frame)
        self.canvas_aba2a.place(relx=0, rely=0.01, relheight=0.98, relwidth=0.01)

                
        janela.mainloop()
        
    def cores(self):
        self.fundo_do_frame = '#dfe3ee'; self.borda_frame = '#759fe6'; self.fundo_da_tela = '#4682b4'
        self.bg_button = '#107db2'; self.fg_button = 'white'; self.bg_label = '#dfe3ee'
        self.fg_label = '#3b5998'; self.fg_entry = 'gray25'; self.bg_entry = '#edf3f8'
        self.bg_button_del = '#c66c73'
        
    def Menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)
        filemenu4 = Menu(menubar)
        filemenu5 = Menu(menubar)

        def Quit(): self.janela.destroy()
        def Help():
            msg = self.m_Ajuda
            msg += ""
            messagebox.showinfo("GLAC ", msg)
        def Sobre():
            msg = "GlacX -        rafaelserafim.rfzorzi@gmail.com                \n "
            msg += "RfZorzi - https://www.facebook.com/rfzorzi/ - Brazil"
            messagebox.showinfo("GLAC ", msg)

        menubar.add_cascade(label= self.m_Cadastros, menu=filemenu)
        menubar.add_cascade(label= self.m_Consulta, menu=filemenu2)
        menubar.add_cascade(label= self.m_Relatorios, menu=filemenu3)
        menubar.add_cascade(label= self.m_Procedimentos, menu=filemenu4)
        menubar.add_cascade(label= self.m_Ajuda, menu=filemenu5)

        filemenu.add_command(label= self.m_Automoveis, command= self.cadaut)
        filemenu.add_command(label= self.m_Clientes, command= self.cadcli)
        filemenu.add_command(label= self.m_Fornecedores, command= self.cadforn)
        filemenu.add_command(label= self.m_Produtos, command= self.cadprod)
        filemenu.add_command(label= self.m_Marca + self.m_Produtos, command= self.cadmarcaprod)
        filemenu.add_command(label= self.m_Serviços, command= self.cadserv)
        filemenu.add_command(label= self.m_Tecnico, command= self.cadtec)
        filemenu.add_command(label= self.m_Estab, command= self.cademp)
        filemenu.add_command(label= self.m_Copia, command= self.backup)
        filemenu.add_command(label= self.m_Sair, command=Quit)

        filemenu2.add_command(label= self.m_Cons_Rec, command= self.cadfinan)
        filemenu2.add_command(label= self.m_Cons_Pag, command= self.consultapag)

        filemenu3.add_command(label= self.m_Orcamento, command=self.PrintOrc)
        filemenu3.add_command(label= self.m_ImprimirVistoria, command=self.PrintVist)

        filemenu4.add_command(label= self.m_Proced_Lanc, command= self.cadest)
        filemenu4.add_command(label= self.m_Proced_Atual, command= self.procedServ)

        filemenu5.add_command(label= self.m_Sobre, command=Sobre)
        

MeuOrc()