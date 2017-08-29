import core


def moves():
    print('Attack: random number between damage high and damage low')
    print('Heal: takes ten rage to add five HP')


def main():
    input('----------FIGHT BEGIN---------')
    liza = core.Gladiator('liza', 100, 0, 7, 20)
    mac = core.Gladiator('mac', 100, 0, 7, 20)
    print('{}\n{}\n'.format(liza, mac))

    # gladiator_1 = core.Gladiator('liza', 100, 25, 16, 50)
    # gladiator_2 = core.Gladiator('Jackie', 100, 25, 16, 50)
    # print('{}\n{}'.format(gladiator_1, gladiator_2))

    # sword = core.Moves('sword', 25)
    # kick = core.Moves('kick', 15)
    # punch = core.Moves('Punch', 20)
    # poke = core.Moves('poke', 10)
    # kamehameha = core.Moves('kamehameha', 30)

    # print('\n--{}\n--{}\n--{}\n--{}\n--{}'.format(sword, kick, punch, poke,
    #                                               kamehameha))

    # while True:
    #     choice = input('Make a move:\t')


if __name__ == '__main__':
    main()