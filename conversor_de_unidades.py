import locale


class ConversorDeUnidades:

    def __init__(self):
        # Inicializa o objeto ConversorDeUnidades e define a formatação para o padrão brasileiro
        locale.setlocale(locale.LC_ALL, "pt_br")

    def km_para_milhas(self, quilometros):
        # Converte quilômetros para milhas utilizando o fator de conversão
        fator_conversao = 0.621371
        milhas = quilometros * fator_conversao
        return round(milhas, 2)

    def litros_para_galoes(self, litros):
        # Converte litros para galões utilizando o fator de conversão
        fator_conversao = 0.264172
        galoes = litros * fator_conversao
        return round(galoes, 2)

    def kg_para_libras(self, quilogramas):
        # Converte quilogramas para libras utilizando o fator de conversão
        fator_conversao = 2.20462
        libras = quilogramas * fator_conversao
        return round(libras, 2)

    def celsius_para_fahrenheit(self, celsius):
        # Converte graus Celsius para Fahrenheit utilizando a fórmula
        fahrenheit = (celsius * 9 / 5) + 32
        return round(fahrenheit, 1)

    def converter(self, opcao, valor):
        # Remove espaços e troca vírgula por ponto, caso existam.
        valor, opcao = (str(valor).strip().replace(",", "."), str(opcao).strip())

        # Tenta converter o valor entrado em decimal. Se não der certo, retorna mensagem de erro.
        try:
            valor = float(valor)
        except:
            return "ERRO: Entrada inválida. Certifique-se de digitar um valor válido."

        # Faz a conversão de acordo com a opção escolhida e retorna uma string formatada com o valor convertido.
        if opcao == "1":
            resultado = self.km_para_milhas(valor)
            return f"{locale.format_string('%.2f', valor)} quilômetros é igual a {locale.format_string('%.2f', resultado)} milhas."
        elif opcao == "2":
            resultado = self.litros_para_galoes(valor)
            return f"{locale.format_string('%.2f', valor)} litros é igual a {locale.format_string('%.2f', resultado)} galões."
        elif opcao == "3":
            resultado = self.kg_para_libras(valor)
            return f"{locale.format_string('%.2f', valor)} quilogramas é igual a {locale.format_string('%.2f', resultado)} libras."
        elif opcao == "4":
            resultado = self.celsius_para_fahrenheit(valor)
            return f"{locale.format_string('%.1f', valor)} graus Celsius é igual a {locale.format_string('%.1f', resultado)} graus Fahrenheit."
        else:
            return "ERRO: Opção inválida. Certifique-se de escolher uma opção válida."
