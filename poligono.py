# Imprime um quadrado
# Define a função 'ret' que recebe dois parâmetros: 'l' para largura e 'a' para altura
def ret(l, a):
    # Verifica se a largura 'l' é maior que 20 e, se for, redefine 'l' como 20
    if l > 20:
        l = 20
    
    # Verifica se a altura 'a' é maior que 20 e, se for, redefine 'a' como 20
    if a > 20:
        a = 20
    
    # Imprime uma linha horizontal formada por '-+-' repetida 'l' vezes
    print('-+-'*l)
    
    # Inicializa o contador 'c' como 0
    c = 0
    
    # Enquanto 'c' for menor que a altura 'a'
    while c < a:
        # Define uma barra vertical '|' na variável 'z'
        z = '|'
        
        # Imprime a linha vertical composta por uma barra '|', seguida de espaços, repetindo 'l*3 - 1' vezes
        print(f'{z}{z:>{(l*3 - 1)}}')
        
        # Incrementa o contador 'c'
        c += 1
    
    # Imprime uma linha horizontal formada por '-+-' repetida 'l' vezes
    print('-+-' * l)

# Solicita ao usuário que digite a largura e armazena o valor em 'l'
l = int(input('Digite a largura: '))

# Solicita ao usuário que digite a altura e armazena o valor em 'a'
a = int(input('Digite a altura: '))

# Chama a função 'ret' com os valores de largura 'l' e altura 'a' fornecidos pelo usuário como argumentos
ret(l, a)
