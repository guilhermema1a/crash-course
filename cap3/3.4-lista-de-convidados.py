convidados=['ana', 'julia', 'carolina']

for n in convidados:
    print(f'Oi, {n}! Quer vir para o meu jantar?')

convidado_faltante = convidados.pop()

convidados.append('joana')

print(f'\nOi, {convidados[2]}! A {convidado_faltante} não pode comparecer ao jantar, você quer vir?')

print(f'Convidados: {convidados}')