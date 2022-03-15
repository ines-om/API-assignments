print("----- Cálculo de média escolar! ------" + "\n")

print("---")
nome = input("Nome do aluno: ")
escola = input("Escola: ")
print("---" + "\n")

print("DISCIPLINAS: ")
notas = []
disciplinas = input("Número de disciplinas: ")
nr_d = int(disciplinas)

for i in range(0, int(nr_d)):
    nota_i = input("Nota da disciplina " + str(i) + " : ")
    if (0<=int(nota_i)<=20):
        notas.append(int(nota_i))
        continue
    else:
        print("Valores inválidos! Notas de 0-20.")
        break


print("\n" + "----")
soma_notas = sum(notas)
média = int(soma_notas)/int(disciplinas)
print("Valor da média: "  + str(média))
print("\n" + "----")
print("Aluno:" + str(nome))
print("Escola: " + str(escola))











