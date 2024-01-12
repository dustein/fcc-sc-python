#List comprehension é uma forma de criar e manipular listas
#[expressão for item in lista] = aplique a expressão em cada item da lista
#---------------------------------------------

lista_for = []
for item in range(10):
  lista_for.append(item * 2)
print(lista_for)
#usando a comprehension:
lista_comp = [item * 2 for item in range(10)]
print(lista_comp)

#---------------------------------------------

lista_minusculas = ['a', 'b', 'c']
maiusulas_for = []
for item in lista_minusculas:
  maiusulas_for.append(str(item).upper())
print(maiusulas_for)
#usando comprehension:
maiusculas_comp = [str(item).upper() for item in lista_minusculas]
print(maiusculas_comp)

#---------------------------------------------

#usando IF
lista_pares = [numero for numero in range(10) if numero % 2 == 0]
print(lista_pares)

lista_pares_dividePor5 = [numero for numero in range(100) if numero % 5 == 0 if numero % 2 == 0]
print(lista_pares_dividePor5)

lista_1_se_divide_5 = ['1' if numero % 5 == 0 else '0' for numero in range(10)]
print(lista_1_se_divide_5)

