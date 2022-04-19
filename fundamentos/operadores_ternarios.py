esta_chuvendo = True
# secas -> False
# molhadas -> True
print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chuvendo])
print('Hoje estou com as roupas ' + ('molhadas.' if esta_chuvendo else 'secas.'))