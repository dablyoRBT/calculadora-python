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
    except ValueError:
        print("Você digitou um valor inválido!")
    else:
        break

match op:
    case "+":
        if n1.is_integer() and n2.is_integer() :
            print(int(n1 + n2))
        else:
            print(float(n1 + n2))
    case "-":
        if n1.is_integer() and n2.is_integer() :
            print(int(n1 - n2))
        else:
            print(float(n1 - n2))
    case "*":
        if n1.is_integer() and n2.is_integer() :
            print(int(n1 * n2))
        else:
            print(float(n1 * n2))
    case "/":
        try:
            print(n1 / n2)
        except ZeroDivisionError:
            print("Indefinido!")