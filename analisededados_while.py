maiordeidade = tot_homens = mulheres_menos20 = 0
while True:
    print(30 * '-')
    print('CADASTRE UMA PESSOA'.center(30))
    print(30 * '-')
    idade = int(input('Idade: '))
    if idade > 18:
        maiordeidade += 1

    sexo = ' '
    while sexo not in 'FM':
        sexo = input('Sexo [F/M]: ').upper().strip()[0]

    if sexo == 'F' and idade < 20:
        mulheres_menos20 += 1
    if sexo == 'M':
        tot_homens += 1
    print(' ')

    continua = ' '
    while continua not in 'SN':
        continua = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if continua == 'S':
        continue
    else: 
        print('== FIM DO PROGRAMA ==')
        print(' ')
        break
print(f'Total de pessoas com mais de 18 anos: {maiordeidade}')
print(f'Ao todo temos {tot_homens} homens cadastrados')
print(f'Temos {mulheres_menos20} mulheres com menos de 20 anos')