from objects_glac import *

class Empresa(Objects_Glac):
    def cademp(self):
        self.multiGlacx()
        self.cores();

        def abre_janela():
            self.janelaEmp = Toplevel()
            self.janelaEmp.title('Glacx' + self.m_Empresa)
            self.janelaEmp.configure(background=self.fundo_da_tela)
            self.janelaEmp.geometry("410x250")
            self.janelaEmp.resizable(FALSE, FALSE)
            self.janelaEmp.transient(self.janela)
            self.janelaEmp.focus_force()
            self.janelaEmp.grab_set()
        abre_janela()

        self.descrNomeServ = Label(self.janelaEmp, text=self.m_Estab, fg='gray75', bg=self.fundo_da_tela,
                                   font=('Times', '18', 'bold', 'italic'))
        self.descrNomeServ.place(x=75, y=1)

        self.cliente_canvas2 = Canvas(self.janelaEmp, width=380, height=190, cursor='X_cursor', bd=2,
                                      bg=self.fundo_do_frame)
        self.cliente_canvas2.place(x=8, y=38)

        self.entradaCod_emp = Entry(self.janelaEmp, width=6)

        ###  Descrição e Entrada Nome
        self.descrNome = Label(self.janelaEmp, text=self.m_Nome + self.m_Pontinhos, bg=self.fundo_do_frame,
                               fg='darkblue', font=('Verdana', '8', 'bold'))
        self.descrNome.place(x=10, y=53)
        self.entradaNome_emp = Entry(self.janelaEmp, width=32, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaNome_emp.place(x=85, y=53)

        ###  Descrição e Entrada Enedereco
        self.descrEndereco = Label(self.janelaEmp, text=self.m_Endereco + self.m_Pontinhos, bg=self.fundo_do_frame,
                                   fg='darkblue', font=('Verdana', '8', 'bold'))
        self.descrEndereco.place(x=10, y=83)
        self.entradaEndereco_emp = Entry(self.janelaEmp, width=32, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaEndereco_emp.place(x=85, y=83)

        ###  Descrição e Entrada Bairro
        self.descrBairro = Label(self.janelaEmp, text=self.m_Bairro + self.m_Pontinhos, bg=self.fundo_do_frame,
                                 fg='darkblue', font=('Verdana', '8', 'bold'))
        self.descrBairro.place(x=10, y=103)
        self.entradaBairro_emp = Entry(self.janelaEmp, width=32, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaBairro_emp.place(x=85, y=103)

        ###  Descrição e Entrada Municipio
        self.descrMunicipio = Label(self.janelaEmp, text=self.m_Cidade + self.m_Pontinhos, bg=self.fundo_do_frame,
                                    fg='darkblue', font=('Verdana', '8', 'bold'))
        self.descrMunicipio.place(x=10, y=123)
        self.entradaMunicipio_emp = Entry(self.janelaEmp, width=27, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaMunicipio_emp.place(x=85, y=123)

        ###  Descrição e Entrada UF
        self.descrUf = Label(self.janelaEmp, text=self.m_Uf, bg=self.fundo_do_frame, fg='darkblue',
                             font=('Verdana', '10', 'bold'))
        self.descrUf.place(x=320, y=123)
        self.entradaUf_emp = Entry(self.janelaEmp, width=2, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaUf_emp.place(x=350, y=123)

        ###  Descrição e Entrada Fone
        self.descrFone = Label(self.janelaEmp, text=self.m_Fone + self.m_Pontinhos, bg=self.fundo_do_frame,
                               fg='darkblue', font=('Verdana', '8', 'bold'))
        self.descrFone.place(x=10, y=143)
        self.entradaFone_emp = Entry(self.janelaEmp, width=14, fg='brown',  font=('Verdana', '9', 'bold'))
        self.entradaFone_emp.place(x=85, y=143)

        ###  Descrição e Entrada Cep
        self.descrCep = Label(self.janelaEmp, text=self.m_Cep, bg=self.fundo_do_frame, fg='darkblue',
                              font=('Verdana', '10', 'bold'))
        self.descrCep.place(x=220, y=143)
        self.entradaCep_emp = Entry(self.janelaEmp, width=12, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaCep_emp.place(x=260, y=143)

        ###  Descrição e Entrada Cpf
        self.descrCpf = Label(self.janelaEmp, text=self.m_Cnpj + self.m_Pontinhos, bg=self.fundo_do_frame, fg='darkblue',
                              font=('Verdana', '8', 'bold'))
        self.descrCpf.place(x=10, y=163)
        self.entradaCpf_emp = Entry(self.janelaEmp, width=15, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaCpf_emp.place(x=85, y=163)

        ###  Descrição e Entrada Rg
        self.descrRg = Label(self.janelaEmp, text=self.m_Cpf, bg=self.fundo_do_frame, fg='darkblue',
                             font=('Verdana', '10', 'bold'))
        self.descrRg.place(x=230, y=163)
        self.entradaRg_emp = Entry(self.janelaEmp, width=12, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaRg_emp.place(x=260, y=163)

        ###  Descrição e Entrada Obs
        self.descrObs = Label(self.janelaEmp, text=self.m_Obs + self.m_Pontinhos, bg=self.fundo_do_frame, fg='darkblue',
                              font=('Verdana', '10', 'bold'))
        self.descrObs.place(x=10, y=193)
        self.entradaObs_emp = Entry(self.janelaEmp, width=32, fg='brown', font=('Verdana', '9', 'bold'))
        self.entradaObs_emp.place(x=85, y=193)

        ### Botao Altera dados do Cliente
        # self.botaoMudServ = Button(self.janelaEmp, text= multilingua.Alterar, command=self.mud_empresa, fg='darkblue', bd=3,
        #                   font=('Verdana', '12', 'bold'))
        # self.botaoMudServ.place(x=150, y=250, width=80)
        self.conecta_Glac()

        lista = self.cursor.execute("""
                SELECT cod_emp FROM empresa;
                """)
        for i in lista:
            self.entradaCod_emp.insert(END, i)

        self.desconecta_Glac()

        self.carrega_empresa()
        self.janelaEmp.mainloop()
    def carrega_empresa(self):
        cod_emp = self.entradaCod_emp.get()

        self.entradaNome_emp.delete(0, END)
        self.entradaEndereco_emp.delete(0, END)
        self.entradaBairro_emp.delete(0, END)
        self.entradaMunicipio_emp.delete(0, END)
        self.entradaUf_emp.delete(0, END)
        self.entradaFone_emp.delete(0, END)
        self.entradaCep_emp.delete(0, END)
        self.entradaCpf_emp.delete(0, END)
        self.entradaRg_emp.delete(0, END)
        self.entradaObs_emp.delete(0, END)

        self.entradaNome_emp.insert(END, licence.NomeEmpresa)
        self.entradaEndereco_emp.insert(END, licence.NomeRuaEmp)
        self.entradaBairro_emp.insert(END, licence.NomeBairroEmp)
        self.entradaMunicipio_emp.insert(END, licence.MunicipioEmp)
        self.entradaFone_emp.insert(END, licence.TelefoneEmp)
        self.entradaCpf_emp.insert(END, licence.LicencaCpf)
        self.entradaObs_emp.insert(END, licence.Licenca)
