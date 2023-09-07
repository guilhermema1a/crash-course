rios = {
    'nilo': 'egypt',
    'amazonas': 'brazil',
    'mississipi': 'united states'
}

for k, v in rios.items():
    print(f'O rio {k} atravessa o(a) {v}')

print('Lista de rios importantes: ', end='')
for rio in rios.keys():
    print(rio, end=' ')

print('\nPaíses onde estão esses rios: ', end='')
for paises in rios.values():
    print(paises, end=' ')