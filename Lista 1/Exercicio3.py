print('Qual o verdadeiro nome do super-heroi Batman?:')
print(' Opção A Clark Kent \n Opção B Bruce Wayne \n Opção C Steve Rogers \n Opção D Tony Stark \n Opção E Peter Parker')
batman = str(input('Qual o verdadeiro nome do super-heroi Batman?:'))


if batman == 'B' or batman == 'b':
    print('certo')
elif batman != 'B' or batman != 'b':
    print('errado')