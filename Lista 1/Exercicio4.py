print('Qual o verdadeiro nome do super-heroi Batman?:')

OpçãoA = 'a) Bruce Wayne'
OpçãoB = 'b) Clark Kent'
OpçãoC = 'c) Peter Parker'
OpçãoD = 'd) Tony Stark'
OpçãoE = 'e) Steve Rogers'

print(OpçãoA)
print(OpçãoB)
print(OpçãoC)
print(OpçãoD)
print(OpçãoE)

batman = str(input('Qual o verdadeiro nome do super-heroi Batman?:'))

if batman == 'B' or batman == 'b':
    print('certo')
elif batman != 'B' or batman != 'b':
    print('errado')