from player import Player


def beginning(player: Player):
    print('\033c', end='')
    print('This land used to be a land of peace. Now it is frought with peril an monsters. The royals no longer care about their people instead they throw the people to the monsters as sacrifices. But from this peril will come heros, warriors who will rise up. You must never lose hope. Take your rightfull place to the throne even it is kills you!')
    print('\n\nYou wake up in your father\'s wooden hut. You have recently come of age and are able to go out into the world. There are tools in the closet you can take before you leave. What do you do?')

    sword_taken = False

    while (True):
        inp = input()
        inp = inp.lower()

        if 'leave' in inp:
            outside()
        elif 'exit' in inp:
            outside()
        elif 'outside' in inp:
            outside()
        elif 'closet' in inp:
            if not sword_taken:
                print('Inside the closet you find a sword. You take it.')
                player.data['inventory'].append('sword')
            else:
                print('Inside the closet you find nothing.')


def outside():
    pass

