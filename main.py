from clear import clear
from conversor import converter

def printMedidas():
    for item in medidas.keys():
        print(str(item) + " - " + medidas[item])

medidas = {1 : "metros",
           2 : "pés",
           3 : "jardas"}

############## INÍCIO ##############
clear()

print("Selecione a medida que deseja converter:")
printMedidas()
medidaInicial = int(input())

while(medidaInicial not in medidas.keys()):
    clear()
    print("Valor inválido. Tente novamente.\n")
    print("Selecione a medida que deseja converter:")
    printMedidas()
    medidaInicial = int(input())

val = float(input(f"Insira o valor (em {medidas[medidaInicial]}) a ser convertido - "))


print("\nDeseja converter em qual medida?")
printMedidas()
medidaFinal = int(input())

while(medidaFinal not in medidas.keys()):
    clear()
    print("Valor inválido. Tente novamente.\n")
    print("Deseja converter em qual medida?")
    printMedidas()
    medidaFinal = int(input())

resultado = converter(medidas[medidaInicial], medidas[medidaFinal], val)
print(f"{val} {medidas[medidaInicial]} = {resultado} {medidas[medidaFinal]}")
