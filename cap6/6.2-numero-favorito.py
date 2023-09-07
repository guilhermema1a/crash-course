from random import randint
favorite_number = {
    'leo': randint(1, 10),
    'ana': randint(1, 10),
    'bia': randint(1, 10),
}

for k, v in favorite_number.items():    #ITEMS
    print(f'{k.title()}: {v}')

print('Essas são as chaves: ', end='')
for k in favorite_number.keys():    #KEYS
    print(k.title(), end=' ')

print('\nEsses são os valores: ', end='')
for v in favorite_number.values():    #VALUES
    print(v, end=' ')

print('\nEsses são os pares chave-valor: ', end='')
for kv in favorite_number.items():    #ITEMS
    print(kv, end=' ')

'''
.keys() - retorna a chave
    
.values() - retorna os valores das chaves
    
.items() - retorna os pares chave-valor
'''