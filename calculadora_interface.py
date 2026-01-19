import tkinter as tk
import calculadora as calculadora_logica

# Funções

def clicar(valor):
    atual = display.get()
    display.delete(0, tk.END)
    display.insert(0, atual + valor)

def limpar():
    display.delete(0, tk.END)

def transformar_em_lista(expressao):
    tokens = []
    numero = ""

    i = 0
    while i < len(expressao):
        char = expressao[i]

        # Captura números (incluindo ponto)
        if char.isdigit() or char == ".":
            numero += char

        else:
            if numero:
                tokens.append(float(numero))
                numero = ""

            # Trata operador **
            if char == "*" and i + 1 < len(expressao) and expressao[i + 1] == "*":
                tokens.append("**")
                i += 1
            else:
                tokens.append(char)

        i += 1

    if numero:
        tokens.append(float(numero))

    return tokens


def calcular_resultado():
    try:
        expressao = display.get()
        lista = transformar_em_lista(expressao)
        resultado = calculadora_logica.precedencia(lista)

        if resultado == "ZeroDivisionError":
            display.delete(0, tk.END)
            display.insert(0, "Erro")
        else:
            display.delete(0, tk.END)
            display.insert(0, str(resultado))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

# App principal

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)

# Display

display = tk.Entry(
    janela,
    font=("Arial", 24),
    justify="right"
)
display.pack(padx=10, pady=10, fill="x")

# Frame dos botões

frame = tk.Frame(janela)
frame.pack(expand=True, fill="both")

# Botões (layout)

botoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["C", "**", "=", ""]
]

for linha in botoes:
    linha_frame = tk.Frame(frame)
    linha_frame.pack(expand=True, fill="both")

    for texto in linha:
        if texto == "C":
            botao = tk.Button(linha_frame, text=texto, font=("Arial", 18), command=limpar)

        elif texto == "=":
            botao = tk.Button(linha_frame, text=texto, font=("Arial", 18), command=calcular_resultado)

        elif texto == "":
            botao = tk.Label(linha_frame)  # espaço vazio
        else:
            botao = tk.Button(
            linha_frame,
            text=texto,
            font=("Arial", 18),
            command=lambda t=texto: clicar(t)
        )

        botao.pack(side="left", expand=True, fill="both")

# Loop da janela
janela.mainloop()


