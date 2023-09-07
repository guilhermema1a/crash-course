animals = {
    'cachorro': {
        'tipo': 'canino',
        'nome_dono': 'maia'
    },

    'gato': {
        'tipo': 'felino',
        'nome_dono': 'carol'
    }

}

pets = [animals]

for animal, info in animals.items():
    print(animal.title())
    print(f"\tTipo: {info['tipo']}")
    print(f"\tNome do dono: {info['nome_dono'].title()}")