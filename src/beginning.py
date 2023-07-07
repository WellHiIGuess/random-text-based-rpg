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
            print('What do you do next?')


def outside():
    print('\033c', end='')
    print('You exit the hut. You look around and you see a waste land. There are piles of rubble where houses used to be before chaos befell the land. You never had neighbors but if you did they would live in those lots. You\'re father once new the people who made them their steads. Now he is tending to the small farm in front of the hut. Before you leave you should talk to him. What do you do?')

    while (True):
        inp = input()
        inp = inp.lower()
