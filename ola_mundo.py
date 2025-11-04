"""
Função print()

A função print() é uma função embutida (built-in) do Python usada para exibir informações na tela (saída padrão).

Sintaxe:
    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

Parâmetros:
    *objects → Um ou mais valores que serão exibidos.
    sep       → Define o separador entre os valores (padrão: espaço ' ').
    end       → Define o que será colocado no final da linha (padrão: quebra de linha '\n').
    file      → Define o destino da saída (padrão: sys.stdout — a tela).
    flush     → Se True, força a exibição imediata da saída.

Exemplos:
    print('Olá,Mundo!')      → imprime o texto "Olá,Mundo!"
    print(10)                → imprime o número 10
    print('Ricardo', 32)     → imprime "Ricardo 32"
"""

# Exemplo 1: texto simples
print('Olá,Mundo!')

# Exemplo 2: número inteiro
print(10)

# Exemplo 3: múltiplos valores
print('Ricardo', 32)

# Exemplo 4: alterando o separador (opcional)
print('Python', 'é', 'legal', sep='-')  # Saída: Python-é-legal

# Exemplo 5: alterando o final da linha (opcional)
print('Olá', end=' ')
print('Mundo!')  # Saída: Olá Mundo!

print('------------------Exercicios ------------------\n')

print('''Vamos praticar o uso da função print com algumas atividades. Para isso, solucione os problemas propostos em código:

Imprima a frase Escola de Dados da Alura!.

Imprima seu nome e seu sobrenome seguindo a estrutura abaixo:

Nome: [seu nome]
Sobrenome: [seu sobrenome]\n''')
print('Resolução da Atividades: \n')
print('Escola Backend Python da Alura!')

print('Nome: Ricardo')
print('Sobrenome: Silva Franco\n')

print('Imprima o seu primeiro nome letra a letra. Por exemplo, meu nome é Mirla, então eu obtenho a seguinte saída:\n')

print('R')
print('i')
print('c')
print('a')
print('r')
print('d')
print('o\n')


print('''Imprima o dia do seu nascimento em formato dia mês ano. Lembrando que os valores de dia e ano não podem estar entre aspas. Supondo uma data de aniversário dia 28 de fevereiro de 2003, o formato deve estar como no exemplo abaixo:\n''')

print(21,'de Fevereiro de',1993,'\n')



print('''Imprima, em um único print, o atual ano que você está fazendo esse curso. O valor do ano deve ser um dado numérico e a saída do print deve ser a seguinte:''')

print('Ano: 2025\n')

# Esse é um comentário de uma linha
print(10) # # Podemos colocar outro comentário em uma linha após um código
# Você pode rodar o código acima no seu notebook e verificar que todo o texto após o símbolo # é ignorado na execução.

'''docstrings'''
'''
Esse é um comentário
de várias linhas.
'''
'''Aspas Simples'''
"""aspas duplas"""