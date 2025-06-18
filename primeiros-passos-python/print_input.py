nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(f"Os dados informados foram: {nome}, {idade} anos.")

print(nome, idade, end="... \n")
print(nome, idade, sep=" | ")
print(nome, idade, sep=" | ", end=" !!!")