from modulos import *
from multilanguage import *
import licence
from functions import *


class Objects_Glac():
    def custommer_obj(self):
        def validadores():
            # Chama validadores de entradas com apenas numeros
            self.vcmd1 = (self.janelaCli.register(self.validate_entry1), "%P")
            self.vcmd2 = (self.janelaCli.register(self.validate_entry2), "%P")
            self.vcmd4 = (self.janelaCli.register(self.validate_entry4), "%P")
            self.vcmd8 = (self.janelaCli.register(self.validate_entry8), "%P")
            self.vcmd12 = (self.janelaCli.register(self.validate_entry12), "%P")
        validadores()

        #### Codigo
        self.codPeLabel = Label(self.janelaCli, text = self.m_Codigo)
        self.codPeLabel.configure(font=('Verdana', '8', 'bold'), bg = self.bg_label, fg = self.fg_label)
        self.codPeEntry = Entry(self.janelaCli, width=10)
        self.codPeEntry.configure(font=('Arial', '8', 'bold'), fg= self.fg_entry, validate="key", bg = self.bg_entry,
                                  validatecommand=self.vcmd8)
        #### Nascimento
        self.nascPeLabel = Label(self.janelaCli, text = self.m_Nasc)
        self.nascPeLabel.configure( bg = self.bg_label, fg = self.fg_label, font=('Verdana', '8', 'bold'))

        ## dia
        self.nascDiaPeEntry = Entry(self.janelaCli, bg = self.bg_entry)
        self.nascDiaPeEntry.configure(font=('Verdana', '8', 'bold'), fg=self.fg_entry
                                      , validate="key", validatecommand=self.vcmd2)

        ## mes
        self.nascMesPeEntry = Entry(self.janelaCli )
        self.nascMesPeEntry.configure(font=('Verdana', '8', 'bold'), fg=self.fg_entry , bg = self.bg_entry
                                      , validate="key", validatecommand=self.vcmd2)

        ## ano
        self.nascAnoPeEntry = Entry(self.janelaCli)
        self.nascAnoPeEntry.configure(font=('Verdana', '8', 'bold'), fg=self.fg_entry, bg = self.bg_entry
                                      , validate="key", validatecommand=self.vcmd4)

        #### Nome
        self.nomePeLabel = Label(self.janelaCli, text = self.m_Nome)
        self.nomePeLabel.configure(font=('Verdana', '8', 'bold'), bg = self.bg_label, fg = self.fg_label)
        self.nomePeEntry = Entry(self.janelaCli)
        self.nomePeEntry.configure(font=('Arial', '8', 'bold'), fg=self.fg_entry, bg = self.bg_entry)

        ##### Rua
        self.logradPeLabel = Label(self.janelaCli, text = self.m_Endereco)
        self.logradPeLabel.configure(font=('Verdana', '8', 'bold'), bg = self.bg_label, fg = self.fg_label)
        self.logradPeEntry = Entry(self.janelaCli, bg = self.bg_entry)
        self.logradPeEntry.configure(font=('Arial', '8', 'bold'), fg=self.fg_entry)

        #### nummero
        self.numPeLabel = Label(self.janelaCli, text = self.m_Numero, bg = self.bg_label, fg = self.fg_label)
        self.numPeEntry = Entry(self.janelaCli)
        self.numPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.numPeEntry.configure(font=('Arial', '8', 'bold'), fg=self.fg_entry, bg = self.bg_entry)

        #### commmplemento
        self.complemPeLabel = Label(self.janelaCli, text = self.m_Complemento, bg = self.bg_label, fg = self.fg_label)
        self.complemPeEntry = Entry(self.janelaCli)
        self.complemPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.complemPeEntry.configure(font=('Arial', '8', 'bold'), fg=self.fg_entry, bg = self.bg_entry)

        #### bairro
        self.bairroPeLabel = Label(self.janelaCli, text = self.m_Bairro, bg = self.bg_label, fg = self.fg_label)
        self.bairroPeEntry = Entry(self.janelaCli)
        self.bairroPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.bairroPeEntry.configure(font=('Arial', '8', 'bold'), fg=self.fg_entry, bg = self.bg_entry,)

        ######
        self.cidadePeLabel = Label(self.janelaCli, text = self.m_Cidade, bg = self.bg_label, fg = self.fg_label)
        self.cidadePeEntry = Entry(self.janelaCli)
        self.cidadePeLabel.configure(font=('Verdana', '8', 'bold'))
        self.cidadePeEntry.configure(font=('Arial', '8', 'bold'), fg=self.fg_entry, bg = self.bg_entry)

        ####
        self.ufPeLabel = Label(self.janelaCli, text = self.m_Uf, bg = self.bg_label, fg = self.fg_label)
        self.ufPeEntry = Entry(self.janelaCli )
        self.ufPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.ufPeEntry.configure(font=('Arial', '8', 'bold'), fg=self.fg_entry, bg = self.bg_entry)

        #####
        self.fone1Pelabel = Label(self.janelaCli, text = self.m_Fone + ' 1', bg = self.bg_label, fg = self.fg_label)
        self.fone1PeEntry = Entry(self.janelaCli,fg=self.fg_entry, bg = self.bg_entry)
        self.fone1PeEntry2 = Entry(self.janelaCli, fg=self.fg_entry, bg = self.bg_entry)


        self.fone2Pelabel = Label(self.janelaCli, text = self.m_Fone + ' 2', bg = self.bg_label, fg = self.fg_label)
        self.fone2PeEntry = Entry(self.janelaCli, fg=self.fg_entry, bg = self.bg_entry)
        self.fone2PeEntry2 = Entry(self.janelaCli, fg=self.fg_entry, bg = self.bg_entry)

        self.fone1Pelabel.configure(font=('Verdana', '8', 'bold'))
        self.fone2Pelabel.configure(font=('Verdana', '8', 'bold'))
        self.fone2PeEntry2.configure(font=('Verdana', '8', 'bold'), fg=self.fg_entry
                                     , validate="key", validatecommand=self.vcmd12, bg = self.bg_entry)
        self.fone2PeEntry.configure(font=('Verdana', '8', 'bold'), fg=self.fg_entry
                                    , validate="key", validatecommand=self.vcmd2, bg = self.bg_entry)
        self.fone1PeEntry2.configure(font=('Verdana', '8', 'bold'), fg=self.fg_entry
                                     , validate="key", validatecommand=self.vcmd12, bg = self.bg_entry)
        self.fone1PeEntry.configure(font=('Verdana', '8', 'bold'), fg=self.fg_entry
                                    , validate="key", validatecommand=self.vcmd2, bg = self.bg_entry)

        #####
        self.cpfPeLabel = Label(self.janelaCli, text = self.m_Cpf, bg = self.bg_label, fg = self.fg_label)
        self.cpfPeEntry = Entry(self.janelaCli, bg = self.bg_entry)
        self.cpfPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.cpfPeEntry.configure(font=('Verdana', '8', 'bold'), fg=self.fg_entry
                                  , validate="key", validatecommand=self.vcmd12, bg = self.bg_entry)

        #####
        self.cnpjPeLabel = Label(self.janelaCli, text = self.m_Cnpj, bg = self.bg_label, fg = self.fg_label)
        self.cnpjPeEntry = Entry(self.janelaCli, bg = self.bg_entry)
        self.cnpjPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.cnpjPeEntry.configure(font=('Verdana', '8', 'bold'), fg=self.fg_entry
                                   , validate="key", validatecommand=self.vcmd12, bg = self.bg_entry)

        #######
        self.rgPeLabel = Label(self.janelaCli, text = self.m_RG, bg = self.bg_label, fg = self.fg_label)
        self.rgPeEntry = Entry(self.janelaCli, bg = self.bg_entry)

        ######
        self.obsPeLabel = Label(self.janelaCli, text = self.m_Obs, bg = self.bg_label, fg = self.fg_label)
        self.obsPeEntry = Entry(self.janelaCli)
        self.obsPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.obsPeEntry.configure(font=('Arial', '8', 'bold'), fg=self.fg_entry, bg = self.bg_entry)

        self.emailPeLabel = Label(self.janelaCli, text = 'E-mail', bg = self.bg_label, fg = self.fg_label)
        self.emailPeEntry = Entry(self.janelaCli)
        self.emailPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.emailPeEntry.configure(font=('Arial', '8', 'bold'), fg=self.fg_entry, bg = self.bg_entry,)

        self.inscEstPeLabel = Label(self.janelaCli, text = 'Inscrição Estadual', bg = self.bg_label, fg = self.fg_label)
        self.inscEstPeEntry = Entry(self.janelaCli, bg = self.bg_entry,)

        self.cepPeBt = Button(self.janelaCli, text= '>>', command = self.cep, fg = self.fg_label)
        self.cepPeLabel = Label(self.janelaCli, text= self.m_Cep, bg = self.bg_label, fg = self.fg_label)
        self.cepPeEntry = Entry(self.janelaCli)
        self.cepPeLabel.configure(font=('Verdana', '8', 'bold'))
        self.cepPeEntry.configure(font=('Arial', '8', 'bold'), fg=self.fg_entry
                                  , validate="key", validatecommand=self.vcmd8, bg = self.bg_entry)
        ###  Botao Novo Cliente
        self.botaoAdd = Button(self.janelaCli, text = self.m_Novo, bd=2, bg= self.bg_button, fg= self.fg_button,
                               font=('Verdana', '9', 'bold'))
        self.botaoAdd2 = Button(self.janelaCli, text = self.m_Novo, bd=2, bg= self.bg_button, fg= self.fg_button,
                               font=('Verdana', '9', 'bold'))
        ### Botao Altera dados do Cliente
        self.botaoMud = Button(self.janelaCli, bd=2, text = self.m_Alterar, bg= self.bg_button, fg= self.fg_button,
                                   font=('Verdana', '9', 'bold'))
        self.botaoMud2 = Button(self.janelaCli, bd=2, text = self.m_Alterar, bg= self.bg_button, fg= self.fg_button,
                               font=('Verdana', '9', 'bold'))
        ### Botao deletar dados do Cliente
        self.botaoDel = Button(self.janelaCli, bd=2, text = self.m_Apagar, bg= self.bg_button_del, fg= self.fg_button,
                                   font=('Verdana', '9', 'bold'))
        self.botaoDel2 = Button(self.janelaCli, bd=2, text = self.m_Apagar, bg= self.bg_button_del, fg= self.fg_button,
                               font=('Verdana', '9', 'bold'))
        ##  Botao limpa
        self.botaolimpa = Button(self.janelaCli, bd=1, text = self.m_Limpar, bg=self.bg_button, fg= self.fg_button,
                                 font=('Verdana', '9', 'bold'))
        ###  Botao busca Cabeça
        self.botaobusca = Button(self.janelaCli, bitmap = 'questhead', bg= self.bg_button, fg= self.fg_button,
                                font=('Verdana', '8', 'bold'))
        #### cod
        self.entradaVeiculo2 = Entry(self.janelaCli, bg= self.bg_entry, fg= self.fg_entry,
                                font=('Verdana', '8', 'bold'))
        self.entradaMontadora2 = Entry(self.janelaCli, bg= self.bg_entry, fg= self.fg_entry,
                                font=('Verdana', '8', 'bold'))

        self.codEquipLabel = Label(self.janelaCli, text = self.m_Codigo, bg = self.bg_label, fg = self.fg_label)
        self.codEquipEntry = Entry(self.janelaCli, width=10, bg= self.bg_entry, fg= self.fg_entry,
                                font=('Verdana', '8', 'bold'))

        self.fabrAnoEquipLabel = Label(self.janelaCli, text = self.m_Ano, bg = self.bg_label, fg = self.fg_label)
        self.fabrAnoEquipEntry = Entry(self.janelaCli)
        self.fabrAnoEquipLabel.configure(font=('Verdana', '8', 'bold'))
        self.fabrAnoEquipEntry.configure( bg= self.bg_entry, fg= self.fg_entry,
                                font=('Verdana', '8', 'bold'))

        self.fabrModeloEquipLabel = Label(self.janelaCli, text=self.m_Ano, bg = self.bg_label, fg = self.fg_label)
        self.fabrModeloEquipEntry = Entry(self.janelaCli, bg= self.bg_entry, fg= self.fg_entry,
                                font=('Verdana', '8', 'bold'))

        self.nomeEquipLabel = Label(self.janelaCli, text = self.m_Automovel, bg = self.bg_label, fg = self.fg_label)
        self.nomeEquipEntry = Entry(self.janelaCli, bg= self.bg_entry, fg= self.fg_entry,
                                font=('Verdana', '8', 'bold'))
        self.nomeIdEquipEntry = Entry(self.janelaCli, bg= self.bg_entry, fg= self.fg_entry,
                                font=('Verdana', '8', 'bold'))

        self.serialEquipLabel = Label(self.janelaCli, text = self.m_Placa, bg = self.bg_label, fg = self.fg_label)
        self.serialEquipEntry = Entry(self.janelaCli, bg= self.bg_entry, fg= self.fg_entry,
                                font=('Verdana', '8', 'bold'))
        self.serialEquipLabel.configure(font=('Verdana', '7', 'bold'))

        self.corEquipLabel = Label(self.janelaCli, text = self.m_Cor, bg = self.bg_label, fg = self.fg_label)
        self.corEquipLabel.configure(font=('Verdana', '7', 'bold'))
        self.corEquipEntry = Frame( self.janelaCli, bd=2)
        self.corEquipEntry.grid(column=0, row=0, sticky=(N, W, E, S))
        self.corEquipEntry.columnconfigure(0, weight=1)
        self.corEquipEntry.rowconfigure(0, weight=1)
        self.corEquipEntry.place(relx=0.5, rely=0, relwidth=0.12, relheight=1)
        self.corvar = StringVar(self.janelaCli)
        self.coresV = {self.m_Branco, self.m_Amarelo, self.m_Verde, self.m_Bege,
                       self.m_Azul, self.m_Laranja, self.m_Vermelho, self.m_Verde,
                       self.m_Cinza, self.m_Preto, self.m_Marrom, self.m_Bordo, self.m_Prata,
                       self.m_Grafite, self.m_Dourado, self.m_Outro}
        self.corvar.set(self.m_Branco)
        self.popupMenu = OptionMenu(self.corEquipEntry, self.corvar, *self.coresV)
        self.popupMenu.grid(row=2, column=1)

        self.combEquipLabel = Label(self.janelaCli, text=self.m_Combustivel, bg = self.bg_label, fg = self.fg_label)
        self.combEquipLabel.configure(font=('Verdana', '7', 'bold'))
        self.combEquipEntry = Frame(self.janelaCli,   bd=2)
        self.combEquipEntry.grid(column=0, row=0, sticky=(N, W, E, S))
        self.combEquipEntry.columnconfigure(0, weight=1)
        self.combEquipEntry.rowconfigure(0, weight=1)
        self.combEquipEntry.pack(pady=100, padx=100)
        self.combEquipEntry.place(relx=0.63, rely=0, relwidth=0.13, relheight=1)
        self.combvar = StringVar(self.janelaCli)
        self.combV = {self.m_Gasolina, self.m_Alcool, self.m_Diesel, self.m_Flex,
                      self.m_Gasolina_e_Gas, self.m_Alcool_e_Gas, self.m_Flex_e_Gas}

        self.combvar.set(self.m_Gasolina)
        self.popupMenu = OptionMenu(self.combEquipEntry, self.combvar, *self.combV)
        self.popupMenu.grid(row=2, column=1)

        self.marcaEquipLabel = Label(self.janelaCli, text=self.m_Marca, bg = self.bg_label, fg = self.fg_label)
        self.marcaEquipEntry = Entry(self.janelaCli, bg= self.bg_entry, fg= self.fg_entry,
                                font=('Verdana', '8', 'bold'))
        self.marcaIdEquipEntry = Entry(self.janelaCli)
        self.marcaEquipLabel.configure(font=('Verdana', '7', 'bold'))

    def provider_obj(self):
        self.descrCod_forn = Label(self.janelaFor, text=self.m_Codigo + self.m_Pontinhos,
                                   bg=self.fundo_do_frame, fg= self.fg_label, font=('Verdana', '10', 'bold'))
        self.entradaCod_forn = Entry(self.janelaFor, width=6, fg='brown', bg='white', font=('Verdana', '7', 'bold'))
        self.descrFornecedor = Label(self.janelaFor, text=self.m_Fornecedor + self.m_Pontinhos,
                                     bg=self.bg_label, fg= self.fg_label, font=('Verdana', '8'))
        self.entradaFornecedor = Entry(self.janelaFor, width=30, fg='brown', bg='white', font=('Verdana', '7', 'bold'))
        self.descrFone = Label(self.janelaFor, text=self.m_Fone + self.m_Pontinhos, bg=self.bg_label,
                               fg='darkblue', font=('Verdana', '8'))
        self.entradaFone = Entry(self.janelaFor, width=15, fg='brown', bg='white', font=('Verdana', '7', 'bold'))
        self.descrCnpj = Label(self.janelaFor, text=self.m_Cnpj + self.m_Pontinhos, bd=6, bg=self.bg_label,
                               fg= self.fg_label, font=('Verdana', '7'))
        self.entradaCnpj = Entry(self.janelaFor, width=15, fg='brown', bg='white', font=('Verdana', '7', 'bold'))
        self.entradaCep = Entry(self.janelaFor, width=15, fg='brown', bg='white', font=('Verdana', '7', 'bold'))
        self.descrEndereco = Label(self.janelaFor, text=self.m_Endereco + self.m_Pontinhos, bg=self.bg_label,
                                   fg='darkblue', font=('Verdana', '8'))
        self.entradaEndereco = Entry(self.janelaFor, width=40, fg='brown', bg='white', font=('Verdana', '7', 'bold'))
        self.descrMunicipio = Label(self.janelaFor, text=self.m_Cidade + self.m_Pontinhos, bg=self.bg_label,
                                    fg='darkblue', font=('Verdana', '8'))
        self.entradaMunicipio = Entry(self.janelaFor, width=30, fg='brown', bg='white', font=('Verdana', '7', 'bold'))
        self.descrDescricao = Label(self.janelaFor, text=self.m_Observacao + self.m_Pontinhos, bg=self.bg_label,
                                    fg='darkblue', font=('Verdana', '8'))
        self.entradaDescricao = Entry(self.janelaFor, width=40, fg='brown', bg='white', font=('Verdana', '7', 'bold'))
        self.botaoCarregarForn = Button(self.janelaFor, text=self.m_Carregar + ' ' + self.m_Fornecedor, bg='#37609b',
                               fg=self.fg_button, font=('Verdana', '8', 'bold'))
        self.botaoLimpaForn = Button(self.janelaFor, text=self.m_Limpar, bg='#37609b', fg=self.fg_button,
                                     font=('Verdana', '8', 'bold'))
        self.botaoBuscaForn = Button(self.janelaFor, text=self.m_Buscar, bg='#37609b', fg=self.fg_button,
                                     font=('Verdana', '8', 'bold'))
        self.botaoCepForn = Button(self.janelaFor, text=self.m_Cep, bg='#37609b', fg=self.fg_button,
                                   font=('Verdana', '10', 'bold'))
        self.botaoNovoForn = Button(self.janelaFor, text=self.m_Novo, bg='#37609b', fg=self.fg_button,
                                    font=('Verdana', '10', 'bold'))
        self.botaoAlterarForn = Button(self.janelaFor, text=self.m_Alterar, bg='#37609b', fg=self.fg_button,
                                       font=('Verdana', '10', 'bold'))
        self.botaoApagarFornecedor = Button(self.janelaFor, text=self.m_Apagar, font=('Verdana', '10', 'bold')
                                            , bg='brown', fg=self.fg_button)
    def model_car_obj(self):
        def validadores():
            self.vcmd4 = (self.janelaAut.register(self.validate_entry4), "%P")
        validadores()

        ####### Label do codigo
        self.descrCod_aut = Label(self.janelaAut, text=self.m_Codigo)
        self.descrCod_aut.configure(font=('Verdana', '10'), bg= self.bg_label, fg='darkblue')
        #### entrada do codigo
        self.entradaCod_autA = Entry(self.janelaAut, width=6, fg='brown', font=('Verdana', '9', 'bold') )
        self.entradaCod_autA.configure( bd=1, validate="key", validatecommand=self.vcmd4)
        ##### label da descrição do veiculo
        self.descrAut = Label(self.janelaAut, text=self.m_Automovel, bg= self.bg_label, fg='darkblue',
                              font=('Verdana', '10'))
        #### entry da marca
        self.entradaMarcaA = Entry(self.janelaAut, width=28, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaMarca2A = Entry(self.janelaAut, width=20)
        ##### entry da descrição do veiculo
        self.entradaAutA = Entry(self.janelaAut, width=22, fg='brown', font=('Verdana', '9', 'bold'))
        ##### label do titulo da janela
        self.descrNomeServ = Label(self.janelaAut, text=self.m_Automoveis, bg= self.fundo_da_tela, fg= self.fg_button,
                                   font=('Times', '18', 'bold', 'italic'))
        ###### botão busca
        self.botaoBuscaAut = Button(self.janelaAut, text=self.m_Buscar, bd=2, bg='#37609b', fg=self.fg_button,
                                    font=('Verdana', '9', 'bold'))
        ##### botao Carregar
        self.botaoCarregaAut = Button(self.janelaAut, text=self.m_Carregar, font=('Verdana', '8', 'bold'), bd=2,
                                      bg='#37609b', fg=self.fg_button)
        ##### botao limpa
        self.botaoLimpaAut = Button(self.janelaAut, text=self.m_Limpar, font=('Verdana', '8', 'bold'), bd=2,
                                    bg='#37609b', fg=self.fg_button)
        #### botao marca
        self.botaoMarcaAut = Button(self.janelaAut, text=self.m_Marca, bg='#37609b', fg=self.fg_button,
                                    font=('Verdana', '8', 'bold'))
        #####
        self.botaoNovoAut = Button(self.janelaAut, text=self.m_Novo,
                                   font=('Verdana', '12', 'bold'), bg='#37609b', fg=self.fg_button, bd=1)
        #####
        self.botaoAlterarAut = Button(self.janelaAut, text=self.m_Alterar, font=('Verdana', '12', 'bold'),
                                      bg='#37609b', fg=self.fg_button, bd=1)
        #####
        self.botaoApagarAut = Button(self.janelaAut, text=self.m_Apagar,
                                     font=('Verdana', '12', 'bold'), fg=self.fg_button, bg='brown', bd=1)
    def tech_obj(self):
        ###  Botao Novo Cliente
        self.botaoAdd = Button(self.janelaTec, text=self.m_Novo, bd=2, bg=self.bg_button, fg=self.fg_button,
                               font=('Verdana', '9', 'bold'))
        self.botaoAdd2 = Button(self.janelaTec, text=self.m_Novo, bd=2, bg=self.bg_button, fg=self.fg_button,
                               font=('Verdana', '9', 'bold'))
        ### Botao Altera dados do Cliente
        self.botaoMud = Button(self.janelaTec, bd=2, text=self.m_Alterar, bg=self.bg_button, fg=self.fg_button,
                                   font=('Verdana', '9', 'bold'))
        self.botaoMud2 = Button(self.janelaTec, bd=2, text=self.m_Alterar, bg=self.bg_button, fg=self.fg_button,
                               font=('Verdana', '9', 'bold'))
        ### Botao deletar dados do Cliente
        self.botaoDel = Button(self.janelaTec, bd=2, text=self.m_Apagar, bg='brown', fg=self.fg_button,
                                   font=('Verdana', '9', 'bold'))
        self.botaoDel2 = Button(self.janelaTec, bd=2, text=self.m_Apagar, bg='brown', fg=self.fg_button,
                               font=('Verdana', '9', 'bold'))
        ##  Botao limpa
        self.botaolimpa = Button(self.janelaTec, bd=1, text=self.m_Limpar, bg=self.bg_button, fg=self.fg_button,
                                 font=('Verdana', '9', 'bold'))
        ###  Botao busca Cabeça
        self.botaobusca = Button(self.janelaTec, bitmap='questhead', bg='#37609b', fg=self.fg_button,
                                 font=('Verdana', '8', 'bold'))
        ###  Botao busca Carregar
        self.botaoCarregar = Button(self.janelaTec, text= self.m_Carregar, bg='#37609b', fg=self.fg_button,
                                 font=('Verdana', '8', 'bold'))


