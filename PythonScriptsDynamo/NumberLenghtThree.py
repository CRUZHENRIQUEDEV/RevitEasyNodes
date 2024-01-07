# Função para formatar os números conforme as regras especificadas
def formatar_numeros(lista_numeros):
    numeros_formatados = []
    for numero in lista_numeros:
        if numero < 10:
            numero_formatado = "00" + str(numero)
            numeros_formatados.append(numero_formatado)
        elif 10 <= numero < 100:
            numero_formatado = "0" + str(numero)
            numeros_formatados.append(numero_formatado)
        else:
            numeros_formatados.append(str(numero))
    return numeros_formatados

# Entrada para a lista de números
numeros = IN[0]

# Chamando a função para formatar os números
numeros_formatados = formatar_numeros(numeros)

# Saída com os números formatados
OUT = numeros_formatados
