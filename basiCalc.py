calc = True

def calculadora(n1,operator,n2):
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


def teste(calc):
    while calc:
            num1 = float(input('Insira os numeros a serem calculados: '))
            operator = input('Insira o operador para o cálculo: ')
            num2 = float(input('Insira os numeros a serem calculados: '))
            result= calculadora(num1,operator,num2)
            print(result) 
            calc = False
            

inicio = input("Deseja fazer uma conta? sim ou nao  ")
print(inicio)
if inicio == 'sim':
    resultado = teste(calc)
    continua = input('s or n')
    if continua == 's':
        calc = True
        teste(calc)
        








