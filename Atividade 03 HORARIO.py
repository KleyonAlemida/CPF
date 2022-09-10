horario = input('Digite um horario (0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horario deve estar entra 0 e 23')
    else:
        if horario <= 11:
            print('Bom dia.')
        elif horario <= 12:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('Por favor digite um horario valido, entre 0 a 23.')

"""
Mais uma vez utilizamos a função -- isdigit --, para checar 

Objetivo da atividade foi fazer o usuario digitrar um horario de 0 a 23, e conforte a hora que ele digitar, será
impresso, as saudações conforme os horarios.
"""
