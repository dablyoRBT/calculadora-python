#Validação de entrada inicial ------------------------------------------------------------
operacoes = ["+", "-", "/", "*", "="]
def obter_entrada():
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
            return n1, n2, operacao

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
def executar_operacoes(result):
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
        
#Controle do programa -------------------------------------------------------------------------
def main():
    entrada = obter_entrada()
    resultado = calcular(*entrada)
    executar_operacoes(resultado)
    while True:
        end = input("Deseja continuar? (s/n): ").upper()
        if end == "S":
            entrada = obter_entrada()
            resultado = calcular(*entrada)
            executar_operacoes(resultado)
            continue
        elif end == "N":
            print("Fim do programa!")
            break
        else:
            print("Por favor, digite S para sim ou N para não!")
            continue
        

main()