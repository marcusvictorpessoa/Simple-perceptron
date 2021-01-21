
from random import uniform
import csv
import matplotlib.pyplot as plt

class Perceptron:

    def __init__(self, taxa_aprendizagem,dados_treino):

        self.taxa_aprendizagem = taxa_aprendizagem
        self.dados_treino = dados_treino
        self.dataframe = csv.reader(open(self.dados_treino, 'r'))


    def treino(self):

        self.w0 = uniform(-10,10)
        self.w1 = uniform(-10,10)
        self.teta = uniform(-10,10)

        teve_erro = True
        epoca = 0

        while teve_erro:

            print(f'epoca: {epoca+1}\n')
            cont = 1
            teve_erro = False

            for x in self.dataframe:

                entrada0 = float(x[0])
                entrada1 = float(x[1])

                x0w0 = entrada0*self.w0
                x1w1 = entrada1*self.w1
                limiar = (-1*self.teta)

                u = x0w0 + x1w1 + limiar
            
                #função de ativação
                if u >= 0:
                    saida = 1
                else:
                    saida =-1
            
                saida_esperada = int(x[2])
                erro = saida_esperada - saida
                print(f'index: {cont}, saida: {saida}, erro: {erro}')

                #se a saida nao for esperada ajuste os pesos
                if erro != 0:
                    teve_erro = True
                
                    self.w0 = self.w0 + (self.taxa_aprendizagem * erro * entrada0)
                    self.w1 = self.w1 + (self.taxa_aprendizagem * erro * entrada1)
                    self.teta = self.teta + (self.taxa_aprendizagem * erro * (-1))

                    print(f'pesos ajustados -> w0: {self.w0}, w1: {self.w1}, teta: {self.teta}')
                
                cont = cont + 1
            
            self.dataframe = csv.reader(open(self.dados_treino, 'r'))
            epoca = epoca + 1

        print(f'Pesos achados: w0: {self.w0}, w1: {self.w1}, teta: {self.teta}')

    #metodo em desenvolvimento
    def teste(self, dados_teste):
        self.dados_teste = dados_teste
        self.teste = csv.reader(open(self.dados_teste, 'r'))
        for x in self.teste:
            entrada0 = float(x[0])

    #metodo que gera grafico para visualização das duas classes com Matplotlib
    def grafico(self, dados):
        self.x1, self.y1, self.x2, self.y2 = [], [], [], []
        self.dados = csv.reader(open(dados, 'r'))
        for linha in self.dados:
            if linha[2] == '1':
                one = float(linha[0])
                two = float(linha[1])
                self.x1.append(one)
                self.y1.append(two)
            else:
                o = float(linha[0])
                t = float(linha[1])
                self.x2.append(o)
                self.y2.append(t)

        plt.scatter(self.x1, self.y1)
        plt.scatter(self.x2, self.y2)

        plt.show()


perceptron = Perceptron(0.35, 'dados-treinamento.csv')
perceptron.treino()
perceptron.grafico('dados-treinamento.csv')