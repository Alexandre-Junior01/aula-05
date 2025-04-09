cont1=0
cont2=0
for i in range(10):
    num=int(input("Digite um numero: "))
    if 10 <= num <= 20:
        cont1+=1

    else:
        cont2+=1

print(f"numeros entre 10 e 20 que estão no intervalo foram de {cont1} no total")
print(f"numeros fora do intervalo foi de {cont2} no total")
