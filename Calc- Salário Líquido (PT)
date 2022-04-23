print("Programa de Processamento de Salários: " + "\n")

salario_hora= input("Insira aqui salário por hora: ")
horas = input("Insira aqui o número de horas efetuadas durante o mês: ")
dias = input("Insira aqui a quantidade de dias em que trabalhou: ")

#Cálculo de salário iliquido:
print("SALÁRIO ILÍQUIDO:" + "\n")
salario_iliquido = int(salario_hora)*int(horas)
print("Salário ilíquido: " +  "+" + str(salario_iliquido))

#Cálculo de descontos:
print("VALOR DE DESCONTOS:" + "\n")
segu_social = 11%int(salario_iliquido)
print("Valor segurança social:" + "-" + str(segu_social))
IRS = 10%int(salario_iliquido)
print("Valor IRS:" + "-" + str(IRS))
Sindicato = 1%int(salario_iliquido)
print("Valor do Sindicato:" + "-" + str(Sindicato))

Descontos_Total = int(segu_social) + int(IRS) + int(Sindicato)
print("\n" + "TOTAL DESCONTOS:" + "-" + str(Descontos_Total))

#Cálculo de subsidio de refeição por mês
print("\n"+ "SUBSÍDIOS:")
sub_ref = (12/2)*int(dias)
print("Subsídio de Refeição por mês: " + "+" + str(sub_ref))

#Calculo do salário líquido
print("\n")
sal_liquido = float(salario_iliquido) - float(Descontos_Total) + float(sub_ref)
print("SALÁRIO LÍQUIDO: " + str(sal_liquido))
