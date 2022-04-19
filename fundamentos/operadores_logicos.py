print(True or False)
print(7 != 3 and 2 > 3)

# Tabela verdade do AND
print("Tabela verdade do AND")
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print(True and True and False and True and True and True)  # False

# Tabela verdade do OR
print("Tabela verdade do OR")
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
print(False or False or True or False or False or False)  # True

# Tabela verdade do XOR
print("Tabela verdade do XOR")
print(True != True)  # False
print(True != False)  # True
print(False != True)  # True
print(False != False)  # False

# Operador de Negação (unário)
print("Operadores de Negação (unário)")
print(not True)  # False
print(not False)  # True

print(not 0)  # True
print(not 1)  # False
print(not not -1)  # True
print(not not True)  # True

# Cuidado!
print("Operadores Bit-a-bit")
print(True & False)
print(True | False)
print(True ^ False)
