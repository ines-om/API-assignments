from math import ceil

print("------- Programa para loja de tintas. -------" + "\n")

area = input("Inserir o valor da área (em m^2) a ser pintada:  ")
print("\n")

print("LATAS - INFORMAÇÕES:" + "\n")
# 1L corresponde a 3 m^2
tinta = int(area)/3

#1 lata corresponde a 18L
latas = ceil(int(tinta)/18)
print("Quantidade de latas necessárias: " + str(latas))
#preço a pagar
preço = int(latas)*95
print("Preço das latas: " + str(preço) + "€")

#Opção de desconto
print("\n" + "DESCONTOS:")
desconto = input("Introduzir desconto: ")

if (1<=int(desconto)<=100):
    desc = int(preço)*int(desconto)*(1/100)
    preço_desc = int(preço) - int(desc)
    print("Preço com desconto: " + str(preço_desc) +"€")
    IVA = 23*1/100*int(preço_desc)
    print("\n" + "IVA:")
    print("Valor IVA: " + str(IVA) + "€")
    total = int(preço_desc) + int(IVA)
    print("-----")
    print("PREÇO TOTAL:" + str(total) + "€")
    print("-----")
    print("Processamento concluído!")
elif int(desconto) == 0:
    IVA = (23*1/100)*int(preço)
    print("\n" + "IVA:")
    print("Valor IVA: " + str(IVA) + "€")
    total = int(preço) + int(IVA)
    print("-----")
    print("PREÇO TOTAL:" + str(total) + "€")
    print("-----")
    print("Processamento concluído!")
else:
    print("Valor inválido.")

