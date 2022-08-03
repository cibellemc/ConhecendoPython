# só aceitar M ou F, caso contrário pedir de novo
sexo = input('Informe o sexo da pessoa: [F/M] ').upper()

# Se vc usar o OR, basta uma das condicoes estarem diferentes para ele entrar no processo do while.
# Ele compara M com M (Iguais) ou M com F (Diferente), como um das condicoes esta como diferente, vai pro loop
# poderia ser while not sexo == 'F' and not sexo == 'M':

while 'F' != sexo != 'M':
    print('Por favor, informe uma opção válida.')
    sexo = input('Informe o sexo da pessoa: [F/M] ').upper()
print(f'Sexo {sexo} registrado.')
