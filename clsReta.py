class Retangulo:
    def __init__(self,comprimento, largura):
        self.comprimento = float(comprimento)
        self.largura = float(largura)

    def metMuda(self, LadoA, LadoB):
        self.comprimento = LadoA
        self.largura = LadoB

    def calc_Size(self):
        area = self.largura * self.comprimento
        return area

    def calc_peri(self):
        perimetro = 2 * self.largura + 2 * self.comprimento
        return perimetro

    def calc_roda(self):
        if self.comprimento < self.largura:
            Maior = self.largura
        else: Maior = self.comprimento
        print(Maior)
        return Maior
