# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')

# Funcao sortear_dado 6 numeros entre 1 e 6
# For com range 1 a 6
# Se for impar continue
# Se o numero for par e for igual ao valor sorteado pela
# funcao dado imprimir a string 'ACERTOU' e depois chamar o break
# Se não acertar chama o else... print('Não acertou o número!')

from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('ACERTOU', i)
        break
else:
    print('Não acertou o número!')
