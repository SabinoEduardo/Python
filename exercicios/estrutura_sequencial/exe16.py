#
#? Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#? Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#? que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#TODOS Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#* comprar apenas latas de 18 litros;
#* comprar apenas galões de 3,6 litros;
#* misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os 
#* valores para cima,   isto é, considere latas cheias.

#! O exercício 16 e 17 têm a mesma lógica. Portanto, será resolvido apenas o exercício 17.


from tkinter import *
from tkinter import ttk
import math

class Loja_Tintas():
    def __init__(self):

        self.parents = Tk()
        self.parents.title("Loja de Tintas")
        self.parents.geometry("600x530+30+30")
        self.parents.resizable(1, 1)
        self.frame_1 = ttk.Frame(self.parents)
        self.frame_2 = ttk.Frame(self.parents)
        self.frame_3 = ttk.Frame(self.parents)

        #* Variaveis
        self.area_parede = StringVar()
        self.qtde_litros = StringVar()
        self.qtde_latas = StringVar()
        self.option = IntVar()
        self.preco = StringVar()

        #* widgets
        self.text_option = ttk.Label(self.frame_3, text="Opção de compra:", 
                                        font="Arial 12 bold").grid(row=0, column=0)
        self.option_latas = ttk.Radiobutton(self.frame_3, text="Só latas", variable=self.option, 
                                                value=0).grid(row=1, column=0)
        self.option_latas = ttk.Radiobutton(self.frame_3, text="Só Galão", variable=self.option, 
                                                value=1).grid(row=2, column=0)
        self.option_latas = ttk.Radiobutton(self.frame_3, text="Latas e Galão", variable=self.option, 
                                            value=2).grid(row=3, column=0)

        self.text_areaValue = ttk.Label(self.frame_1, text="Área da parede(m²):", font="Arial 9 bold")
        self.entrada_areaValue = ttk.Entry(self.frame_1, textvariable=self.area_parede, justify="center")

        self.text_qtdeLitros = ttk.Label(self.frame_1, text="Quantidade de Litros:", font="Arial 9 bold")
        self.saida_qtdeLitros = ttk.Label(self.frame_1, textvariable=self.qtde_litros, background="#ccccb3", anchor="center",
                                            justify="center", width=17, font="Arial 10 bold")
        
        self.text_qtdeLatas = ttk.Label(self.frame_1, text="Quantidade de Latas:", font="Arial 9 bold")
        self.saida_qtdeLatas = ttk.Label(self.frame_1, textvariable=self.qtde_latas, background="#ccccb3",
                                            justify="center", width=17, anchor="center", font="Arial 10 bold")

        self.text_preco = ttk.Label(self.frame_1, text="Preço (R$):", font="Arial 9 bold")
        self.saida_preco = ttk.Label(self.frame_1, textvariable=self.preco, background="#ccccb3",
                                            justify="center", width=17, anchor="center", font="Arial 10 bold")

        self.mensagem = ttk.Label(self.frame_2, text="Nota:",  justify="center", anchor="center", font="Arial 13 bold", background="#cc8800", width=50)
        self.mensage_saida = ttk.Label(self.frame_2, text="1 litro de tinta cobre uma área de 6 metros quadrados." +
                                        "\nUma lata possui 18 litros e que custa R$80,00.\nUm galão possui 3,6 litros e custa R$25,00", justify="center", anchor="center", 
                                        font="Arial 11 normal", background="#cc8800", width=50)

        self.btn1 = Button(self.parents, text="Quantidade de Litros", background="#000000", foreground="#f2f2f2", width=25, 
                                    font="Arial 11 bold", command=self.calcular_litros)

        self.btn2 = Button(self.parents, text="Quantidade de Latas/Galão e\nPreço", background="#000000", foreground="#f2f2f2", width=25, 
                                    font="Arial 11 bold", command=self.calcular_preco_latas_galao)

        self.mensagem_erro = ttk.Label(self.parents, text=" ", anchor="center", justify="center")

        #* Layout
        self.frame_1.grid(row=1, padx=60)
        self.frame_2.grid(row=3, column=0, padx=65, pady=15)
        self.frame_3.grid(row=4, column=0, pady=10)

        self.text_areaValue.grid(row=0, column=0, padx=10, pady= 10)
        self.entrada_areaValue.grid(row=0, column=1)

        self.text_qtdeLitros.grid()
        self.saida_qtdeLitros.grid(row=1, column=1, pady= 10)

        self.text_qtdeLatas.grid()
        self.saida_qtdeLatas.grid(row=2, column=1, pady= 10)

        self.text_preco.grid()
        self.saida_preco.grid(row=3, column=1, pady= 10)

        self.btn1.grid(row=2, column=0)
        self.btn2.grid(row=5, column=0)

        self.mensagem.grid(columnspan=1)
        self.mensage_saida.grid(columnspan=1, sticky="WE")

        self.mensagem_erro.grid(row=0, columnspan=1, sticky="EW", padx=10, pady=10)

        self.entrada_areaValue.focus()

        self.parents.mainloop()

    def calcular_litros(self):
        #* Função para calcular a quuantidade de litros de tita necessários
        #* para pintar a área declarada.
        try:
            self.litros_necessarios =float(self.area_parede.get())/6
            self.qtde_litros.set(math.ceil(self.litros_necessarios))
            self.mensagem_erro["text"] = " " 
        except:
            self.mensagem_erro["text"] = "ERRO!\nVerifique o valor da área da parede."
            self.mensagem_erro["foreground"] = "red"
            self.mensagem_erro["font"] = "Arial 12 bold"
    
    def calcular_preco_latas_galao(self):
        #* Função para calcular a quuantidade de latas/galão de tinta e preço total
        try:
            if self.option.get() == 0:
                self.qtde_latas.set(math.ceil(self.litros_necessarios/18))
                self.preco.set((math.ceil(self.litros_necessarios/18))*80)
            elif self.option.get() == 1:
                self.qtde_latas.set(math.ceil(self.litros_necessarios/3.6))
                self.preco.set((math.ceil(self.litros_necessarios/3.6))*25)
            else:
                valor_litros_total = self.litros_necessarios + 0.10*self.litros_necessarios
                n_latas = int(valor_litros_total//18)
                n_galao = math.ceil((valor_litros_total - 18*n_latas)/3.6)
                self.qtde_latas.set(f"{n_latas} lata(s) e {n_galao} galão")
                self.preco.set(n_latas*80 + n_galao*25)
        except:
            self.mensagem_erro["text"] = "ERRO!\nVerifique o valor da área da parede e a quantidade de litros."
            self.mensagem_erro["foreground"] = "red"
            self.mensagem_erro["font"] = "Arial 12 bold"


loja_de_tintas = Loja_Tintas()
