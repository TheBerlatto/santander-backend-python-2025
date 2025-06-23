texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
# Semelhante ao fori do Java
for numero in range(0, 51, 5): # Começa em 0, Finaliza em 51, Incrementa de 5 em 5
    print(numero, end=" ")