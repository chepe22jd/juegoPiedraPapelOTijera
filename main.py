import random

options = ('piedra', 'papel', 'tijera')
computer_win =0
user_win = 0

round = 1

while True:
    print('*' * 10)
    print('ROUND', round)
    print('*' * 10)

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    computer_option = random.choice(options)
    print('Opcion de la computadora => '+ computer_option)
    if not user_option  in options:
        print('Informacion no valida')
    elif user_option == computer_option:
        print('empate')
    elif user_option == 'piedra' and computer_option =='papel':
        print('Gana la computadora')
        computer_win += 1
    elif user_option == 'papel' and computer_option == 'piedra':
        print('Gana el usario')
        user_win += 1
    elif user_option == 'tijera' and computer_option == 'piedra':
        print('Gana la computadora')
        computer_win += 1
    elif user_option == 'piedra' and computer_option == 'tijera':
        print('Gana el usuario')
        user_win += 1
    elif user_option == 'tijera' and computer_option == 'papel':
        print('Gana el usuario')
        user_win += 1
    elif user_option == 'papel' and computer_option == 'tijera':
        print('Gana la computadora')
        computer_win += 1

    print('Usuario : ', user_win, 'vs Computadora: ', computer_win)
    round += 1

    if user_win == 3:
        print('Usuario Gano')
        break
    elif computer_win == 3:
        print('Computadora gano')
        break

