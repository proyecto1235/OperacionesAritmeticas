def ingresoNumeros():
    num1 = float(input("Denos el dato prinjcipal:  "))
    num2 = float(input("Denos el segundo numero:  "))

    return num1, num2


def suma(num1, num2):
    return num1 + num2

if __name__=="__main__":
    num1, num2 = ingresoNumeros()
    print(f"{num1} + {num2} = {suma(num1, num2)}")
