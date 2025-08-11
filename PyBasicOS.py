import os

def clear():
    os.system("clear")

while True:
    clear()
    print("Bem-Vindo ao PyBasicOS")
    print("O que deseja fazer?\n")
    print("1. Calculadora")
    print("2. Bloco de Notas")
    print("3. Campo Minado")
    print("4. Sair")

    Escolha = input("\nPrompt: ")

    if Escolha == "1":
        clear()
        number_1 = int(input("Primeiro Número: "))
        number_2 = int(input("Segundo Número: "))
        print("Resultado:", number_1 + number_2)
        input("\nPressione Enter para voltar ao menu...")

    elif Escolha == "2":
        clear()
        Notas = input("Digite sua nota: ")
        print("Nota salva:", Notas)
        input("\nPressione Enter para voltar ao menu...")

    elif Escolha == "3":
        clear()
        print("Entre um número de 1 a 100. Onde Está A Mina?")
        Mina = int(input("Local da Mina no Campo: "))
        if Mina == 12:
            print("Parabéns, Você Venceu!!")
        else:
            print("💥 Booom! Você perdeu!")
        input("\nPressione Enter para voltar ao menu...")

    elif Escolha == "4":
        clear()
        print("Saindo do PyBasicOS...")
        break

    else:
        print("Opção inválida!")
        input("\nPressione Enter para voltar ao menu...")