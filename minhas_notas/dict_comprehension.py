# {chave : recebe valor x FOR elemento IN dados iteraveis}

dicionario1 = {elemento: elemento * 2 for elemento in range(5)}
print(dicionario1)

#---------------------------------------------------------------

lista2 = ['Uno', 'Palio', 'Punto']
dicionario2 = {f'{elemento.lower()}' : f'muda para {elemento.upper()}' for elemento in lista2}
print(dicionario2)

#---------------------------------------------------------------

dict_carros = { 'Uno' : 1000, 'Palio' : 2000, 'Punto' : 3000}
dicionario3 = { chave: f'{chave.upper()} vale {valor}' for chave, valor in dict_carros.items() }
print(dicionario3)

#---------------------------------------------------------------

dicionario4 = { chave: f'{chave.upper()} custa {valor}' for chave, valor in dict_carros.items() if valor >= 2000 }
print(dicionario4)

#---------------------------------------------------------------

animais = {
  'cao': 'pelos',
  'pato': 'penas',
  'nemo': 'escamas',
  'gato': 'pelos',
  'galinha': 'penas',
  'dory': 'escamas'
}

mamiferos = {
  chave: 'verificado' for chave, valor in animais.items() if valor == 'penas'
}
print(mamiferos)