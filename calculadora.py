class Calculadora:
    def _init_(self):
        self.valor_1 = 0
        self.valor_2 = 0
        self.resultado =0

    def suma (self):
        self.resultado = self.valor_1 + self.valor_2
    
    def resta (self):
        self.resultado = self.valor_1 - self.valor_2
    
    def multiplicacion (self):
        self.resultado = self.valor_1 * self.valor_2
    
    def division (self):
        if(self.valor_2!=0):
            self.resultado = self.valor_1 / self.valor_2
        else:
            print("no se puede hacer division por cero")