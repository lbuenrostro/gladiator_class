import core
import time


def moves():
    print('\n[A]ttack')
    print('[K]amehameha')
    print('[H]eal')
    print('[I]ncrease_rage')
    # print('[S]pirit_bomb\n')


def main():
    input('----------FIGHT BEGIN---------')

    Gladiator_1 = core.Gladiator('Gladiator_1', 100, 0, 7, 20)
    Gladiator_2 = core.Gladiator('Gladiator_2', 100, 0, 7, 20)

    while True:
        print('\n{}\n{}'.format(Gladiator_1, Gladiator_2))
        time.sleep(1)

        moves()
        time.sleep(1)

        # THIS WILL BE Gladiator_1'S Turn
        if Gladiator_1.is_dead():
            print('Gladiator_1 is Dead')
            exit()

        print('<<<<<Gladiator_1>>>>>')
        answer = input('Make a move:\n').strip().upper()

        if answer == 'A':
            Gladiator_1.attack(Gladiator_2)

        elif answer == 'k':
            Gladiator_1.kamehameha(Gladiator_2)

        elif answer == 'H':
            Gladiator_1.heal()

        elif answer == 'I':
            Gladiator_1.increase_rage()

        # elif answer == 'S':
        #     Gladiator_1.spirit_bomb(Gladiator_2)

        if Gladiator_2.is_dead():
            print('Gladiator_2 Your Dead!')
            exit()

        # THIS WILL BE Gladiator_2'S turn
        print('<<<<<Gladiator_2>>>>>')
        answer = input('Make a move:\n').strip().upper()

        if answer == 'A':
            Gladiator_2.attack(Gladiator_1)

        elif answer == 'k':
            Gladiator_2.kamehameha(Gladiator_1)

        elif answer == 'H':
            Gladiator_2.heal()

        elif answer == 'I':
            Gladiator_2.increase_rage()

        # elif answer == 'S':
        #     Gladiator_2.spirit_bomb(Gladiator_1)


if __name__ == '__main__':
    main()