nomes = ['Ana', 'Bruno', 'Carlos']
resultado = ', '.join(nomes)
print(resultado)

nomes = ['Ana', 'Bruno', 'Carlos']
print(', '.join(nomes)) 

numeros = ['1', '2', '3', '4']
resultado = '-'.join(numeros)
print(resultado)  

letras = ['A', 'B', 'C']
resultado = ' '.join(letras)
print(resultado)

# Os elementos da lista que você quer juntar precisam ser strings.
# Se os elementos forem de outro tipo (como inteiros ou floats),
# você precisa convertê-los para string antes de usar o join():