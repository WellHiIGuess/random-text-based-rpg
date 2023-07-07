from __global__ import player


def plains():
    player.data['area'] = 'plains'
    print('\033c', end='')
    print('You walk until you come upon the plains. You now can access the menu at any time. There you can manage your inventory and equip your weapon. You can also choose to explore.')

    while True:
        pass
