var_1 = float(input("Digite um número: "))
var_op = input("Escolha um operador aritmético (+, -, *, /): ")
var_2 = float(input("Digite um outro número: "))
if var_op == "+":
    print(f"O resultado da operação é {var_1 + var_2}")
elif var_op == "-":
        print(f"O resultado da operação é {var_1 - var_2}")
elif var_op == "*":
        print(f"O resultado da operação é {var_1 * var_2}")
elif var_op == "/":
    if var_2 != 0:
        print(f"O resultado da operação é {var_1 / var_2}")
    else:
        print("Erro. Divisão por 0")    

else:
    print("Erro na operação. Verifique os valores digitados")


