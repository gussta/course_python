"""
>>  Validação de CPF <<

CPF = 168.995.350-09
"""
cpf = input("Digite o seu CPF: ")
for letra in cpf:
    if letra == ".":
        cpf = cpf.replace(".","")

    if letra == '-':
        cpf = cpf.replace('-','')


digitos_backup = cpf[9:]
cpf = cpf[:-2]


# Verificação de entrada !
while len(cpf) != 9 or cpf.isnumeric() == False:
    cpf = input("Digite corretamente os digitos do seu CPF: ")
    digitos_backup = cpf[9:]

cpf_backup = cpf

# Operações Matemáticas
aux = 10
soma_dg1 = 0
soma_dg2 = 0

for cont in cpf:
    cont = int(cont)
    soma_dg1 += (cont*aux)
    soma_dg2 += (cont*(aux+1))
    aux -= 1

primeiro_digito = 11 - (soma_dg1%11)
if primeiro_digito > 9:
    primeiro_digito = 0

segundo_digito = 11 - (soma_dg2%11)

# Formatação e validação das strings

cpf = '.'.join(cpf[i:i + 3] for i in range(0, len(cpf), 3))
cpf_backup = '.'.join(cpf_backup[i:i + 3] for i in range(0, len(cpf_backup), 3))

cpf_backup += '-'+digitos_backup


digitos_finais = '-'+str(primeiro_digito)+str(segundo_digito)
cpf += digitos_finais

if cpf_backup == cpf:
    print(f'Seu CPF é VALIDO!!!\nCPF digitado: {cpf_backup}\nCPF obtido: {cpf}')
else:
    print(f'CPF INVALIDO!!!!\nCPF digitado: {cpf_backup}\nCPF obtido: {cpf}')

