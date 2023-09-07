program = {
    'python': 'O Python é uma linguagem de programação amplamente usada em aplicações da Web, desenvolvimento de softwar'
              'e, ciência de dados e machine learning (ML).\n',
    'java': 'Java é uma linguagem multiplataforma, orientada a objetos e centrada em rede que pode ser usada como uma pl'
            'ataforma em si.\n',
    'c++': 'C++ é uma das linguagens mais versáteis que existem, permitindo desenvolver desde tarefas simples como aplic'
           'ações na linha de comando ou web, até sistemas complexos de tempo real, muito usadas no mercado financeiro.\n'
}

for language, description in program.items():
    print(f'{language}: {description}')