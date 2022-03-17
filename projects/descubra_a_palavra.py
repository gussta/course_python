# Caça-palavras estilo TRELLO

trello = 'perfume'
chances = 3
digitadas = []


print(f'Bem vindo ao caça palavras!!!\nVocê terá {chances} chances para descobrir a palavra do dia!!!\n')

while True:
    print()
    letra = input('Digite uma letra: ')

    # Caso a pessoa tente digitar mais de uma letra!
    if len(letra) > 1:
        print('Ahhhh isso não valtee, digite apenas uma letra!!')
        continue

    digitadas.append(letra) #Adiciona a letra na lista digitada

    #Verificando se a letra está na palavra
    if letra in trello:
        print(f'A letra {letra} existe na palavra')

    else:
        print('A letra não está contida na palavra')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in trello:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta

        else:
            secreto_temporario += '*'

    if secreto_temporario == trello:
        print(f'Parabéns!! Você acertou a palavra correta!\n\n')
        break

    else:
        print(f'A palavra secreta está assim: {secreto_temporario}  ')

    if letra not in trello:
            chances -= 1
            if chances == 0:
                print(print(f'\n\nVocê falhou!!! A palavra '))
                break
            print(f'Você ainda tem {chances} chances.')