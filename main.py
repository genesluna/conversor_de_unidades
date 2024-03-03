from os import system, name
from conversor_de_unidades import ConversorDeUnidades


def limpar_tela():
    # Verifica o sistema operacional e executa o comando apropriado para limpar a tela
    if name == "nt":  # Windows
        system("cls")
    else:  # Mac e Linux
        system("clear")


def main():
    # Inicializa o conversor de unidades
    conversor_de_unidades = ConversorDeUnidades()

    limpar_tela()

    # Apresenta o cabeçalho do programa
    print("=" * 40)
    print(f"{'Conversor de Unidades':^40}")
    print("=" * 40, end="\n\n")
    print("1. Quilômetros para Milhas")
    print("2. Litros para Galões")
    print("3. Quilogramas para Libras")
    print("4. Celsius para Fahrenheit", end="\n\n")

    # Solicita a escolha da opção e o valor a ser convertido
    opcao = input("Escolha a opção (1 a 4): ")
    valor = input("Digite o valor a ser convertido: ")

    # Faz a conversão de acordo com a opção escolhida
    resultado = conversor_de_unidades.converter(opcao, valor)

    # Imprime o resultado com uma linha tracejada acima e abaixo
    print("-" * len(resultado))
    print(resultado)
    print("-" * len(resultado))


if __name__ == "__main__":
    # Chama a função principal quando o script é executado
    main()
