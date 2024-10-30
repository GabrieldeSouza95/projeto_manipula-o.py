from math import trunc


def ordenar_lista(lista):
    """Ordena uma lista de números e retorna a lista ordenada"""
    return sorted(lista)

def maior_menor(lista):
    """Retorna o maior e o menor valor de uma lista"""
    return max(lista), min(lista)

def contar_palavras(texto):
    """Conta o número de palavras em um texto e retorna a contagem e a lista de palavras."""
    palavras = texto.split()
    return len(palavras), palavras

def remover_duplicatas(lista):
    """Remove duplicatas de uma lista e retorna a lista resultante."""
    return list(set(lista))

def juntar_lista(lista1, lista2):
    """Junta duas listas e retorna uma nova lista"""
    return lista1 + lista2

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\nMenu de Opções: ")
    print("1. Ordenar uma lista de números.")
    print("2. Encontrar o maior e o menor valor em uma lista.")
    print("3. Contar palavras em um texto.")
    print("4. Remover duplicatas em uma lista.")
    print("5. Juntar duas listas.")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-6): ")

        if escolha == '1':
            numeros = input("Digite números separados por vírgula: ")
            lista_numeros = [int(num) for num in numeros.split(',')]
            lista_ordenada = ordenar_lista(lista_numeros)
            print(f"Lista ordenada: {lista_ordenada}")

        elif escolha == '2':
            numeros = input("Digite números separados por vírgula: ")
            lista_numeros = [int(num) for num in numeros.split(',')]
            maior, menor = maior_menor(lista_numeros)
            print(f"Maior valor: {maior}, Menor Valor: {menor}")

        elif escolha == '3':
            texto = input("Digite o texto: ")
            contagem, palavras = contar_palavras(texto)
            print(f"Número de palavras: {contagem}")
            print(f"As palavras são: {palavras}")

        elif escolha == '4':
            numeros = input("Digite números separados por vírgula: ")
            lista_numeros = [int(num) for num in numeros.split(',')]
            lista_sem_duplicatas = remover_duplicatas(lista_numeros)
            print(f"Lista sem duplicatas: {lista_sem_duplicatas}")

        elif escolha == '5':
            lista1 = input("Digite a primeira lista de números separados por vírgula: ")
            lista2 = input("Digite a segunda lista de números separados por virgula: ")
            lista1 = [int(num) for num in lista1.split(',')]
            lista2 = [int(num) for num in lista2.split(',')]
            lista_junta = juntar_lista(lista1, lista2)
            print(f"Lista junta: {lista_junta}")

        elif escolha == '6':
            print("Saindo do programa")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()