from player import Player


def menu(player: Player):
    print('\033c', end='')
    print('> ITEMS  > EQUIPMENT  > EXIT')

    def items():
        print(player.data['inventory'])

    while (True):
        inp = input()
        inp = inp.lower()

        if 'item' in inp:
            items()
