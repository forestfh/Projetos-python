from time import sleep


def linha():
    print('')


sair = False

while not sair:
    print('Aumento de salario    [1]\n'
          'calcular porcentagem  [2]\n'
          'sair                  [3]\n')

    opc = int(input('digite sua opção:'))

    if opc == 1:
        try:
            linha()
            salario = float(input('digite seu salario R$:'))
            porcentagem_aumento = float(input('digite o aumento em porcentagem %:'))
            mult = salario * porcentagem_aumento
            div = mult / 100
            atualizado_salario = salario + div
            print(f'salario após o aumento R$: {atualizado_salario}\n')
        except Exception as e:
            print(f'erro encontrado> {e}/digite novamente!')

    if opc == 2:
        try:
            valor = float(input('digite o valor R$:'))
            por = float(input('digite a porcentagem do valor %:'))
            linha()
            mult1 = valor * por
            div1 = mult1 / 100
            sleep(0.5)
            print('{:.2f}% de {:.2f}-R$ é igual a: {:.2f}-R$'.format(por, valor, div1), flush=True)    #Formatação float
                                                                                                       #Por casas decimais {:.2f}
            linha()
        except Exception as e1:
            print(f'erro encontrado> {e1}//digite novamente!')

    if opc == 3:
        sleep(1)
        print('saindo do programa..',
              flush=True)
        sleep(0.9)
        sair = True
    else:
        linha()
        print('digite uma opção valida!'.upper())
        linha()

