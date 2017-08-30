import core
import time


def moves():
    print('\n[A]ttack: random number between damage high and damage low')
    print(
        '[K]amehameha: a lot of hit points for a lot of range and energy attack'
    )
    print('[H]eal: takes ten rage to add five HP\n')


def main():
    input('----------FIGHT BEGIN---------')

    liza = core.Gladiator('liza', 100, 0, 7, 20)
    mac = core.Gladiator('mac', 100, 0, 7, 20)

    while True:
        print('\n{}\n{}'.format(liza, mac))
        time.sleep(1)

        answer = moves()
        time.sleep(1)

        # THIS WILL BE LIZA'S TURN
        print('Liza\'s Turn:')
        answer = input('Make a move:\n').strip().upper()

        if answer == 'A':
            liza.attack(mac)

        elif answer == 'k':
            liza.kamehameha(mac)

        elif answer == 'H':
            liza.heal()

        # THIS WILL BE MAC'S TURN
        print('Mac\'s Turn:')
        answer = input('Make a move:\n').strip().upper()

        if answer == 'A':
            mac.attack(liza)

        elif answer == 'k':
            mac.kamehameha(liza)

        elif answer == 'H':
            mac.heal()


if __name__ == '__main__':
    main()