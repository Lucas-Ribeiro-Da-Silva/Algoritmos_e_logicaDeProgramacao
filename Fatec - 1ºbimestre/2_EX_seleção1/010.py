#10. Fornecidas duas datas distintas, exibir qual delas ocorre primeiro. Cada data será fornecida em três valores inteiros, onde o primeiro representa o dia, o segundo o mês e o terceiro o ano.


dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

dia2 = int(input("Digite o dia: "))
mes2 = int(input("Digite o mês: "))
ano2 = int(input("Digite o ano: "))

if ano < ano2:
    print(dia, "/", mes, "/", ano)
elif ano == ano2:
    if mes<mes2:
        print(dia, "/", mes, "/", ano)
    elif mes == mes2:
        if dia<dia2:
            print(dia, "/", mes, "/", ano)
        elif dia == dia2:
            print(dia2, "/", mes2, "/", ano2)
            print(dia, "/", mes, "/", ano)
        else:
            print(dia2, "/", mes2, "/", ano2)
    else:
         print(dia2, "/", mes2, "/", ano2)
else:
     print(dia2, "/", mes2, "/", ano2)