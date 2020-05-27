from modulos import *


class Formulas:
    def totalbotao(self):
        def moedaTotal1(total1=0, moeda='R$'):
            return f'{moeda}{total1:>8.2f}'.replace('.', ',')
        quant1 = self.listaCol3a.get()
        quant1 = float(quant1)
        valor1 = self.listaCol4a.get()
        valor1 = float(valor1)
        total1 = quant1 * valor1
        total1 = float(total1)
        self.listaCol5a.delete(0, END)
        self.listaCol5a.insert(END, moedaTotal1(total1))

        self.entradatotal.delete(0, END)
        self.totalsimples = float(total1 )
        self.entradatotal.insert(END, self.moedaTotalizador(total1 ))
    def moedaTotalizador(self, totalizador=0, moeda='R$'):
        return f'{moeda}{totalizador:>8.2f}'.replace('.',',')
    def moedaTotal1(self, total1=0, moeda='R$'):
        return f'{moeda}{self.total1:>8.2f}'.replace('.',',')
    def busca_servico1(self):
        self.busca_servico()
        # Binding da listbox da Placa
        self.listaServ1.bind('<Button-1>', self.add_servico1bind)
    def add_servico1(self):
        codVazio = self.codServ1.get()
        if codVazio == '':
            self.capturaCod = self.listaCol2a.get()
            capcod = str(self.capturaCod).replace("("," ").replace("'"," ").replace("*"," ")
            capcod2 = capcod[0:7].strip()
            self.codServ1.insert(END, capcod2)
            self.listaCol2a.delete(0, END)
            self.listaCol4a.delete(0, END)

            self.conecta_Glac()

            cod_sp = self.codServ1.get()

            addserv2 = self.cursor
            addserv2.execute("""SELECT UPPER(servprod), ' - ', UPPER(tiposerv), ' - ' , UPPER(id_marcaprod), '##' 
                FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico2 = self.cursor.fetchall()
            for i in addservico2:
                i = str(i);
                i = i.replace('(', '');
                i = i.replace(')', '');
                i = i.replace("'", "");
                i = i.replace(',', '')
                self.listaCol2a.insert(END, i)

            self.listaCol3a.delete(0, END)
            self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico3 = self.cursor.fetchall()
            for i in addservico3:
                self.listaCol3a.insert(END, i)

            addserv4 = self.cursor
            addserv4.execute("""SELECT  valor  FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico4 = self.cursor.fetchall()
            for i in addservico4:
                self.listaCol4a.insert(END, i)

            quant1 = self.listaCol3a.get()
            quant1 = float(quant1)
            valor1 = self.listaCol4a.get()
            valor1 = float(valor1)
            self.total1 = quant1 * valor1
            self.total1 = float(self.total1)

            self.listaCol5a.delete(0, END)
            self.listaCol5a.insert(END, self.moedaTotal1(self.total1))

            self.desconecta_Glac()
            print(capcod[0:7])
        else:
            self.listaCol2a.delete(0, END)
            self.listaCol4a.delete(0, END)

            self.conecta_Glac()

            cod_sp = self.codServ1.get()

            addserv2 = self.cursor
            addserv2.execute("""SELECT UPPER(servprod), ' - ', UPPER(tiposerv), ' - ' , UPPER(id_marcaprod), '##' 
                FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico2 = self.cursor.fetchall()
            for i in addservico2:
                i = str(i);
                i = i.replace('(', '');
                i = i.replace(')', '');
                i = i.replace("'", "");
                i = i.replace(',', '')
                self.listaCol2a.insert(END, i)

            self.listaCol3a.delete(0, END)
            self.cursor.execute("""SELECT hor FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico3 = self.cursor.fetchall()
            for i in addservico3:
                self.listaCol3a.insert(END, i)

            addserv4 = self.cursor
            addserv4.execute("""SELECT  valor  FROM servprod WHERE cod_sp LIKE '%s'""" % cod_sp)
            addservico4 = self.cursor.fetchall()
            for i in addservico4:
                self.listaCol4a.insert(END, i)

            quant1 = self.listaCol3a.get()
            quant1 = float(quant1)
            valor1 = self.listaCol4a.get()
            valor1 = float(valor1)
            self.total1 = quant1 * valor1
            self.total1 = float(self.total1)

            self.listaCol5a.delete(0, END)
            self.listaCol5a.insert(END, self.moedaTotal1(self.total1))

            self.desconecta_Glac()
    def add_servico1bind(self, event):
        self.codServ1.delete(0, END)
        self.listaCol2a.delete(0, END)
        self.listaCol4a.delete(0, END)
        self.entradatotal.delete(0, END)

        self.listaServ1.selection()

        for n in self.listaServ1.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaServ1.item(n, 'values')
            self.codServ1.insert(END, col1)

        self.add_servico1()
        self.listaServP1.destroy()

    def busca_servico1F(self):
        self.busca_falha()
        # Binding da listbox da Placa
        self.listaServ1F.bind('<Button-1>', self.add_servico1bindF)
    def add_servico1F(self):
        self.listaCol2aF.delete(0, END)

        self.conecta_Glac()

        cod_sp = self.codServ1F.get()

        addserv2 = self.cursor
        addserv2.execute("""SELECT falha FROM codfalha WHERE cod_falha LIKE '%s'""" % cod_sp)
        addservico2 = self.cursor.fetchall()
        for i in addservico2:
            self.listaCol2aF.insert(END, i)



        self.desconecta_Glac()
    def add_servico1bindF(self, event):
        self.codServ1F.delete   (0, END)
        self.listaCol2aF.delete (0, END)


        self.listaServ1F.selection()

        for n in self.listaServ1F.selection():
            col1, col2, col3 = self.listaServ1F.item(n, 'values')
            self.codServ1F.insert(END, col1)
            self.listaCol2aF.insert(END, col2)

            self.listaServP1F.destroy()
class Validadores:
    def validate_entry1(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 10
    def validate_entry2(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 100
    def validate_entry4(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 10000
    def validate_entry8(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 100000000
    def validate_entry12(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 100000000000000
    def validate_entry8float(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return len(text) < 9
    def validate_entry6(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return 0 <= value <= 1000000
    def validate_entry4float(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return len(text) < 5
    def validate_entry9float(self, text):
        if text == "": return True
        try:
            value = float(text)
        except ValueError:  # oops, couldn't convert to int

            return False
        return len(text) < 10
class Functions():
    def moedaTotaliza(self, totalizador=0, moeda='R$'):
        return f'{moeda}{totalizador:>8.2f}'.replace('.',',')
    def images_base64(self):
        ########################
        #### Logo da Empresa Seu Logo Aqui
        self.CADFORNEC_BT = 'iVBORw0KGgoAAAANSUhEUgAAAE4AAABGCAYAAABi+aJwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAQiSURBVHhe7Zy9axRBFMDf7t3FfJ0IYsRoECsFLQMGSWuhbfAPEBvtLCwFsdfaSvwD/BPELkhaQVDsooQUKhLRaLzcrfPmduLc3M7ufO7cx/xgc3t7t7uzv3vvzdsUm9y4/zQDCfOf3+Rr08v+yrV8bZAhcVGWHF7igLgqadvXH+Vr/riQdGGnA7DXOgbdrEm3NbNDmG3twZWzS/Bu+xfd5pPzrx7na8MweSn9G9HmKOJk0eY7yu5dPAXP3udv0h6kyW+y0oEsy6BHFiQhLwt/ydYGicRZEo6E09++wo8TS3TdF7LIw6grFedb2krWhd3eLHTSBfq+BQfEXQo/F5twfO87LCX9hNg+PICZuTZk5LMOWiQcJsRkF2C13YO3+wnd5osigXRkIaSda7XhCyxAI21CAzK6HCSLsENG9PDySfgzk8KnFtDl9d1VuLo8T6KQhFyjvyQwA83GHHzcb8PN5b54X6AL0QeNOF6cb2HjDou+ZGNjox/7hFDSGlsf8jV1umuX8rV6YeKCzKooil9McHEMG2oTJ17kkztn6KsrxOP7xnuq8heCstbX1/N3AJubm/T1wfNd+uoaH+nsvcbxwrZe3MrXikGBvuQxXEn0WuPEKKsCo9B16oq4TmGn4nBwrgfoEpfjcyZulIWJuBirE3G2A6mjxonYjtlaXNUAUAibPUcNG3lW4lRPzOSJAtm2uqONx1SecTtSdUKVWTKkMBHVdsWqj1ORxje6PKEjrAwVecZ9nE1dQOro2UzRuTYtcbbSJgmtVFUVV5WqqoRK6bKU1a5xOtEmE4fSZEKLCFkPZfK83qtOA1GcIUqpqjspjHuNYxSlq1aNcykOUaldrGUJKc9KnEkL4kocHmPt9st8y3+YVB1MfoAycWNX45hQ3cVEdlnQxMnBkCjOkCjOkCjOkFrE4SzKL6H7MxfU0o6YyBqFdgQRW5KxvldFCSY/BL/YUsudg+uIQ8Rz6KIypolqgEeFKM6QKE5CUZryKImrOsg0EiPOEGVx0xR1Kteq1I4wVNuSOtoRBL9jimw8VdK0/gPMoyLPlTgfmPRuPMZ93CSnrM61aUccoyry+IjRjbYixAhUPabqfqrSjFOVRyZPJc10ZOLxxNsrlfRX3U8n0pyIQ4rkFQ1YpKzo85Qdq0xe2X78uXVLj7N71XGueTZjt444hhh5+IuXESpVWbSZSnOWqjwqrYop4g+hKp7tx3/fJtK8iGP4FGiDi7LirMYVMYp1z/WYvN3k40BHQaCvcXgTxwghkJ3T53m9i2P4vhjfxxepTRwPf5GmF2u7vy0DsyriamadVI5mVdlDlyLDMGnIUKrih/wXIsUEqXGTQNBHBI0DsuxTegzaNAosK1cDD6ViyORF+kifH4cfxJl2EOaE9xInB0Ok4mLklTkA+AdJToBApvpBEwAAAABJRU5ErkJggg=='

        self.CADAUT_BT = 'iVBORw0KGgoAAAANSUhEUgAAAE4AAABGCAYAAABi+aJwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAP0SURBVHhe7ZxPa9RAFMBfst12tV3xYj1IEU968OihildBb2LbD6DgwZvfQPwAHjyJBesHUPwAll4UbK+CoNcq4kWRirbW/RMzs5kym81k5897k2Q3P0gzydLMe7+8ySTdkuDG/UcRKDj+5V3Sml72l64krWFGxNWy1MgSh8SNk7Z77UHSouNc0IOvHYC95hz0ohm+bybqQqu5BxfPLMKH3T98HyVnNx8mrVGEvJD/rDHmqOJU1UZdZffOn4InH5ONsA9hcBA3OhBFEfTjhRHEq/l/8d5GXImtuBxjTv/4Dr9OLvI2FarKY1WXK45a2lLUg2/9FnTCeb7dhMPYXQi/F2bgxN5PWAwGA2K3ewizx9oQxZ91mMWYbhCb7AFcavfh/X7A91GRJZCLK0JaFZEFjogrQlhj51PS0qO3fCFp+UfIC1ZWVga1H+NLmqmocfgUKcR5mVWZKHnBhvr4WZCK85mIjI9+ScQVJSwNZRyo4soiLA1FXGjiyigsDaZAZ3EUZ5MajHidxFVNmIxr7NbiqixN4JKDlbhJkCawzcVY3CRJE9jkZPTI5Spt5/la0sJn+faLpGWPzqOb8SNXmaVhYZKjlrgqSMPqQzdXraHqIk5OCGM4ZYHdR96Q1R6qZZfGkI+NUXk6OVvdjuiANXR0oTwxWeSKs622tDTfSfmoOrKKE/iUhj1k81BODrrVNi7AMlabSUzpicLLn859S2P46pO84spIKSqOBVFEZdmCFWumONPZtApVZ3uCVS7IZ9WygH1yp0YcA1Oes7isYMSwwLqemOCrb/SKEwG/fnydr+VEKJNJH397Y420P5Khyqqw3V7g6zdPbyZ7B2AnIwtj/b17tsqXIBhsU8kju8YFLPKY2dkmT4At2xurfB82b9dv8eMzwjDgy8HBX+h2e3wfBd4mB/bPlZfvvEy2cGk0RtNotebg6t1XyRY+6E8OOkMj/TsujOtv/vM6bG1tJlvmlwrVk8PUPXJhifM2VCeNWpwlSnF5X1jIUE33FLgOU5m64izJFadbddNIXXEKxhUNyhfSurckVNdD7P7zpKHejugERDmJFNG/ljjXax2lNAFWH7q5aldcFSYKV3kmORoN1bwDq4L2UW0yWf3pxGBaGFqTQxrTL3PKjok0p8mhCsNWF9tcrGfVSZDnkoO1OEaV5bnG7iSOUUV5GDE7i2OwQKogEDNOFHGCMgvEjgtVnKAsAkUcFLEMiRP3KFgUJdBHv6HqpUuYiEQok/HRh1xYhb93xPYphFKQilKJqxIj4lijlpeN6rp/JI6RJY8xjQLzJsqhl1IJVPJqBijfH8c+8DHTVgnhRPZCcgM8DSjF1ZWX5wDgPyk0+/P2DGPYAAAAAElFTkSuQmCC'

        self.CADPROD_BT = 'iVBORw0KGgoAAAANSUhEUgAAAE4AAABGCAYAAABi+aJwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAANoSURBVHhe7Zy7bhQxFIY3oUO8AkpLQ4kU0VNQr9LQUdHyBoiOhgeggp5HoEeRUtJQISGegIYOgc7Kjrwz43Pzb3uy40/ayEkkX779fTyzWs3Z89fv/+0y3P/1NbS2y5+HT0PrmJm4IStPKvFInCTt57M3oXXaXHx5G1pzorzzw8+BmdvE5dK2lZQtkUsepY5N3JalEbT+JQcUsoO4pbRtXVrKksBZ4nKWB8dhOtvv97enai9h966/h5aOv5ePQqs9se51EceJuv54FVo6Ll9+biqyuTikLI7aIpuIayVriVoCq4rrKWyJJx++hVY5URz8ziEnjYT1kEbcvHp8eCGBJY4T5oG2moSn79L0wbYqaltqREloxyupfxBxCGkIYVO0Y3vSV1zjSqWRsBrSCG3fJXXPJY6TJlFT2BTNWF55ZnGSNC5trYRNkcb1BAF+OZKjl7QIenzT4VBS10omjkqx1I/mpDUfDt66RhOqJc2KNA/LGptt1bVjfYNU4rwHQknSIog+UlCpG4lzIorz1jYElGRpCyFrYESz5pNInEYwmtWK84hoKW/UuAzSdmXF9axvaweSuNwR37ruaEDNib3lsiQuNyH0dVgplnku3YKpPshEiItYBXqTwY3D9WkVBzscaGCrnLXgmXezU9WbIBTo8WFbNcW6JWojScvNyV3jCI8870RTvAlJ+9b0wc2lSY1LkcTQguKrBtq+rdJSmtW4HGiBWmHSmyvRZatq0CzMM45WWC5x6hpHIK/neqKR9vvHp92DF+/Cb3PgNY6ErVUaYmtOUYmTCqVFWI1F5PCMxaUtpThxVmmRuCjrwiRK+qVtqkVV4yLTWueVxmHd7kjx0s4iTIdDSpSnWSByUbXRSCOKxLWQZk1exDuuVZy5xmkGuEtJI7TSUlyHA/eFvC1II8xbNSX9btldE0Z4pLlr3BSSV0NazRon3R1wwO4caNt6494DmqtXWkpx4lI8Hwi0BPEGwxKXQhNbY/pqzAsqLrIWgTXnUUVcpJfAFuOy4lA1Ky6k5mLQY0hrZ8XRJNAFP11gySJR/eSQ+oSeqltg8VSNfxzInOceujSYkwZrVuPonyN5MlUvR04Z9tlK47DI133VY9C2KJArV3QujAfvGck+P47+MU7aY6KT1Ms4HJxkxY3kcQ52u//ociLxXz5AGwAAAABJRU5ErkJggg=='

        self.CADSERV_BT = 'iVBORw0KGgoAAAANSUhEUgAAAE4AAABGCAYAAABi+aJwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAPUSURBVHhe7Zy/ixNBFMcnlxxe9P4FETsbS+Gws7AQbCTY2FkJVlfbiJ2NrWClva2dhY3IgaWNlSIiqdMY0YToy82cs7PzZt7MvJn9kf1Ajtls9sd89vt2JjnY0a3jZxuBcP77B9naXX5evC5bVWriBlk4usSKOJ+0bzcfy1Y+Lo/W4scfIRb758R6M9m+N9msxMH+QojVhe1ybi69fSJbdZS8ve3fFvF1Mxa/J2Mx/SfrUPzavg5Gq2LSqJwlDktbiZS1FSx5kDpn4nZZGgD9tzmAkG0TZ0tbKWnjk8+yRWN9dEW2yqMnsCYut7BQUT5Ki1TyRrPZ7GxUzSWNWxZGCYlKXNZRFYSVkgao45U4JnviSok6eXlXtqoc3X8tW6dwpzBL4kqmCwOE6q9c58SSuDYIA7AUApBEjvSxJa4t0gCQY5aqAqR+fHBVLqWTJK6kNFeaXJgiueRFi2tCGlWeKSuHvChxbSpPKmYZp8oLFldampmy2JJV6PJS+hIkri1JA3kpApU82Edsn8jimpBmk2PerziI6Vv04NAkemJspKSRCmkCnCNtXKXmw5ZQfTt9PWWCXORLPkaJRIAQnzSTkIB4xXGnjUOa2odNDCYM4Lxg3lLlFGc7cayTJinbAtTtfeVKKtWc0lzJsGH7LDVBIdKpfS5yj7NJiwGT5xIYIi2E7OK4pCma3l6RVRy3NAXsh2tfNijlig4O2MaussCYz+fizqP3cokP/VwwkbEXDxskis3jlstlFmlNQxYHVy40bXB1bzx8I5f6BalUKSXRBL0u1b4yiIskWFzofa6vsCQOZOqvXQAVR/ltChPVdYGUvkcnzhQDo5U5YnVZng/nz0pqSuIT0IQwOKZ+HGyaYbvAPlyJI01H1A5cB7Oto5xcW6GUKUAuVZDRZSHcRP8CjJXJu+e3xXQ6lUv/ySE9R6n6Ekf+5oDtSD8BODn1MqXB53JIywG1TAFSqVLk2eiKMCBEGhA9HVHYEmV7r80svrySLTpkcb4romR1SZji8N5T2aITlLjQOHeB2D4Fl2qf5KX0Jeoe1wd5qX2IHhy6LI/j3L0TYB+Uf6XlwpzcUrj24pNsxcH203mXkpcqTSdZHADy2iwQhHFKA5JL1aTJ0jWBiW3MHM1Ftv9ytSV9cA7c0nTYxSmUwNISSx0zmzidnBL1fefYP0YRcTqpHYX7Vsr2XLAPDn3HOjioNwf87GEPXRqoowerdo+DlUPy/BQfHPqC89lKw2CB3/dJj0HbRYGu2xWMCxVxACZv4BT0+XGwYhhpqygnupdhcIgEFTckz+VAiL/FbRfdMawwqgAAAABJRU5ErkJggg=='

        self.CADCLI_BT = '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'

        self.LOGORF = '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'

        self.SEULOGO = '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'
        ################################

        self.BTIMPRIME2 = 'iVBORw0KGgoAAAANSUhEUgAAAEUAAAAsCAYAAAAzdnW7AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAJSSURBVGhD7Zm7SwNBEMb3El//iqXWki6WahlEULBJoYL4xCYoKPGBgja2ioqlsdTOXu1sFBtREU1SWPlIzttz7txbZmNyt5e7S/YHQ4ZLsbNfZr/ZI1pPJqcThYMYfCoYKnbK6kQvZI3F3PYZZDioKKczjSkGT986Lo5DFFYMXW8eq+nfOIfsF9tTVsebozswctNJyH5RRougREFQoiAoURDs6ZM1jLazXSeapplfeJk+A+ktyPzlZHcSMu+wEyjSneKX+NI7hS1U5i/JI3udhukUv1CiIChREJQoCH9GO5YknR3GAwkjOYqwRutJlP9GYr2mD4+bdaVMH7/uCDKgtXmpr2ZRsAVX0gkzgsJan6/BrTCejDZoMTBk1FSzp1jqYwsv7F5AVl9oLezaVm30WbX+4sloK4kSNtyKYh8fLaaR+5ciuXl4JbdPeXL3XEAjajwW3tF98MGiLm8IShQE21PoH19txQL5+CqR1rhYq+nFPfMzTEZLEdWzszxKPj6/4YmYqcNLyFSnoDhEKZfxidNs+NIpFwcLZoSBkosfGhWlZNxRRFEtiaEVyIIH2wcfLMpTEBzTpyWfJ1+lMokZFzkRc0v7kImpx9GpthM3F0fMPf3H7NEVZD6KEpbj41kU7e3NnECVRInDuxGGdYcJolM2MsOQOaF7qVWUhvcUN9cMZbQI9vGhrA12Szk+QSA6PhR+5GIIj4/1BRVGFFEE2wcbrCAUR6ewZFNdkDmp9LIYVkRGO398DZkToSg89GhFFdoNIgEwqhalmVDThyOb6iI/07GWSu7pmdsAAAAASUVORK5CYII='

        self.BTLOGORF = ''

        self.LBNORC = 'iVBORw0KGgoAAAANSUhEUgAAADwAAAAuCAYAAAB04nriAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAF5SURBVGhD7Zq9boJgFIZfewVcAyVp4tiBO0AHJ4burG6uvYKubq7sHZwYKnfA4EhiQrkG7qA9wAcV6AAh/TnH8yTH7wcTffg+XjG6APBB9acURWF6P8+CXmyWsGVZv/qG53Jn2ptBhaWjwtJRYemosHRUWDoqLB0V/rfEu+qr6OqQ1+P8gBWNLWuHuJ6hp5Tj6/o61sBuhZPjG4xyjxhRaLotIaKeMb8tnVzwbrod8gxp2bovOBcFitegmk6z7ulheA0PV20KLEMrnGHMUpiMB2E0FnbCruvSY4qsfyHbDpZlmzzjsUzopzrBlo5dtQ38Vtj3ESDBMbqYiQYPmzqnrgiw8UzXwHBLO3igRU7CkLS7eHtK5zKh29rTaejCUPgea7/c1j3aG5FutTcqBpahZa99fKM8CpbCZIzBIttbnDrbua7TlntoVdhwqkieDlNhCqhhJI+CrTAZ04fOdPTXQ+mosHRUWDoqLB0Vlo4KS0eFpXNjfy4FPgF1Zm9BmKrCzwAAAABJRU5ErkJggg=='

        self.BTCLIENT = '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'

        self.BTTECNICO = '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'

        self.BTLUPA = 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAFPSURBVEhLvZUhTwNBEEb3TtTVonHFkwaNQyCKQSGxJSkYEjS6gf6Opoha0qS2IVgIpkldZSUIyCwze3NzM3t7R8IT7ew2fd/O7nWbfWx23y7CcLzCqspRd+kuLm9wpGMGxMSSWFAloIlYMhn1sSooBVjyg/0MqzJv62rzMiQEaHJNPB4eY+XcaLKoDfEBUm6tmOQgBvhYBlFI7l8ZqXKA19b38iaHyoUcCuch5C11cHfWwSodK5QIASCfvn7hKB1+6ABfJHQRAlLkUkbwLqSncsgaXGzVFrUBXHJ4euXfYY7m684gO7l+9g/w9v3JT3Be5o9YFfIU9noDrCIdtJVLQgBP/Yuce+DXXOqAfwg0lT/cnmNVkGtXLNBmW+5nn1hF7iLooo1cdk9Er2vtyZJoYr4roQNtq6xVEXVy4H//MjlNgjQxYQYQsaCY+BfnfgDiMKCq6QYtEwAAAABJRU5ErkJggg=='

        self.ADD = 'iVBORw0KGgoAAAANSUhEUgAAACYAAAAQCAYAAAB6Hg0eAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAJJSURBVEhLxZZfSFNRHMe/x9S2bKz1TxqLqD2ZYH+0f+JDb0GFhEGCEWRB9GCBT9FD9NxLvRREDzkIgyxEQUfT6ilWLWemra3NNkdr4ixbs7a13e107h+0tXP78+DuB778zu+c7zl877lwuSQej9O+0Qjsr6OIxlPQkmqjDofqzGhp2Ahy+9EEveX9Arp7OyoMVYpFG7LfkiAvXuFs7WqQo1cdNNLUiPq1Ohw3CoqltFAKEFa7E+Vwz6awyfkcpOlyP0XrYVxZn0GNTjaWGsqSEULg/QFcmKkE7g2gTFkDCy0Z1OVA50o9DtyYLFobPqdH55B6/zfxWAjGHMpAhaAfb1l56Xsv90vMQjBSRqTrVNPUw17g1Gns8gQwxfqlZvHGGFlBUJXfm0dzx3k04z7sfgFCLofA9f1YY1iB1i4gz+lFz7+IR0Ew8W3yNQy7rRbWzVtg3eqCf1KeD75z4UTPPO6eFDcX98Xn8MWjIFgskeRr3IMJdKHNZECbDbjTNyDNxzNAKqlei85R0ce5eUQ+J5QUMgXB8iw+T+HH/RhTPBK+AMLimjimIYR8YuX0/6lfKQiWy1OuQoER1F1ywh2cZupGy6gfITZvsTbgQXsHHGyvePDvPe+sP0kQcux55ICLH9jqDGhsVposNcsrlkk1bTThYox9YHsGQY5dG6Lhxr2oX6fHvu/TkkErnlVtgPtTGpanThDbkzf0pmcOdM8OZMrl5FpRmRVAXGM4U2OC9NvTO/IBg+NRzHxNKxZtMK/S4+A2M47stOAnOz0vNHr8npEAAAAASUVORK5CYII='

        self.ORCAMENTOLB = 'iVBORw0KGgoAAAANSUhEUgAAAHMAAAAZCAYAAAACLBHaAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAQbSURBVGhD7Zp/aFNXFMe/kQpOrHWsFSakselWKBgonWVMaG2roqbIZJhpnUqZTEH3VyMIs7ao+Uexf8mEVaxi/bHh/qh/NFNqTW1hQYqh0MF+aBOSFv2j+6PtBP1Dmp1732nyniZNfMkTn7wPpO/cc8+9ee+ce8+96bu26enpeG9oEpH7N2FhThy1O/DVWjts3XfH4tHhX3Hb7cW3K15wtYVZ6J75AFv6zqJsvQe2jo6O+O2mI/iseAm+KXrJJhbvMvG5OGw2m5SvzRbg4dRzbPF3KsFctfsw1nxUiJlHT6WBhXkoqvgYf/z7H55c/xGLWIc4Xy3MSyKYiFvhNDuJYNoWKTnYwrwkZ6aF6dEZzEGc+8IJd+KzA70TXPXeEUXvASdaf4lyeZ4sfDBxCa2ZbPKIvmAG+/EbiwohDP3+6sO+QwSP6XdksAtdY9WoW+dgBZONDyYf4y8WFUKYmGTRAHJIs804EQzDH+zGVta8j4wM3QC2f4/tdlZoWNgHT2N/01+tTSRm3KAv4KvEvrKQpQwULZaXErK3YymWkbykcCni/p1oOlWJ8+NuBMp34dHxB+hpieAkycl/Fu6j+k7UIoyrns9xOsTqah/6bh5E6aAXrv2QNmgrwaEbir3jspv7Fm0HtH1q2v6Jo/f8cFwQbWtI9iLcSgEhur7eiQ9FuTHV/aQg+hN+6AU8F7eRb1g3TxofqH1od62RV8VmG86MT8lyPpnlq8CADdAVHCr3w3m8BqN9/YgN+slxwqlTGLvnQxXVBwbJLNqPOyHhSNaHbmEoMWhFHyUIkKPn5WOPK5Nt1X1eJBtN2xGcbqS2n4jvGkE4sgHtwkba+7EnkuZ+UhAL3MIoDZSWela8KfWdON8s7t+Nq29hFTIgmMpIr+OSBsdB9FDw2oVzpKyeEcLxLMo+yG6jkBXH93xXIWsyo9i3N3BRNwO4fGoEVU2bUMoaPdT6piigYoAZH1ADgqlQ2uLHmEh9XH4dkSpL4BKfxjaMsjZ7lBno2n+Fy3mGZ//mBicr9PO2AmpYMDMinaVKs6zOHk6Vov04pc9XNpu5MnyXBkmzN6d+Y7TOu8q9GCa51vczPDQA7wTCSqUB5BBMZS1zaTY3mVBm48k0a5QuaJOyN99rEvXZRXsmz8YNrEhHCh/I+1GesXR1JSm0Np+uzn2mp0NfMOvdNMrULJCOpC2nRPlA+9Ag1kyp5wd90zSr7lO0rf4SdQvNoIQ9BR0VcmOUaDt/Pyqy2vhk44My8V1qauAsY9EAkq/AiguxfPoZqw1AjNjGf3Ag3c8AC13MrliW4hXYnJFvTSi9yllAM7FtgHUW+SaZZvnNtTHQbz25UaGPL9M6ZKGXRDCtF2DmxzoDZHKuzajOAFmn88yN5nSedW7W/CjnZu34HzHHwHvwVqgGAAAAAElFTkSuQmCC'
    def conecta_Glac(self):
        self.conn = sqlite3.connect("glac.db")
        self.cursor = self.conn.cursor()
    def desconecta_Glac(self):
        self.conn.close()
    def montaTabelas(self):
        ### Cria tabela servprod
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS servprod (
                cod_sp INTEGER PRIMARY KEY,
                servprod CHAR(40) NOT NULL,
    			tiposerv CHAR(20),
    			sistemaserv CHAR(20),
    			id_marcaprod INTEGER,
    			id_fornec INTEGER,
                hor INTEGER(2,2),
                custo MONEY NOT NULL,
                valor MONEY NOT NULL,
    			sp CHAR(2) NOT NULL,
                descricao VARCHAR(200) NOT NULL

            );
        """)
        ### Automoveis
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS automoveis (
                cod_aut INTEGER PRIMARY KEY,
                automovel CHAR(40) NOT NULL,
                ano INTEGER NOT NULL,
    			marca CHAR NOT NULL


            );
        """)
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fornecedores (
                cod_forn INTEGER PRIMARY KEY,
                fornecedor CHAR(20) NOT NULL,
    			fone SMALLINT NOT NULL,
    			cnpj SMALLINT NOT NULL,
                cep SMALLINT NOT NULL,
    			endereco CHAR(20) NOT NULL,
                municipio CHAR(15) NOT NULL,
                descricao VARCHAR(200) NOT NULL

            );
        """)
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS marcaprod (
                cod_marca INTEGER PRIMARY KEY,
                marca CHAR(20) NOT NULL,
    			descricao VARCHAR(200) NOT NULL

            );
        """)
        ###
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS orcamento1 (
    			id_orc1 INTEGER PRIMARY KEY,
    			cliente_orc NUMERIC(8) NOT NULL,
    			placa_orc VARCHAR(12) NOT NULL,
    			descp1 VARCHAR(120) NOT NULL,
    			descp2 VARCHAR(120) NOT NULL,
    			descp3 VARCHAR(120) NOT NULL,
    			dia NUMERIC(4) NOT NULL,
    			mes NUMERIC(4) NOT NULL,
    			ano NUMERIC(4) NOT NULL,
    			totalizador NUMERIC(8) NOT NULL
    			);
    	""")
        ###
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS orcamento2 (
    			cod_orc2 INTEGER PRIMARY KEY,
    			id_orc2 NUMERIC(10) NOT NULL,
    			cod_item NUMERIC(8) NOT NULL,
    			desc_item VARCHAR(120) NOT NULL,
    			valor NUMERIC(8) NOT NULL,
    			quant NUMERIC(8) NOT NULL,
    			total NUMERIC(8) NOT NULL
    			);
    	""")
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS empresa (
                cod_emp INTEGER PRIMARY KEY,
                nome_emp CHAR(40) NOT NULL,
                endereco_emp CHAR(40) NOT NULL,
                bairro_emp CHAR(20) NOT NULL,
                municipio_emp CHAR(20) NOT NULL,
                uf_emp CHAR(2) NOT NULL,
                fone_emp CHAR(12) NOT NULL,
                cep_emp CHAR(12) NOT NULL,
                cpf_emp CHAR(12) NOT NULL,
                rg_emp CHAR(10) NOT NULL,
                obs_emp CHAR(200) NOT NULL
            );
        """)
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS frota (
                id INTEGER PRIMARY KEY,
    			veiculo CHAR NOT NULL,
    			anoveic CHAR NOT NULL,
                placa CHAR NOT NULL,
    			renavan CHAR NOT NULL,
    			cliente CHAR NOT NULL,
    			combust CHAR NOT NULL,
    			motor CHAR NOT NULL,
    			cor CHAR NOT NULL


            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens_orc (
                cod_item INTEGER PRIMARY KEY,
                quant INTEGER,
    			valor INTEGER,
                item INTEGER

            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod_cli INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
    			nascdia NUMERIC(2) NOT NULL,
    			nascmes NUMERIC(2) NOT NULL,
    			endereco CHAR(40) NOT NULL,
    			complemento CHAR(40) NOT NULL,
    			bairro CHAR(20) NOT NULL,
                municipio CHAR(20) NOT NULL,
    			cep NUMERIC(12) NOT NULL,
                uf CHAR(2) NOT NULL,
    			numcasa CHAR(20) NOT NULL,
                fone1ddd NUMERIC(2) NOT NULL,
    			fone1 NUMERIC(10) NOT NULL,
    			fone2ddd NUMERIC(2) NOT NULL,
    			fone2 NUMERIC(10) NOT NULL,
                cpf NUMERIC(12) NOT NULL,
                rg NUMERIC(10) NOT NULL,
    			email CHAR(40) NOT NULL,
                obs CHAR(200) NOT NULL,
    			nascano NUMERIC(4) NOT NULL

            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS codfalha (
                cod_falha CHAR(40) NOT NULL,
                falha CHAR(40) NOT NULL,
    			falha2 CHAR(20),
    			falha3 CHAR(20),
    			falha4 CHAR(20),
    			falha5 NUMERIC(20)

            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orcfalha (
                id_orcfalha NUMERIC(10),
                cod_orcfalha VARCHAR(40),
                orcfalha CHAR(40),
    			orcfalha2 CHAR(200),
    			orcfalha3 CHAR(200),
    			orcfalha4 CHAR(200),
    			orcfalha5 NUMERIC(10)

            );
        """)
        ####
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS formapag (
    	    	id INTEGER PRIMARY KEY,
    			ordem CHAR NOT NULL,
    			tipopag CHAR NOT NULL,
    	        valorpagar CHAR NOT NULL,
    			valordeduzir CHAR NOT NULL,
    			dia CHAR NOT NULL,
    			mes CHAR NOT NULL,
    			ano CHAR NOT NULL,
    			pago CHAR NOT NULL,
    			fpag10 CHAR NULL,
    			fpag11 CHAR NULL

    	        );
    	    """)
        ####
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS meiopag (
    	    	id INTEGER PRIMARY KEY,
    			meiopag CHAR NOT NULL,
    			meiopag2 CHAR NOT NULL,
    	        meiopag3 CHAR NOT NULL,
    			meiopag4 CHAR NOT NULL

    	        );
    	    """)
        self.conn.commit()
    def add_itens_orc(self):
        #self.add_servico1()
        id_orc = self.listaNumOrc.get()
        cod_item1 = self.codServ1.get()
        desc_item1 = self.listaCol2a.get()
        ###
        valor1 = self.listaCol4a.get()
        quant1 = self.listaCol3a.get()
        total1 = self.listaCol5a.get()

        if id_orc == '':
            msg = 'Para Inserir um item é necessário que um orçamento ou O.S esteja aberta!!! Clique em ' \
                  'gravar para abrir novo chamado ou buscar para editar um já existente. ;) '
            messagebox.showerror("GLAC ", msg)
            self.codServ1.delete(0, END)
            self.listaCol2a.delete(0, END)
            self.listaCol4a.delete(0, END)
            self.listaCol3a.delete(0, END)
            self.listaCol5a.delete(0, END)
        else:
            self.conecta_Glac()

            numeroItemOrc = self.cursor
            numeroItemOrc.execute("""SELECT MAX(ordem_item) FROM orcamento2 WHERE id_orc2 = '%s'""" % id_orc)
            buscaNumItem = self.cursor.fetchall()
            for i in buscaNumItem:
                i = str(i);
                i = i.replace('(', '');
                i = i.replace(')', '');
                i = i.replace("'", "");
                i = i.replace(',', '')
                print(i)
                if i == 'None':
                    i = int(1)
                    self.cursor.execute("""	INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, 
                        total, ordem_item) VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                                        (id_orc, cod_item1, desc_item1, valor1, quant1, total1, i))
                    self.conn.commit()
                else:
                    i = int(i)
                    tItem = int(i + 1)
                    self.cursor.execute("""	INSERT INTO orcamento2 ( id_orc2, cod_item, desc_item, valor, quant, 
                                            total, ordem_item) VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
                                (id_orc, cod_item1, desc_item1, valor1, quant1, total1, tItem))
                    self.conn.commit()

            ##################

            self.listaServProd.delete(*self.listaServProd.get_children())
            lista = self.cursor.execute("""SELECT ordem_item, desc_item, cod_item, valor, quant, total 
                FROM orcamento2 WHERE id_orc2 = '%s' """ % id_orc)
            rows = self.cursor.fetchall()
            for row in rows:
                self.listaServProd.insert("", END, values=row)
            self.desconecta_Glac()
            self.codServ1.delete(0, END)
            self.listaCol2a.delete(0, END)
            self.listaCol4a.delete(0, END)
            self.listaCol3a.delete(0, END)
            self.listaCol5a.delete(0, END)
            self.total_orc()
    def atualiza_listaServProd(self):
        id_orc = self.listaNumOrc.get()
        cod_item1 = self.codServ1.get()
        desc_item1 = self.listaCol2a.get()
        ###
        valor1 = self.listaCol4a.get()
        quant1 = self.listaCol3a.get()
        total1 = self.listaCol5a.get()
        self.conecta_Glac()
        self.listaServProd.delete(*self.listaServProd.get_children())
        lista = self.cursor.execute("""SELECT ordem_item, desc_item, cod_item, valor, quant, total 
                        FROM orcamento2 WHERE id_orc2 = '%s' """ % id_orc)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServProd.insert("", END, values=row)
        self.desconecta_Glac()
    def altera_itens_orc_quant(self):
        valor = self.valorItem.get()
        quant = self.quantItem.get()
        total = self.totalItem.get()
        valor = float(valor)
        quant = float(quant)
        self.totalItem.delete(0, END)
        soma = valor * quant
        self.totalItem.insert(END, self.moedaTotaliza(soma))
    def altera_itens_orc_quant2(self):
        valor = self.listaCol3a.get()
        quant = self.listaCol4a.get()
        total = self.listaCol5a.get()
        valor = float(valor)
        quant = float(quant)
        self.listaCol5a.delete(0, END)
        soma = valor * quant
        self.listaCol5a.insert(END, self.moedaTotaliza(soma))
    def altera_itens_orc_alterabt(self):
        valor = self.valorItem.get();  quant = self.quantItem.get();  total = self.totalItem.get()
        ordem = self.ordemItem.get();  descr = self.descrItem.get();  codigo = self.codigoItem.get()
        numorc = self.listaNumOrc.get(); ordem2 = self.ordemItem.get()

        self.conecta_Glac()
        updateValor = self.cursor
        updateValor.execute("""UPDATE orcamento2 SET ordem_item = ?, desc_item = ?, cod_item = ?,
            valor = ?, quant = ?, total = ? WHERE id_orc2 = ? AND ordem_item = ?""",
                            (ordem, descr, codigo, valor, quant, total, numorc, ordem2))
        self.conn.commit()

        self.altOrcW.destroy()
        self.desconecta_Glac()
        self.atualiza_listaServProd()
        self.total_orc()
    def altera_itens_orc_deletabt(self):
        ordem = self.ordemItem.get();
        numorc = self.listaNumOrc.get();

        self.conecta_Glac()
        self.cursor.execute("""DELETE FROM orcamento2 WHERE ordem_item = ? AND id_orc2 = ?""", (ordem, numorc,))

        self.conn.commit()

        self.altOrcW.destroy()
        self.desconecta_Glac()
        self.atualiza_listaServProd()
        self.total_orc()
    def altera_itens_orc_deletabt2(self, event):
        numorc = self.listaNumOrc.get();
        self.listaServProd.selection()
        for n in self.listaServProd.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServProd.item(n, 'values')
            self.conecta_Glac()
            self.cursor.execute("""DELETE FROM orcamento2 WHERE ordem_item = ? AND id_orc2 = ?""", (col1, numorc,))

            self.conn.commit()

            self.desconecta_Glac()
            self.atualiza_listaServProd()
            self.total_orc()

    def altera_itens_orc(self, *args):
        self.altOrcW = Tk()
        self.altOrcW.title('Edição de Item')
        self.altOrcW.configure(background=self.fundo_do_frame)
        self.altOrcW.geometry("900x100")
        self.altOrcW.resizable(False, False)


        self.ordemItemL = Label(self.altOrcW, text = 'Ordem',width=4).place(x=5, y=1)
        self.ordemItem = Entry(self.altOrcW, width = 4)
        self.ordemItem.place(x=5, y=30)

        self.descrItemL = Label(self.altOrcW, text = 'Descrição').place(x=50, y=1)
        self.descrItem = Entry(self.altOrcW, width = 80)
        self.descrItem.place(x=50, y=30)

        self.codigoItemL = Label(self.altOrcW, text='Código').place(x=550, y=1)
        self.codigoItem = Entry(self.altOrcW, width = 10)
        self.codigoItem.place(x=550, y=30)

        self.valorItemL = Label(self.altOrcW, text='R$ Valor').place(x=635, y=1)
        self.valorItem = Entry(self.altOrcW, width = 10)
        self.valorItem.place(x=635, y=30)

        self.quantItemL = Button(self.altOrcW, text='Quant', command = self.altera_itens_orc_quant).place(x=720, y=1)
        self.quantItem = Entry(self.altOrcW, width = 10)
        self.quantItem.place(x=720, y=30)

        self.totalItemL = Label(self.altOrcW, text='R$ Total').place(x=805, y=1)
        self.totalItem = Entry(self.altOrcW, width = 10)
        self.totalItem.place(x=805, y=30)

        self.altera_itenBt = Button(self.altOrcW, text = 'Alterar Registro', command = self.altera_itens_orc_alterabt)
        self.altera_itenBt.place(x= 700, y=60)

        self.deleta_itenBt = Button(self.altOrcW, text='Excluir Registro', command = self.altera_itens_orc_deletabt)
        self.deleta_itenBt.place(x=800, y=60)

        self.listaServProd.selection()
        for n in self.listaServProd.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServProd.item(n, 'values')
            self.ordemItem.insert(END, col1)
            self.descrItem.insert(END, col2)
            self.codigoItem.insert(END, col3)
            self.valorItem.insert(END, col4)
            self.quantItem.insert(END, col5)
            self.totalItem.insert(END, col6)
    def total_orc(self):
        self.entradatotal.delete(0, END)
        id_orc = self.listaNumOrc.get()
        totalizador = self.entradatotal.get()

        if id_orc == '':
            msg = 'Não é possivel calcular o Valor Total se nenhum Orçamento' \
                  ' ou Ordem de Serviço estiver selecionada. '
            messagebox.showerror("GLAC ", msg)
        else:
            self.conecta_Glac()

            numeroItemOrc = self.cursor
            numeroItemOrc.execute("""SELECT SUM(valor * quant) FROM orcamento2 
                WHERE id_orc2 = '%s'""" % id_orc)
            buscaNumItem = self.cursor.fetchall()
            for i in buscaNumItem:
                i = str(i);
                i = i.replace('(', '');
                i = i.replace(')', '');
                i = i.replace("'", "");
                i = i.replace(",", "h");
                i = i.replace("h", "");
                i = float(i)
                print(i)
                self.entradatotal.insert(END, self.moedaTotaliza(i))

            self.desconecta_Glac()

    def abre_orc(self):

        self.listaNumOrc.delete(0, END)
        id_orc1 = self.listaNumOrc.get()
        numeroorcamento = self.listaNumOrc.get()
        cliente_orc = self.entradaCod_cli.get()
        placa_orc = self.placa.get()
        dia = self.entradaDataorc.get()
        mes = self.entradaDataorc2.get()
        ano = self.entradaDataorc3.get()
        descp1 = self.area1.get()
        descp2 = self.area2.get()
        descp3 = self.area3.get()
        descp4 = self.area4.get()
        totalizador = self.entradatotal.get()
        km = self.entradaObs.get()
        tecnico = self.entradaTecnico.get()
        tipoOrc = self.Tipvar.get()
        comp1 = self.listInicio.get()
        comp2 = self.listFim.get()

        self.conecta_Glac()

        self.cursor.execute("""
    			INSERT INTO orcamento1 ( cliente_orc, placa_orc, descp1, descp2, descp3, descp4, dia, mes, ano, tecnico, totalizador, tipoOrc, km, comp1, comp2)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (cliente_orc, placa_orc, descp1, descp2, descp3, descp4, dia, mes, ano, tecnico, totalizador,
                        tipoOrc, km, comp1, comp2))
        self.conn.commit()

        numeroorc = self.cursor

        numeroorc.execute("""SELECT MAX(id_orc1) FROM orcamento1""")
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listaNumOrc.insert(END, i)

        # variaveis orcamento2
        id_orc2 = self.listaNumOrc.get()
        cod_item1 = self.codServ1.get()
        desc_item1 = self.listaCol2a.get()

        ###
        valor1 = self.listaCol4a.get()
        quant1 = self.listaCol3a.get()
        total1 = self.listaCol5a.get()

        ################
        # Vistoria variaveis
        codVist = self.listaNumOrc.get()
        tanque = self.are1.get()
        odometro = self.are2.get()
        radio = self.are3.get()
        calota = self.are4.get()
        triangulo = self.are5.get()
        macaco = self.are6.get()
        estepe = self.are7.get()
        obs1 = self.are8.get()
        obs2 = self.are9.get()

        self.cursor.execute("""
    			INSERT INTO vistoria ( cod, vist1, vist2, vist3, vist4, vist5, vist6, vist7, vist8, vist9)
    			VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (codVist, tanque, radio, odometro, calota, triangulo, macaco, estepe, obs1, obs2))
        self.conn.commit()



        self.desconecta_Glac()

        self.total_orc()

        msg = "Orçamento gravado com sucesso.\n "
        msg += ""
        messagebox.showinfo("GLAC - Orçamento", msg)
    def altera_orc(self):
        id_orc1 = self.listaNumOrc.get()
        cliente_orc = self.entradaCod_cli.get()
        placa_orc = self.placa.get()
        dia = self.entradaDataorc.get()
        mes = self.entradaDataorc2.get()
        ano = self.entradaDataorc3.get()
        descp1 = self.area1.get()
        descp2 = self.area2.get()
        descp3 = self.area3.get()
        descp4 = self.area4.get()
        totalizador = self.entradatotal.get()
        km = self.entradaObs.get()
        tecnico = self.entradaTecnico.get()
        tipoOrc = self.Tipvar.get()
        comp1 = self.listInicio.get()
        comp2 = self.listFim.get()

        self.conecta_Glac()

        self.cursor.execute("""
    			UPDATE orcamento1 SET id_orc1 = ?, cliente_orc = ?, placa_orc = ?, dia = ?,
    			mes = ?, ano = ?, descp1 = ?, descp2 = ?, descp3 = ?, descp4 = ?, totalizador = ?, km = ?,
    			tecnico = ?, tipoOrc = ? , comp1 = ?, comp2 = ? WHERE id_orc1 = ?""",
                       (id_orc1, cliente_orc, placa_orc, dia, mes, ano, descp1, descp2, descp3,
                        descp4, totalizador, km, tecnico, tipoOrc, comp1, comp2, id_orc1))
        self.conn.commit()


        ################
        # Vistoria variaveis
        cod = self.listaNumOrc.get()
        tanque = self.are1.get()
        odometro = self.are2.get()
        radio = self.are3.get()
        calota = self.are4.get()
        triangulo = self.are5.get()
        macaco = self.are6.get()
        estepe = self.are7.get()
        obs1 = self.are8.get()
        obs2 = self.are9.get()

        self.cursor.execute("""
    			UPDATE vistoria SET vist1 = ?, vist2 = ?, vist3 = ?, vist4 = ?, vist5 = ?,
    			vist6 = ? , vist7 = ?, vist8 = ?, vist9 = ? WHERE cod = ? """,
                       (tanque, radio, odometro, calota, triangulo, macaco, estepe, obs1, obs2, cod))
        self.conn.commit()

        self.desconecta_Glac()
        self.total_orc()

        msg = "Alterações realizadas com sucesso.\n "
        msg += ""
        messagebox.showinfo("GLAC - Orçamento", msg)
    def buscanomeorc(self):
        self.listaNomeO.insert(END, '%')
        self.listaServ.delete((*self.listaServ.get_children()))

        nomeO = self.listaNomeO.get()

        self.conecta_Glac()

        nom = self.cursor

        nom.execute(
            """SELECT id_orc1, nome ,dia , mes , ano, placa_orc, orcamento1.tipoOrc FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND nome LIKE '%s' ORDER BY id_orc1 DESC""" % nomeO)
        buscanomeO = self.cursor.fetchall()
        for row in buscanomeO:
            self.listaServ.insert("", END, values=row)

        self.listaNomeO.delete(0, END)

        self.desconecta_Glac()
    def buscaplacaorc(self):
        self.listaPlaca.insert(END, '%')
        self.listaServ.delete(*self.listaServ.get_children())

        placaO = self.listaPlaca.get()
        self.conecta_Glac()

        plac = self.cursor

        plac.execute(
            """SELECT id_orc1, nome, dia , mes , ano, placa_orc, orcamento1.tipoOrc FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND placa_orc LIKE '%s'""" % placaO)
        buscaplac = self.cursor.fetchall()
        for row in buscaplac:
            self.listaServ.insert("", END, values=row)

        self.listaPlaca.delete(0, END)

        self.desconecta_Glac()

    def carrega_orc(self, event):
        self.limpa_cliente()
        self.entradaDataorc.delete(0, END)
        self.entradaDataorc2.delete(0, END)
        self.entradaDataorc3.delete(0, END)
        self.entradatotal.delete(0, END)
        self.listaNumOrc.delete(0, END)
        self.entradaTecnico.delete(0, END)

        self.listaServ.selection()

        self.conecta_Glac()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.listaServ.item(n, 'values')
            self.listaNumOrc.insert(END, col1)

        id_orc = self.listaNumOrc.get()

        nomecur = self.cursor

        nomecur.execute("SELECT cliente_orc FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultanome = self.cursor.fetchall()
        for i in consultanome:
            self.entradaCod_cli.insert(END, i)

        self.desconecta_Glac()
        self.carrega_cliente()
        self.conecta_Glac()

        self.entradaCod_aut.delete(0, END)

        nomeplaca = self.cursor

        nomeplaca.execute("SELECT placa_orc FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultaplaca = self.cursor.fetchall()
        for i in consultaplaca:
            self.placa.insert(END, i)

        nomedescp1 = self.cursor

        nomedescp1.execute("SELECT descp1 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultap1 = self.cursor.fetchall()
        for i in consultap1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area1.insert(END, i)

        nomedescp2 = self.cursor

        nomedescp2.execute("SELECT descp2 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultap2 = self.cursor.fetchall()
        for i in consultap2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area2.insert(END, i)

        nomedescp3 = self.cursor

        nomedescp3.execute("SELECT descp3 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultap3 = self.cursor.fetchall()
        for i in consultap3:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area3.insert(END, i)

        nomedescp4 = self.cursor

        nomedescp4.execute("SELECT descp4 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultap4 = self.cursor.fetchall()
        for i in consultap4:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.area4.insert(END, i)

        self.entradaDataorc.delete(0, END)
        nomedia = self.cursor

        nomedia.execute("SELECT dia FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultadia = self.cursor.fetchall()
        for i in consultadia:
            self.entradaDataorc.insert(END, i)

        self.entradaDataorc2.delete(0, END)
        nomemes = self.cursor

        nomemes.execute("SELECT mes FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultames = self.cursor.fetchall()
        for i in consultames:
            self.entradaDataorc2.insert(END, i)

        self.entradaDataorc3.delete(0, END)
        nomeano = self.cursor

        nomeano.execute("SELECT ano FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultaano = self.cursor.fetchall()
        for i in consultaano:
            self.entradaDataorc3.insert(END, i)

        nometotal = self.cursor

        nometotal.execute("SELECT totalizador FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultatotal = self.cursor.fetchall()
        for i in consultatotal:
            self.entradatotal.insert(END, i)

        nomekm = self.cursor

        nomekm.execute("SELECT km FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultakm = self.cursor.fetchall()
        for i in consultakm:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaObs.insert(END, i)

        self.cursor.execute("SELECT comp1 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultacomp1 = self.cursor.fetchall()
        for i in consultacomp1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listInicio.insert(END, i)

        self.cursor.execute("SELECT comp2 FROM orcamento1 WHERE id_orc1 = '%s'" % id_orc)
        consultacomp2 = self.cursor.fetchall()
        for i in consultacomp2:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listFim.insert(END, i)
        ##################################################

        placa = self.placa.get()

        nomeaut = self.cursor

        nomeaut.execute(
            "SELECT UPPER(veiculo) FROM frota WHERE placa = '%s'" % placa)
        consultaautomovel = self.cursor.fetchall()
        for i in consultaautomovel:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listAut.insert(END, i)

        nomeano = self.cursor
        nomeano.execute("SELECT ano FROM frota WHERE placa = '%s'" % placa)
        consultaano = self.cursor.fetchall()
        for i in consultaano:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listAno.insert(END, i)

        nomemarca = self.cursor
        nomemarca.execute(
            "SELECT UPPER(montadora) FROM frota WHERE placa = '%s'" % placa)
        consultamarca = self.cursor.fetchall()
        for i in consultamarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listMarca.insert(END, i)

        nomecomb = self.cursor
        nomecomb.execute("SELECT UPPER(combust) FROM frota WHERE placa = '%s'" % placa)
        consultacomb = self.cursor.fetchall()
        for i in consultacomb:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCombustivel.insert(END, i)

        nomecor = self.cursor
        nomecor.execute("SELECT UPPER(cor) FROM frota WHERE placa = '%s'" % placa)
        consultacor = self.cursor.fetchall()
        for i in consultacor:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCor.insert(END, i)

        #############################################

        self.listaServProd.delete(*self.listaServProd.get_children())
        lista = self.cursor.execute("""SELECT ordem_item, desc_item, cod_item, valor, quant, total FROM orcamento2
                    WHERE id_orc2 = '%s' """ % id_orc)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServProd.insert("", END, values=row)

        ##################################


        ##################################

        tec = self.cursor

        tec.execute("SELECT tecnico FROM orcamento1 WHERE id_orc1 = '%s' " % id_orc)
        tecd = self.cursor.fetchall()
        for i in tecd:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.entradaTecnico.insert(END, i)

        orcos = self.cursor
        orcos.execute("Select tipoOrc From orcamento1 Where id_orc1 = '%s' " % id_orc)
        orcos1 = self.cursor.fetchall()
        for i in orcos1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.Tipvar.set(i)

        ################
        # Vistoria variaveis
        codVist = self.listaNumOrc.get()
        tanque = self.are1.get()
        odometro = self.are2.get()
        radio = self.are3.get()
        calota = self.are4.get()
        triangulo = self.are5.get()
        macaco = self.are6.get()
        estepe = self.are7.get()
        obs1 = self.are8.get()
        obs2 = self.are9.get()

        self.cursor.execute("SELECT vist1 FROM vistoria WHERE cod = '%s' " % codVist)
        codVisto = self.cursor.fetchall()
        for i in codVisto:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are1.insert(END, i)

        self.cursor.execute("SELECT vist2 FROM vistoria WHERE cod = '%s' " % codVist)
        codR = self.cursor.fetchall()
        for i in codR:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are3.insert(END, i)

        self.cursor.execute("SELECT vist3 FROM vistoria WHERE cod = '%s' " % codVist)
        codO = self.cursor.fetchall()
        for i in codO:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are2.insert(END, i)

        self.cursor.execute("SELECT vist4 FROM vistoria WHERE cod = '%s' " % codVist)
        codCalota = self.cursor.fetchall()
        for i in codCalota:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are4.insert(END, i)

        self.cursor.execute("SELECT vist5 FROM vistoria WHERE cod = '%s' " % codVist)
        codTri = self.cursor.fetchall()
        for i in codTri:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are5.insert(END, i)

        self.cursor.execute("SELECT vist6 FROM vistoria WHERE cod = '%s' " % codVist)
        cod6 = self.cursor.fetchall()
        for i in cod6:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are6.insert(END, i)

        self.cursor.execute("SELECT vist7 FROM vistoria WHERE cod = '%s' " % codVist)
        cod7 = self.cursor.fetchall()
        for i in cod7:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are7.insert(END, i)

        self.cursor.execute("SELECT vist8 FROM vistoria WHERE cod = '%s' " % codVist)
        cod8 = self.cursor.fetchall()
        for i in cod8:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are8.insert(END, i)

        self.cursor.execute("SELECT vist9 FROM vistoria WHERE cod = '%s' " % codVist)
        cod9 = self.cursor.fetchall()
        for i in cod9:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.are9.insert(END, i)

        # self.add_servico1()
        ########################################
        #########   carrega falhas
        ################################################

        ### lista1
        self.codServ1F.delete(0, END)
        self.listaCol2aF.delete(0, END)

        nomecodserv1F = self.cursor

        nomecodserv1F.execute("SELECT cod_orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 1" % id_orc)
        consultacodserv1 = self.cursor.fetchall()
        for i in consultacodserv1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.codServ1F.insert(END, i)

        nomedescitem1 = self.cursor

        nomedescitem1.execute("SELECT orcfalha FROM orcfalha WHERE id_orcfalha = '%s' and orcfalha5 = 1" % id_orc)
        consultadescitem1 = self.cursor.fetchall()
        for i in consultadescitem1:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.listaCol2aF.insert(END, i)



        self.listaOrc.destroy()
        self.desconecta_Glac()

        self.total_orc()

        def carrega_orc_a(event):
            carrega_orc()
    def OnDoubleClick(self, event):
        self.limpa_cliente()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5 = listaServ.item(n, 'values')
            self.entradan.insert(END, col1)

        self.carrega_orc()
    def backup(self):
        try:
            shutil.copyfile("c:\glacx\glac.db", "c:\glacbkp\copiaGlacX.db")
            msg = "Backup salvo em c:\glacbkp\ \n" \
                 "Copie e salve em local seguro. ;) "
            msg += ""
            messagebox.showinfo("GLACX", msg)
        except:
            msg = "Copia não realizada, crie a pasta c:\glacbkp \n" \
                  "antes de realizar o backup"
            messagebox.showinfo("GLACX", msg)

    def busca_serv(self):
        # self.listaServ1.delete(0, END)
        self.listaServ1.delete(*self.listaServ1.get_children())
        self.listaServicos1.insert(END, '%')

        self.conecta_Glac()

        servprod = self.listaServicos1.get()

        servico12 = self.cursor

        servico12.execute("""SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, sistemaserv, valor * hor
    	FROM servprod WHERE servprod LIKE '%s' """ % servprod)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)

        self.listaServicos1.delete(0, END)

        self.desconecta_Glac()

    def OnVsb_S1F(self, *args):
        self.listaServ1F.yview(*args)
    def busca_servF(self):
        # self.listaServ1.delete(0, END)
        self.listaServ1F.delete(*self.listaServ1F.get_children())
        self.listaServicos1F.insert(END, '%')

        self.conecta_Glac()

        servprodF = self.listaServicos1F.get()

        servico12F = self.cursor

        servico12F.execute("""SELECT cod_falha, falha, falha2 FROM codfalha WHERE falha LIKE '%s' """ % servprodF)
        buscaservico12F = self.cursor.fetchall()
        for i in buscaservico12F:
            self.listaServ1F.insert("", END, values=i)

        self.listaServicos1F.delete(0, END)
        self.desconecta_Glac()
    def PaginaRf(self):
        webbrowser.open("https://www.facebook.com/rfzorzi/")
    def add_movF(self):
        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()
        cod2 = self.codproduto2.get()
        prod2 = self.produto_aba2.get()
        dia = self.dia_aba2.get()
        mes = self.mes_aba2.get()
        ano = self.ano_aba2.get()
        lote = self.lote_aba2.get()
        diaV = self.diaV_aba2.get()
        mesV = self.mesV_aba2.get()
        anoV = self.anoV_aba2.get()
        quant = self.quant_aba2.get()
        custo = self.custo_aba2.get()
        fornecedor = self.entradaIdFornec.get()
        saida = self.saida_aba2.get()
        self.listaMov.delete(*self.listaMov.get_children())

        self.cursor.execute("""
    		INSERT INTO movim_prod ( cod_p, entrada, custo, dia, mes, ano,
    		lote, diaV, mesV, anoV, fornecedor, saida)
    		VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (cod2, quant, custo, dia, mes, ano, lote, diaV, mesV, anoV,
                        fornecedor, saida))
        conn.commit()

        msg = "Movimentação realizada.\n "
        msg += ""
        messagebox.showinfo("GLAC - Estoque", msg)

        lista1 = self.cursor.execute("""
    		SELECT  lote, entrada, saida, custo, dia , mes, ano, fornecedores.fornecedor, diaV, mesV, anoV 
    		    FROM movim_prod , fornecedores WHERE cod_p = '%s' and 
    		    movim_prod.fornecedor = fornecedores.cod_forn ORDER BY id ASC;        """ % cod2)
        for i in lista1:
            self.listaMov.insert("", END, values=i)

        self.quantest.delete(0, END)

        lista2 = self.cursor.execute("""select Sum(entrada) - Sum(saida) from movim_prod where cod_p = '%s'""" % cod2)
        consultalista2 = cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)
        conn.close()

    def buscaCli(self):
        self.conecta_Glac()
        self.EntryCliente2.insert(END, '%')
        nome = self.EntryCliente2.get()
        nomecod = self.cursor
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""SELECT cod_cli, nome FROM clientes WHERE nome LIKE '%s' """ % nome)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaServ.insert("", END, values=row)
        self.EntryCliente2.delete(0, END)
        self.desconecta_Glac()
    def limpa_cliente(self):
        self.entradaCod_cli.delete(0, END)
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
        self.entradaObs.delete(0, END)
        self.area1.delete(0, END)
        self.area2.delete(0, END)
        self.area3.delete(0, END)
        self.area4.delete(0, END)
        self.entradatotal.delete(0, END)
        self.listInicio.delete(0, END)
        self.listFim.delete(0, END)

        self.codServ1.delete(0, END)

        self.listaCol2a.delete(0, END)
        self.listaCol3a.delete(0, END)
        self.listaCol3a.insert(END, 1)
        self.listaCol4a.delete(0, END)
        self.listaCol4a.insert(END, 0)
        self.listaCol5a.delete(0, END)
        self.listaCol5a.insert(END, 0)

        self.listaNumOrc.delete(0, END)
        self.are1.delete(0, END)
        self.are2.delete(0, END)
        self.are3.delete(0, END)
        self.are4.delete(0, END)
        self.are5.delete(0, END)
        self.are6.delete(0, END)
        self.are7.delete(0, END)
        self.are8.delete(0, END)
        self.are9.delete(0, END)

        self.codServ1F.delete(0, END)

        self.listaCol2aF.delete(0, END)

        self.listaServProd.delete(*self.listaServProd.get_children())
    def carrega_cliente2C(self, event):
        self.limpa_clienteC()

        pos = int(self.listaServ2.curselection()[0])
        cod_cli = self.listaServ2.get(pos)

        self.cursor.execute("SELECT cod_cli FROM clientes WHERE cod_cli = '%s'" % cod_cli)
        consultacod = cursor.fetchall()
        for i in consultacod:
            self.entradaCod_clicC.insert(END, i)

        self.carrega_clienteC()
    def carrega_cliente2(self, event):
        self.limpa_cliente()
        #### Variaveis da função
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaCod_cli.insert(END, col1)

        self.carrega_cliente()
        self.listacliente.destroy()

        def carrega_cliente2_a(event):
            self.carrega_cliente2()

    def carrega_automovel(self, event):
        self.listAut.delete(0, END)
        self.listAno.delete(0, END)
        self.listMarca.delete(0, END)
        self.listCombustivel.delete(0, END)
        self.listCor.delete(0, END)
        self.listObs.delete(0, END)
        self.placa.delete(0, END)

        self.conecta_Glac()

        pos = int(self.entradaCod_aut.curselection()[0])
        placa = self.entradaCod_aut.get(pos)

        nomeplac = self.cursor
        nomeplac.execute("SELECT placa FROM frota WHERE placa = '%s'" % placa)
        consultaplac = self.cursor.fetchall()
        for i in consultaplac:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.placa.insert(END, i)

        nomeaut = self.cursor
        nomeaut.execute("SELECT UPPER(veiculo) FROM frota WHERE placa = '%s'" % placa)
        consultaautomovel = self.cursor.fetchall()
        for i in consultaautomovel:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listAut.insert(END, i)

        nomeano = self.cursor
        nomeano.execute("SELECT ano FROM frota WHERE placa = '%s'" % placa)
        consultaano = self.cursor.fetchall()
        for i in consultaano:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listAno.insert(END, i)

        nomemarca = self.cursor
        nomemarca.execute(
            "SELECT UPPER(montadora) FROM frota WHERE placa = '%s'" % placa)
        consultamarca = self.cursor.fetchall()
        for i in consultamarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listMarca.insert(END, i)

        nomecomb = self.cursor
        nomecomb.execute("SELECT UPPER(combust) FROM frota WHERE placa = '%s'" % placa)
        consultacomb = self.cursor.fetchall()
        for i in consultacomb:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCombustivel.insert(END, i)

        nomecor = self.cursor
        nomecor.execute("SELECT UPPER(cor) FROM frota WHERE placa = '%s'" % placa)
        consultacor = self.cursor.fetchall()
        for i in consultacor:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '')
            self.listCor.insert(END, i)

        self.desconecta_Glac()

        def carrega_automovel_a(event):
            carrega_automovel()
    def busca_serv_veic(self):

        # self.listaServ1.delete(0, END)
        self.listaServ1.delete(*self.listaServ1.get_children())
        self.listaServicos1.insert(END, '%')

        servprod = self.listaServicos1.get()

        self.conecta_Glac()

        servico12 = self.cursor

        servico12.execute("""SELECT cod_sp, servprod, tiposerv, hor, descricao, id_marcaprod, sistemaserv, valor * hor
    	FROM servprod WHERE id_marcaprod LIKE '%s' """ % servprod)
        buscaservico12 = self.cursor.fetchall()
        for i in buscaservico12:
            self.listaServ1.insert("", END, values=i)

        self.listaServicos1.delete(0, END)

        self.desconecta_Glac()

    def OnVsb(self, *args):
        self.listaServ.yview(*args)
    def OnVsb_S1(self, *args):
        self.listaServ1.yview(*args)
    def OnVsb_Orc(self, *args):
        self.listaServ.yview(*args)
    def OnVsb_Orc2(self, *args):
        self.listaServProd.yview(*args)