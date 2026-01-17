def validar():
    operacoes = ["+", "-", "/", "*"]
    while True: 
        try: 
            n1 = float(input("Digite um valor: ")) 
            op = input("Digite a operação: ") 
            if op in operacoes: 
                n2 = float(input("Digite outro valor: ")) 
            else: 
                print("Operação inválida!") 
                continue 
        except ValueError: print("Você digitou um valor inválido!") 
        else: 
            resultado = calcular(n1, n2, op)
            print(f"Resultado: {resultado}")
            break
        
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
            
            
validar()