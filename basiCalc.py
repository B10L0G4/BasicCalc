def operadores(n1,operator,n2):
    match operator:
        case '+':
            soma = n1 + n2
            return soma
        case '-':
            sub = n1 - n2
            return sub
        case '*':
            multi = n1 * n2
            return multi
        case '/': 
            div = n1 / n2
            return div
        case '%':
            porc = (n1/100)*n2
            return porc


def calculadora():
    calc = True
    num1 = float(input('Insira os numeros a serem calculados: '))
    while calc:
        operator = input('Insira o operador para o cálculo: ')
        num2 = float(input('Insira os numeros a serem calculados: '))
        result= operadores(num1,operator,num2)
        print(result) 
        continua = input('Digite s para continuar\nn para um novo calculo\n exit para fechar a calculadora\n')
        if continua == 's':
            num1 = result
        elif continua == 'n': 
            calc = False
            calculadora()
        else:
            break
            

calculadora()    

        








