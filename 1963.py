valor = input("escreva filho: ")
resultado=0
lista = (valor.split())

um_por_cento = int(lista[0])/100
primeiro = lista[0]
objetivo = int(lista[1])

n=0
modificador = 1

while resultado!=objetivo:
    resultado = (primeiro*(1+n/10))
    print(resultado)
    n+=1

print(modificador)
"""
while resultado!=lista[1]:
    print(resultado)
    resultado=resultado*um_por_cento
    um_por_cento = um_por_cento*2

for n in range(0, 100):
    resultado = 0.1*modificador
    modificador+=1
    print(resultado)
"""