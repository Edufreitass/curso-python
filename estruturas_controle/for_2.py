# percorrer uma string
palavra = 'paralelepídedo'
for letra in palavra:
    print(letra, end=',')
print('Fim')

# percorrer uma lista
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

# percorrer e acessar o indice
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

# percorrer uma tupla
dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

# percorrer um set
for letra in set('muito legal'):
    print(letra)

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
