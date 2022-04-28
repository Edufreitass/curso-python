pessoa = {'nome': 'Prof(a). Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
print(pessoa)
pessoa['cursos'].append('Angular')
print(pessoa)
pessoa.pop('idade')
print(pessoa)
pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)
