#Calculadora -----------------------------------------------------------------------------     
def calcular(value1, value2, operation):
    match operation:
        case "+":
            return value1 + value2
        case "-":
            return value1 - value2
        case "*":
            return value1 * value2
        case "**":
            return value1 ** value2
        case "/":
            try:
                return value1 / value2
            except ZeroDivisionError:
                return "ZeroDivisionError"
        case "%":
            try:
                return value1 % value2
            except ZeroDivisionError:
                return "ZeroDivisionError"


#Validação de entrada inicial ------------------------------------------------------------
def obter_entrada():
    operacoes = ["+", "-", "/", "*", "**", "%"]
    while True: 
        try: 
            n1 = float(input("Digite um valor: ")) 
            operacao = input("Digite a operação: ") 
            if operacao in operacoes: 
                n2 = float(input("Digite outro valor: ")) 
            else: 
                print("Operação inválida!") 
                continue 
        except ValueError: print("Você digitou um valor inválido!") 
        else: 
            return [n1, operacao, n2]
            
#Laço principal de repetições ------------------------------------------------------------
def montar_operacao(entrada):
    operacoes = ["+", "-", "/", "*", "**", "%", "="]
    expressao = entrada
    while True:
        try:
            operacao = input("Digite outra operação ou = para finalizar: ")
            if operacao in operacoes: 
                if operacao == "=":
                    return expressao
                    
                else:
                    add = float(input("Digite outro valor: "))
                    expressao.append(operacao)
                    expressao.append(add)
                    continue  
            else: 
                print("Operação inválida!") 
                continue 
        except ValueError:
            print("Você digitou um valor inválido!")
        
#Define a ordem de precedência dentro da expressão matemática ----------------------------
def precedencia(array):
    #verifica a potenciação
    i = 0
    while i < len(array):
        if array[i] == "**":
            x = i - 1  # Número antes
            y = i + 1  # Número depois
            z = calcular(array[x], array[y], array[i]) # Realiza o cálculo
            if z == "ZeroDivisionError":
                return "ZeroDivisionError"
            else:
                array.pop(y) #
                array.pop(i) # Remove os valores calculados da lista e insere o resultado no lugar
                array.pop(x) #
                
                array.insert(x, z) # Resultado
                
                i = 0 # Set para zero, pois a lista mudou...
        else:
            i += 1

    #Verifica ("*", "/", "%")
    i = 0
    while i < len(array):
        if array[i] in ("*", "/", "%"):
            x = i - 1  
            y = i + 1  
            z = calcular(array[x], array[y], array[i]) 
            if z == "ZeroDivisionError":
                return "ZeroDivisionError"
            else:
                array.pop(y) 
                array.pop(i) 
                array.pop(x) 
                
                array.insert(x, z) 
                
                i = 0 
        else:
            i += 1

    #Verifica soma e subtração
    i = 0
    while i < len(array):
        if array[i] == "+" or array[i] == "-":
            x = i - 1 
            y = i + 1  
            z = calcular(array[x], array[y], array[i])

            array.pop(y) 
            array.pop(i) 
            array.pop(x) 
            array.insert(x, z)
            
            i = 0 
        else:
            i += 1
    
    return array[0]
        
#Controle do programa -------------------------------------------------------------------------
def main():
    while True: 
        dados = obter_entrada()
        expressao_final = montar_operacao(dados)
        resultado = precedencia(expressao_final)
        if resultado == "ZeroDivisionError":
            print("Erro de divisão por zero!")
            print("Reiniciando programa...")
            continue
        else:
            print(f"O resultado é: {resultado}")
            while True:
                end = input("Deseja continuar? (s/n): ").upper()
                if end == "S" or end == "N":
                    break
                else:
                    print("Por favor, digite S para sim ou N para não!")
                    continue
        if end == "S":
            continue
        elif end == "N":
            print("Fim do programa!")
            break
                    
main()