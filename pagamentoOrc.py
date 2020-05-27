from objects_glac import *

class PagamentoOrc(Objects_Glac):
    def consultapag(self):
        self.multiGlacx()

        self.janelaPagOrc = Toplevel();
        self.janelaPagOrc.title("GlacX")
        self.janelaPagOrc.configure(background='lavender');
        self.janelaPagOrc.geometry("800x495")
        self.janelaPagOrc.resizable(FALSE, FALSE)
        self.janelaPagOrc.transient(self.janela)
        self.janelaPagOrc.focus_force()
        self.janelaPagOrc.grab_set()

        ### Label principal
        self.labelformapag = Label(self.janelaPagOrc, text=self.m_Consulta + ' ' + self.m_Pagamento)
        self.labelformapag.configure(bg='lavender', fg='brown', font=('Comic', '16', 'bold', 'italic'))
        self.labelformapag.place(relx=0.35, rely=0)

        ###  Frame Moldura
        self.frame1 = Frame(self.janelaPagOrc)
        self.frame1.configure(background='lightgray')
        self.frame1.place(relx=0, rely=0.06, relwidth=1, relheight=1)
        self.frame2 = Frame(self.frame1, bd=4, bg='gray55')
        self.frame2.place(relx=0.01, rely=0.01, relwidth=1, relheight=1)
        self.frame3 = Frame(self.frame2, bd=4, bg='lightgray', relief=SUNKEN)
        self.frame3.place(relx=0.02, rely=0.02, relwidth=1, relheight=1)

        self.consulta1()

        self.consulta2()

        ### Widgets - Listar pagamentos ###
        ### Frame lista
        self.framelista = Frame(self.frame3, bg='darkblue')
        self.framelista.place(relx=0.022, rely=0.32, width=742, height=238)
        self.framelista = Frame(self.frame3, bg='lightblue')
        self.framelista.place(relx=0.026, rely=0.33, width=737, height=232)

        ### Lista de pagamentos
        self.listaPag = ttk.Treeview(self.frame3, height=10,
                                     column=("col1", "col2", "col3", "col4",
                                             "col5", "col6", "col7", "col8", "col9"))

        self.listaPag.heading("#0", text="");
        self.listaPag.column("#0", width=0)
        self.listaPag.heading("#1", text=self.m_Ordem);
        self.listaPag.column("#1", width=60)
        self.listaPag.heading("#2", text=self.m_Tipo);
        self.listaPag.column("#2", width=220)
        self.listaPag.heading("#3", text="");
        self.listaPag.column("#3", width=1)
        self.listaPag.heading("#4", text=self.m_Valor);
        self.listaPag.column("#4", width=120)
        self.listaPag.heading("#5", text=self.m_Dia);
        self.listaPag.column("#5", width=60)
        self.listaPag.heading("#6", text=self.m_Mes);
        self.listaPag.column("#6", width=60)
        self.listaPag.heading("#7", text=self.m_Ano);
        self.listaPag.column("#7", width=60)
        self.listaPag.heading("#8", text=self.m_Pago);
        self.listaPag.column("#8", width=110)
        self.listaPag.heading("#9", text="");
        self.listaPag.column("#9", width=1)
        self.listaPag.place(relx=0.03, rely=0.34)

        # Cria barra de rolagem
        self.barraMov = Scrollbar(self.frame3, orient='vertical', command=self.listaPag.yview)
        self.barraMov.place(relx=0.916, rely=0.34, width=38, height=227)

        self.listaPag.bind("<Double-1>")  # , self.OnDoubleClickpag)
        self.listaPag.configure(yscroll=self.barraMov.set)

        #### Frame do Valor a ser inserido
        self.frameValor = Frame(self.frame3, bg='darkblue')
        self.frameValor.place(x=590, y=392, width=110, height=52)
        self.frameValor = Frame(self.frame3, bg='lightblue')
        self.frameValor.place(x=593, y=394, width=105, height=50)

        ### Label do saldo a ser pago
        self.labelValor = Label(self.frame3, text=self.m_Valor + ' ' + self.m_Total)
        self.labelValor.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelValor.place(x=600, y=395)
        self.labelCifrao = Label(self.frame3, text=self.m_Reais)
        self.labelCifrao.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelCifrao.place(x=600, y=415)

        #### Entry do saldo a ser pago
        self.entryValorDevido = Entry(self.frame3, bd=1, fg='brown')
        self.entryValorDevido.configure(width='8', font=('Verdana', '8', 'bold'), validate="key")
        self.entryValorDevido.place(x=620, y=415)

        self.janelaPagOrc.mainloop()
    def consulta1(self):
        #### Frame do Valor a ser inserido
        self.frameValor = Frame(self.frame3, bg='darkblue')
        self.frameValor.place(relx=0.001, rely=0.018, width=550, height=52)
        self.frameValor = Frame(self.frame3, bg='lightblue')
        self.frameValor.place(relx=0.004, rely=0.02, width=547, height=50)

        #### Listbox do tipo de pagamento
        self.entrytipopag = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entrytipopag.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrytipopag.columnconfigure(0, weight=1)
        self.entrytipopag.rowconfigure(0, weight=1)
        self.entrytipopag.place(relx=0.16, rely=0.022, width=120, height=45)
        self.listtipopag = StringVar(self.frame3)
        self.listtipopagV = {self.m_Debito, self.m_Credito, self.m_Dinheiro, self.m_Boleto, self.m_ChequePre,
                             self.m_ChequeVista, self.m_Crediario, self.m_Promissoria, self.m_Desconto, self.m_Avista}
        self.listtipopagV = sorted(self.listtipopagV)
        self.listtipopag.set(self.m_Dinheiro)
        self.popupMenu = OptionMenu(self.entrytipopag, self.listtipopag, *self.listtipopagV)
        Label(self.entrytipopag, bd=0, text= self.m_Tipo + ' ' + self.m_Pagamento, fg='darkblue',
              bg='lightblue').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        #### Entry data

        self.entrymes = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entrymes.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrymes.columnconfigure(0, weight=1)
        self.entrymes.rowconfigure(0, weight=1)
        self.entrymes.place(relx=0.006, rely=0.022, width=55, height=45)
        self.mesvar = StringVar(self.frame3)
        self.mesesV = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                       '11', '12'}
        self.mesesV = sorted(self.mesesV)
        self.mesvar.set('01')
        self.popupMenu = OptionMenu(self.entrymes, self.mesvar, *self.mesesV)
        Label(self.entrymes, bd=0, text='Mês', fg='darkblue',
              bg='lightblue').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        self.entryano = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entryano.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entryano.columnconfigure(0, weight=1)
        self.entryano.rowconfigure(0, weight=1)
        self.entryano.place(relx=0.08, rely=0.022, width=70, height=45)
        self.anovar = StringVar(self.frame3)
        self.anosV = {'2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028',
                      '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038'}
        self.anosV = sorted(self.anosV)
        self.anovar.set('2019')
        self.popupMenu = OptionMenu(self.entryano, self.anovar, *self.anosV)
        Label(self.entryano, bd=0, text='Ano', fg='darkblue',
              bg='lightblue').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        #### Pago?
        ### Pago?
        self.entrypago = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entrypago.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrypago.columnconfigure(0, weight=1)
        self.entrypago.rowconfigure(0, weight=1)
        self.entrypago.place(x=260, y=11, width=65, height=45)
        self.entry7 = StringVar(self.frame3)
        self.entry7V = { self.m_Sim, self.m_Nao}
        self.entry7V = sorted(self.entry7V)
        self.entry7.set(self.m_Sim)

        self.popupMenu = OptionMenu(self.entrypago, self.entry7, *self.entry7V)
        Label(self.entrypago, text= self.m_Pago, bd=0, bg='lightblue', fg='darkblue').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        #### Button Inserir Registro
        self.btinserir = Button(self.frame3, text= self.m_Consulta + ' ' + self.m_Competência + self.m_barra +
                                self.m_Tipo + self.m_barra + self.m_Pago, bg = '#37609b', fg = 'white',
                                font=('Comic', '8', 'bold'), command=self.carregaConsulta)
        self.btinserir.place(relx=0.44, rely=0.06, width = 205)
    def consulta2(self):
        #### Frame do Valor a ser inserido
        self.frameValor2 = Frame(self.frame3, bg='darkblue')
        self.frameValor2.place(relx=0.001, rely=0.128, width=550, height=52)
        self.frameValor2 = Frame(self.frame3, bg='lightblue')
        self.frameValor2.place(relx=0.004, rely=0.13, width=547, height=50)

        #### Listbox do tipo de pagamento
        self.entrytipopag2 = Label(self.frame3, text= self.m_Tipo + ' ' + self.m_Pagamento, fg='darkblue',
                                  bd=0, bg='lightblue', width=2)
        self.entrytipopag2.place(relx=0.16, rely=0.132, width=120)
        self.entrytipopag2 = Label(self.frame3, text='Todos', fg='darkblue',
                                  bd=0, bg='lightgray', width=2)
        self.entrytipopag2.place(relx=0.16, rely=0.17, width=120)


        #### Entry data

        self.entrymes2 = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entrymes2.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrymes2.columnconfigure(0, weight=1)
        self.entrymes2.rowconfigure(0, weight=1)
        self.entrymes2.place(relx=0.006, rely=0.132, width=55, height=45)
        self.mesvar2 = StringVar(self.frame3)
        self.mesesV2 = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                       '11', '12'}
        self.mesesV2 = sorted(self.mesesV2)
        self.mesvar2.set('01')
        self.popupMenu2 = OptionMenu(self.entrymes2, self.mesvar2, *self.mesesV2)
        Label(self.entrymes2, bd=0, text='Mês', fg='darkblue',
              bg='lightblue').grid(row=1, column=1)
        self.popupMenu2.grid(row=2, column=1)

        self.entryano2 = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entryano2.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entryano2.columnconfigure(0, weight=1)
        self.entryano2.rowconfigure(0, weight=1)
        self.entryano2.place(relx=0.08, rely=0.132, width=70, height=45)
        self.anovar2 = StringVar(self.frame3)
        self.anosV2 = {'2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028',
                      '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038'}
        self.anosV2 = sorted(self.anosV2)
        self.anovar2.set('2019')
        self.popupMenu2 = OptionMenu(self.entryano2, self.anovar2, *self.anosV2)
        Label(self.entryano2, bd=0, text= self.m_Ano, fg='darkblue',
              bg='lightblue').grid(row=1, column=1)
        self.popupMenu2.grid(row=2, column=1)

        #### Pago?
        ### Pago?
        self.entrypago2 = Frame(self.frame3, bd=0, bg='lightblue', width=2)
        self.entrypago2.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrypago2.columnconfigure(0, weight=1)
        self.entrypago2.rowconfigure(0, weight=1)
        self.entrypago2.place(x=260, y=61, width=65, height=45)
        self.entry72 = StringVar(self.frame3)
        self.entry7V2 = {self.m_Sim, self.m_Nao}
        self.entry7V2 = sorted(self.entry7V2)
        self.entry72.set(self.m_Sim)

        self.popupMenu2 = OptionMenu(self.entrypago2, self.entry72, *self.entry7V2)
        Label(self.entrypago2, text= self.m_Pago, bd=0, bg='lightblue', fg='darkblue').grid(row=1, column=1)
        self.popupMenu2.grid(row=2, column=1)

        #### Button Inserir Registro
        self.btinserir = Button(self.frame3, text= self.m_Consulta + ' ' + self.m_Competência + self.m_barra
                                + self.m_Pago, bg = '#37609b', fg = 'white',
                                font=('Comic', '8', 'bold'), command=self.carregaConsulta2)
        self.btinserir.place(relx=0.44, rely=0.17, width = 205)
    def pagaOrdem(self):
        conn = sqlite3.connect("glac.db");        cursor = conn.cursor()
        numAt = self.listaNumOrc.get()

        self.janelaPagOrc = Tk();  self.janelaPagOrc.title("GlacX");  self.janelaPagOrc.configure(background= self.fundo_da_tela);
        self.janelaPagOrc.geometry("800x495"); self.janelaPagOrc.resizable(FALSE, FALSE)
        ### Label principal
        self.labelformapag = Label(self.janelaPagOrc, text= self.m_Forma)
        self.labelformapag.configure(bg= self.fundo_da_tela, fg= self.bg_entry,font=('Comic','18','bold', 'italic'))
        self.labelformapag.place(relx=0.35, rely=0)
        ###  Frame Moldura
        self.frame1 = Frame(self.janelaPagOrc); self.frame1.configure(background= self.fg_label)
        self.frame1.place(relx=0, rely=0.1, relwidth=1, relheight=1)
        self.frame2 = Frame(self.frame1, bd=4, bg=self.bg_button)
        self.frame2.place(relx=0.01, rely=0.01, relwidth=1, relheight=1)
        self.frame3 = Frame(self.frame2, bd=4, bg= self.fundo_do_frame, relief=SUNKEN)
        self.frame3.place(relx=0.02, rely=0.02, relwidth=1, relheight=1)
        ### Frame do Numero do Atendimento e Valor Total
        self.frameAt = Frame(self.frame3, bg=self.bg_button)
        self.frameAt.place(relx=0, rely=0, width=205, height=44)
        self.frameAt2 = Frame(self.frame3, bg=self.fundo_do_frame)
        self.frameAt2.place(relx=0.002, rely=0.002, width=202, height=42)
        ## Label do numero de atendimento
        self.labelNumAtend = Label(self.frame3, text= self.m_NumAtend)
        self.labelNumAtend.configure(fg=self.fg_label, font=('Verdana', '8', 'bold'), bg=self.fundo_do_frame)
        self.labelNumAtend.place(relx=0.006, rely=0.006)
        #### Entry do numero de atendimento
        self.entryNumAtend = Listbox(self.frame3, height = 1)
        self.entryNumAtend.configure(bd=1, fg='brown', bg = 'lightgray', width='10', font=('Verdana', '8', 'bold'))
        self.entryNumAtend.place(relx=0.15, rely=0.006);  self.entryNumAtend.insert(END, numAt)
        #### Label do valor total
        self.labelValorTotal = Label(self.frame3, fg=self.fg_label)
        self.labelValorTotal.configure(text= self.m_Valor + ' ' + self.m_Total,
                                       font=('Verdana', '8', 'bold'), bg=self.fundo_do_frame)
        self.labelValorTotal.place(relx=0.006, rely=0.05)
        #### Entry do valor total
        valorT = self.entradatotal.get()
        self.entryValorTotal = Entry(self.frame3, bd=1, fg='brown', bg= 'lightgray')
        self.entryValorTotal.configure(width='10', font=('Verdana', '8', 'bold'))
        self.entryValorTotal.place(relx=0.15, rely=0.05);
        totalsimples = self.entradatotal.get()
        totalsimples = totalsimples.replace("R$","").replace(",",".")
        self.entryValorTotal.insert(END, totalsimples)
        #### Frame do Valor a ser inserido
        self.frameValor = Frame(self.frame3, bg= self.bg_label)
        self.frameValor.place(relx=0.448, rely=0.018, width=100, height=36)
        self.frameValor = Frame(self.frame3, bg= self.bg_label)
        self.frameValor.place(relx=0.45, rely=0.02, width=97, height=34)
        ### Label do valor a ser inserido
        self.labelValor = Label(self.frame3, text= self.m_Valor)
        self.labelValor.configure(fg= self.fg_label, font=('Verdana', '8', 'bold'), bg= self.fg_button)
        self.labelValor.place(relx=0.45, rely=0.02, width = 90)
        self.labelCifrao = Label(self.frame3, text= self.m_Reais)
        self.labelCifrao.configure(fg=self.fg_label, font=('Verdana', '8', 'bold'), bg=self.fg_button)
        self.labelCifrao.place(relx=0.45, rely=0.05)
        #### Entry do valor a ser inserido
        self.entryValor = Entry(self.frame3, bd=1, fg='brown')
        self.entryValor.configure(width='8', font=('Verdana', '8', 'bold'), validate="key")
        self.entryValor.place(relx=0.48, rely=0.055); self.entryValor.insert(END, '0.00')
        #### Frame do tipo de pagamento
        self.frametipopag = Frame(self.frame3, bg= self.bg_button)
        self.frametipopag.place(relx=0.586, rely=0, width=105, height=48)

        #### Listbox do tipo de pagamento
        self.entrytipopag = Frame(self.frame3, bd=0, bg= self.fg_button, width=2)
        self.entrytipopag.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrytipopag.columnconfigure(0, weight=1)
        self.entrytipopag.rowconfigure(0, weight=1)
        self.entrytipopag.place(relx=0.588, rely=0.003, width=100, height=45)
        self.listtipopag = StringVar(self.frame3)
        self.listtipopagV = { self.m_Debito, self.m_Credito, self.m_Dinheiro, self.m_Boleto,
                              self.m_ChequePre, self.m_ChequeVista, self.m_Crediario, self.m_Promissoria,
                              self.m_Desconto, self.m_Avista}
        self.listtipopagV = sorted(self.listtipopagV)
        self.listtipopag.set(self.m_Dinheiro)
        self.popupMenu = OptionMenu(self.entrytipopag, self.listtipopag, *self.listtipopagV)
        Label(self.entrytipopag, bd=0).grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)
        #### Label do tipo de pagamento
        self.labeltipopag = Label(self.frame3, text= self.m_Tipo + ' ' + self.m_Pagamento)
        self.labeltipopag.configure(fg=self.fg_label, font=('Verdana', '7', 'bold'), bg=self.fg_button)
        self.labeltipopag.place(relx=0.60, rely=0.003)
        #### Data frame
        self.framedata=Frame(self.frame3,bg=self.bg_button)
        self.framedata.place(relx=0.718, rely=0, width=98, height=48)
        self.framedata = Frame(self.frame3, bg=self.fg_button)
        self.framedata.place(relx=0.72, rely=0.003, width=95, height=45)
        #### Entry data
        self.entrydia = Frame(self.frame3, bd=0, bg=self.fg_label, width=2)
        self.entrydia.grid(column=0, row=0, sticky=(N, W, E, S)); self.entrydia.columnconfigure(0, weight=1)
        self.entrydia.rowconfigure(0, weight=1); self.entrydia.place(relx=0.72, rely=0.003, width=30, height=45)
        self.diavar = StringVar(self.frame3)
        self.diasV = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                      '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                      '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'}
        self.diasV = sorted(self.diasV); self.diavar.set('01')
        self.popupMenu = OptionMenu(self.entrydia, self.diavar, *self.diasV)
        Label(self.entrydia, bd=0).grid(row=1, column=1);  self.popupMenu.grid(row=2, column=1)

        self.entrymes = Frame(self.frame3, bd=0, bg='azure3', width=2)
        self.entrymes.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrymes.columnconfigure(0, weight=1)
        self.entrymes.rowconfigure(0, weight=1)
        self.entrymes.place(relx=0.75, rely=0.003, width=30, height=45)
        self.mesvar = StringVar(self.frame3)
        self.mesesV = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                      '11', '12'}
        self.mesesV = sorted(self.mesesV)
        self.mesvar.set('01')
        self.popupMenu = OptionMenu(self.entrymes, self.mesvar, *self.mesesV)
        Label(self.entrymes, bd=0).grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        self.entryano = Frame(self.frame3, bd=0, bg='azure3', width=2)
        self.entryano.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entryano.columnconfigure(0, weight=1)
        self.entryano.rowconfigure(0, weight=1)
        self.entryano.place(relx=0.78, rely=0.003, width=40, height=45)
        self.anovar = StringVar(self.frame3)
        self.anosV = {'2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028',
                       '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038'}
        self.anosV = sorted(self.anosV)
        self.anovar.set('2019')
        self.popupMenu = OptionMenu(self.entryano, self.anovar, *self.anosV)
        Label(self.entryano, bd=0).grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)
        #### Data label
        self.labeldata = Label(self.frame3, text= self.m_Data, fg=self.fg_label)
        self.labeldata.configure(bg=self.fg_button, font=('Verdana', '8', 'bold'))
        self.labeldata.place(relx=0.72, rely=0.002, width = 95, height=18)
        #### Button Inserir Registro
        self.btinserir = Button(self.frame3, text= self.m_Inserir, command= self.add_pag)
        self.btinserir.place(relx=0.85, rely=0.04)
        ### Widgets - Listar pagamentos ###
        ### Frame lista
        self.framelista = Frame(self.frame3, bg=self.fg_label)
        self.framelista.place(relx=0.024, rely=0.113, width=745, height=318)
        self.framelista = Frame(self.frame3, bg=self.bg_label)
        self.framelista.place(relx=0.026, rely=0.115, width=742, height=315)
        ### Lista de pagamentos
        self.listaPag = ttk.Treeview(self.frame3, height=14,
            column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.listaPag.heading("#0", text=""); self.listaPag.column("#0", width=0)
        self.listaPag.heading("#1", text= self.m_Ordem); self.listaPag.column("#1", width=50)
        self.listaPag.heading("#2", text= self.m_Tipo);  self.listaPag.column("#2", width=170)
        self.listaPag.heading("#3", text= self.m_Valor + ' ' + self.m_Pagamento);
        self.listaPag.column("#3", width=120)
        self.listaPag.heading("#4", text= self.m_ValorDeduzir); self.listaPag.column("#4", width=120)
        self.listaPag.heading("#5", text= self.m_Dia);  self.listaPag.column("#5", width=50)
        self.listaPag.heading("#6", text= self.m_Mes);  self.listaPag.column("#6", width=50)
        self.listaPag.heading("#7", text= self.m_Mes);  self.listaPag.column("#7", width=50)
        self.listaPag.heading("#8", text= self.m_Pago); self.listaPag.column("#8", width=100)
        self.listaPag.heading("#9", text=""); self.listaPag.column("#9", width=1)
        self.listaPag.place(relx=0.03, rely=0.12)
        # Cria barra de rolagem
        self.barraMov = Scrollbar(self.frame3, orient='vertical', command=self.listaPag.yview)
        self.barraMov.place(relx=0.917, rely=0.12, width=38, height=310)

        self.listaPag.bind("<Double-1>", self.OnDoubleClickpag); self.listaPag.configure(yscroll=self.barraMov.set)
        ### Label do saldo a ser pago
        self.labelValor = Label(self.frame3, text= self.m_ValorDevido)
        self.labelValor.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelValor.place(x=600, y=375)
        self.labelCifrao = Label(self.frame3, text="R$")
        self.labelCifrao.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelCifrao.place(x=600, y=395)

        #### Entry do saldo a ser pago
        self.entryValorDevido = Entry(self.frame3, bd=1, fg='brown')
        self.entryValorDevido.configure(width='8', font=('Verdana', '8', 'bold'), validate="key")
        self.entryValorDevido.place(x=620, y=395)

        ### Label do saldo ja pago
        self.labelValor = Label(self.frame3, text= self.m_ValorInformado)
        self.labelValor.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelValor.place(x=460, y=375)
        self.labelCifrao = Label(self.frame3, text= self.m_Reais)
        self.labelCifrao.configure(fg='darkblue', font=('Verdana', '8', 'bold'), bg='lightblue')
        self.labelCifrao.place(x=460, y=395)

        #### Entry do saldo ja pago
        self.entryValorInform = Entry(self.frame3, bd=1, fg='brown')
        self.entryValorInform.configure(width='8', font=('Verdana', '8', 'bold'), validate="key")
        self.entryValorInform.place(x=480, y=395)


        lista = cursor.execute("""
                           SELECT  ordem, tipopag, valorpagar, valordeduzir, dia, mes, ano, pago, id
                            FROM formapag WHERE ordem = '%s'   ORDER BY id ASC;
                           """ % numAt)
        for i in lista:
            self.listaPag.insert("", END, values=i)

        informe = cursor.execute("""
                                   SELECT SUM(valordeduzir) FROM formapag WHERE ordem = '%s'   ORDER BY id ASC;
                                   """ % numAt)
        for i in informe:
            self.entryValorInform.insert(END, i)

        rest1 = self.entryValorTotal.get()
        rest1 = float(rest1)
        rest2 = self.entryValorInform.get()
        rest2 = float(rest2)
        restante = rest1 - rest2
        #restante = self.entryValorDevido.get()
        self.entryValorDevido.insert(END, restante)

        conn.close()
        self.janelaPagOrc.mainloop()
    def add_pag(self):
        ordem = self.listaNumOrc.get()
        tipopag = self.listtipopag.get()
        valortotal = self.entryValorTotal.get()
        valordeduzir = self.entryValor.get()
        dia = self.diavar.get()
        mes = self.mesvar.get()
        ano = self.anovar.get()
        pago = "Não"

        self.conecta_Glac()

        self.cursor.execute("""
       		INSERT INTO formapag ( ordem, tipopag, valorpagar, valordeduzir, dia, mes , ano, pago)
       		VALUES ( ?, ?, ?, ?, ?, ?, ? , ?)""",
                       (ordem, tipopag, valortotal, valordeduzir, dia, mes, ano, pago))
        self.conn.commit()

        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
               SELECT  ordem, tipopag, valorpagar, valordeduzir, dia, mes, ano, pago
                FROM formapag WHERE ordem = '%s'  ORDER BY id ASC;
               """ % ordem)
        for i in lista:
            self.listaPag.insert("", END, values=i)

        informe = self.cursor.execute("""
                                           SELECT SUM(valordeduzir) FROM formapag WHERE ordem = '%s'   ORDER BY id ASC;
                                           """ % ordem)
        for i in informe:
            self.entryValorInform.delete(0, END)
            self.entryValorInform.insert(END, i)

        self.entryValor.delete(0, END)

        self.desconecta_Glac()
        self.janelaPagOrc.destroy()
        #msg = "Pagamento incluido com sucesso"
        #msg += ""
        #messagebox.showinfo("GLAC - Pagamentos", msg)
        self.pagaOrdem()
    def mud_pag(self):
        self.conecta_Glac()

        tipopag = self.entry2.get()
        valor = self.entry3.get()
        diaA = self.entry4.get()
        mesA = self.entry5.get()
        anoA = self.entry6.get()
        pago = self.entry7.get()
        idA = self.entry9.get()

        self.cursor.execute(""" UPDATE formapag SET tipopag = ?, valordeduzir = ?, dia = ?,
            mes = ?, ano = ?, pago = ? WHERE id = ? """,
                       (tipopag, valor, diaA, mesA, anoA, pago, idA))
        self.conn.commit()

        self.desconecta_Glac()
        self.janPag2.destroy()
        self.janelaPagOrc.destroy()
        self.pagaOrdem()
    def carregaConsulta(self):
        self.conecta_Glac()

        tipopag = self.listtipopag.get()
        valor = self.entryValorDevido.get()

        mes = self.mesvar.get()
        ano = self.anovar.get()
        pago = self.entry7.get()


        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
                       SELECT  ordem, tipopag, '*', valordeduzir, dia, mes, ano, pago
                        FROM formapag WHERE tipopag = ? AND  mes = ? AND ano = ?
                        AND pago = ? ORDER BY id ASC; """, (tipopag, mes, ano, pago))
        for i in lista:
            self.listaPag.insert("", END, values=i)

        self.entryValorDevido.delete(0, END)

        lista2 = self.cursor.execute("""
                               SELECT  SUM(valordeduzir)
                                FROM formapag WHERE tipopag = ? AND  mes = ? AND ano = ?
                                AND pago = ? ORDER BY id ASC; """, (tipopag, mes, ano, pago))
        for i in lista2:
            self.entryValorDevido.insert(END, i)

        self.desconecta_Glac()
    def carregaConsulta2(self):
        mes = self.mesvar2.get()
        ano = self.anovar2.get()
        pago = self.entry72.get()

        self.conn = sqlite3.connect("glac.db")
        self.cursor = self.conn.cursor()

        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
                       SELECT  ordem, tipopag, '*', valordeduzir, dia, mes, ano, pago
                        FROM formapag WHERE  mes = ? AND ano = ?
                        AND pago = ? ORDER BY id ASC; """, ( mes, ano, pago))
        for i in lista:
            self.listaPag.insert("", END, values=i)

        self.entryValorDevido.delete(0, END)

        lista2 = self.cursor.execute("""
                                       SELECT  SUM(valordeduzir)
                                        FROM formapag WHERE mes = ? AND ano = ?
                                        AND pago = ? ORDER BY id ASC; """, ( mes, ano, pago))
        for i in lista2:
            self.entryValorDevido.insert(END, i)


        self.conn.close()
    def OnDoubleClickpag(self, event):
        self.listaPag.selection()

        self.janPag2 = Tk();
        self.janPag2.title("GlacX")
        self.janPag2.configure(background='lavender');
        self.janPag2.geometry("480x85")
        self.janPag2.resizable(FALSE, FALSE)

        ## Entry NUm Atend
        self.label1 = Label(self.janPag2, text = self.m_NumAtend)
        self.label1.place(x=10, y=30)
        self.entry1 = Listbox(self.janPag2, width=8, height = 1)
        self.entry1.place(x=10, y=50)

        #### Listbox do tipo de pagamento
        self.entrytipopag = Frame(self.janPag2, bd=0, bg='lavender', width=2)
        self.entrytipopag.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrytipopag.columnconfigure(0, weight=1)
        self.entrytipopag.rowconfigure(0, weight=1)
        self.entrytipopag.place(x=70, y=30, width=120, height=40)
        self.entry2 = StringVar(self.janPag2)
        self.entry2V = {self.m_Debito, self.m_Credito, self.m_Dinheiro, self.m_Boleto, self.m_ChequePre,
                        self.m_ChequeVista, self.m_Crediario, self.m_Promissoria, self.m_Desconto, self.m_Avista}
        self.entry2V = sorted(self.entry2V)

        self.popupMenu = OptionMenu(self.entrytipopag, self.entry2, *self.entry2V)
        Label(self.entrytipopag, text= self.m_Tipo + ' ' + self.m_Pagamento,bd=0, bg = 'lavender').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        #### Valor da parcela
        self.label1 = Label(self.janPag2, text= self.m_Valor_R)
        self.label1.place(x=210, y=30)
        self.entry3 = Entry(self.janPag2, width = 10)
        self.entry3.place(x=200, y=50)

        ### dia
        self.label1 = Label(self.janPag2, text= self.m_Data + ' ' + self.m_Pagamento)
        self.label1.place(x=285, y=30)
        self.entry4 = Entry(self.janPag2, width = 2)
        self.entry4.place(x=280, y=50)
        self.entry5 = Entry(self.janPag2, width = 2)
        self.entry5.place(x=300, y=50)
        self.entry6 = Entry(self.janPag2, width = 4)
        self.entry6.place(x=320, y=50)

        ### Pago?
        self.label1 = Label(self.janPag2, text= self.m_Pago)
        self.label1.place(x=360, y=30)
        self.entry7 = Entry(self.janPag2, width=6)
        self.entry7.place(x=360, y=50)
        self.entrypago = Frame(self.janPag2, bd=0, bg='lavender', width=2)
        self.entrypago.grid(column=0, row=0, sticky=(N, W, E, S))
        self.entrypago.columnconfigure(0, weight=1)
        self.entrypago.rowconfigure(0, weight=1)
        self.entrypago.place(x=360, y=30, width=55, height=40)
        self.entry7 = StringVar(self.janPag2)
        self.entry7V = {self.m_Sim, self.m_Nao}
        self.entry7V = sorted(self.entry7V)

        self.popupMenu = OptionMenu(self.entrypago, self.entry7, *self.entry7V)
        Label(self.entrypago, text= self.m_Pago, bd=0, bg='lavender').grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        ### Alterar registro
        self.button1 = Button(self.janPag2, text = self.m_Alterar, command = self.mud_pag)
        self.button1.place(x=430, y=47)

        self.entry9 = Entry(self.janPag2)

        for n in self.listaPag.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listaPag.item(n, 'values')
            self.entry1.insert(END, col1)
            self.entry2.set(col2)
            self.entry3.insert(END, col4)
            self.entry4.insert(END, col5)
            self.entry5.insert(END, col6)
            self.entry6.insert(END, col7)
            self.entry7.set(col8)
            self.entry9.insert(END, col9)

        self.janPag2.mainloop()