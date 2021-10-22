class Retangulo:
    def __init__(self,comprimento, largura):
        self.comprimento = float(comprimento)
        self.largura = float(largura)


    def calc_Size(self):
        area = self.largura * self.comprimento
        return area

    def calc_peri(self):
        perimetro = 2 * self.largura + 2 * self.comprimento
        return perimetro