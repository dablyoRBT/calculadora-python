#Validação de entrada inicial ------------------------------------------------------------
operacoes = ["+", "-", "/", "*", "="]
def validar():
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
            resultado = calcular(n1, n2, operacao)
            loop(resultado)
            break

#Calculadora -----------------------------------------------------------------------------     
def calcular(value1, value2, operation):
    match operation:
        case "+":
            return value1 + value2
        case "-":
            return value1 - value2
        case "*":
            return value1 * value2
        case "/":
            try:
                return value1 / value2
            except ZeroDivisionError:
                return "Indefinido!"  
            
#Laço principal de repetições ------------------------------------------------------------
def loop(result):
    atual = result
    while True:
        try:
            operacao = input("Digite outra operação ou = para finalizar: ")
            if operacao in operacoes: 
                if operacao == "=":
                    print(f"Resultado: {atual}")
                    break
                else:
                    add = float(input("Digite outro valor: "))
                    atual = calcular(atual, add, operacao)
                    continue  
            else: 
                print("Operação inválida!") 
                continue 
        except ValueError:
            print("Você digitou um valor inválido!")
        
    
validar()