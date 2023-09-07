
#DICIONÁRIO
favorite_language = {
    'julio': 'javascript',
    'carlos': 'c#',
    'joao': 'rust',
    'carol': 'c++',
}
entrevistado = ['julio', 'joao']

for name in favorite_language:
    print(name, end=' ')

    if name in entrevistado:
        print(f'obrigado pela participação')
    else:
        print('estou aguardando sua resposta')