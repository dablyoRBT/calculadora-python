n1 = float(input("Digite um valor: "))
op = input("Digite a operação: ")
n2 = float(input("Digite outro valor: "))

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
        print(n1 / n2)