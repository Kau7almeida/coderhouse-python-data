# Classe x Objeto

# primeiro pilar: ABSTRAÇÃO

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        pi = 3.14592653
        return pi * (self.raio**2)
    
    def imprime(self):
        print(f"Circulo de raio {self.raio} ")

circulo = Circulo(5) # ou Circulo(raio=5)
circulo.imprime()
print(circulo.area())
print(type(circulo))

circulo2 = Circulo(10)
circulo2.imprime()
print(circulo2.area())

# segundo pilar: HERANÇA

class FormaGeometrica():
    def area(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        pi = 3.14592653
        return pi * (self.raio ** 2)
    
    def imprime(self):
        pass

circulo = Circulo(5) # ou Circulo(raio = 5)
circulo.imprime()
print(circulo.area())
print(type(circulo))

circulo2 = Circulo(10)
circulo2.imprime()
print(circulo2.area())

class Quadrado(FormaGeometrica):
    def __init__(self, lado): # construtor
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
    def imprime(self):
        print(f"Quadrado de lado {self.lado} ")

quadrado = Quadrado(lado = 5)
print(quadrado.area())
print(quadrado.lado)

# ENCAPSULAMENTO

# POLIMORFISMO


