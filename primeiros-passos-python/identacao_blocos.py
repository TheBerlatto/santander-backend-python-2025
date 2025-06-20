def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro no local indicado.")

    print("Obrigado por ser nosso cliente, stay strong!")


def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)