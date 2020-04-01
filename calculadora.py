import time
valor1 = int(input('Digite um valor:'))
valor2 = int(input('Digite um valor:'))
opc = 0
while opc != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] DIGITE NOVOS VALORES
    [ 5 ] FIM''')
    opc = int(input('>>> Digite uma opção: '))
    if opc == 1:
        soma = valor1 + valor2
        print('O valor {} e {} somados é {}'.format(valor1,valor2,soma))
    elif opc == 2:
        multiplicar = valor1 * valor2
        print('O valor {} e {} multiplicados é {}'.format(valor1,valor2,multiplicar))
    elif opc == 3:
        if valor1 > valor2:
            print('O valor {} é maior que o valor {}'.format(valor1,valor2))
        elif valor1 < valor2:
            print('O valor {} é maior que o {}'.format(valor2,valor1))
    elif opc == 4:
        print('Digite novos numeros:')
        valor1 = int(input('Digite o primeiro valor:'))
        valor2 = int(input('Digite o segundo valor:'))
    elif opc == 5:
        print('<<Finalizando>>')
        time.sleep(1)
        print('Prgrama encerrado.')
    else:
        print('INCORRETO.\nDigite outra opção.')
    print('-=' * 20 )
    print('\n')
    time.sleep(2)