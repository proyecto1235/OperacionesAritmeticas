class OperacionesAritmeticas():
    def ingresoNumeros(self):
        num1 = float(input("Denos el dato prinjcipal:  "))
        num2 = float(input("Denos el segundo numero:  "))

        return num1, num2


    def suma(self,num1, num2):
        return num1 + num2

if __name__=="__main__":
    operacion=OperacionesAritmeticas()
    num1, num2 = operacion.ingresoNumeros()
    print(f"{num1} + {num2} = {operacion.suma(num1, num2)}")
