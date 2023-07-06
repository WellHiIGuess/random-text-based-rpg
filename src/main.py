from player import Player
import json


def main():
    player = Player()

    if player.data['name'] == '':
        print('There is no player data. Would you like to make a new game?')
        inp = input()
        inp = inp.lower()
        
        if inp.find('y') == 0:
            print('Enter character name:')
            inp = input()

            player.data['name'] = inp
        else:
            return

    # Game loop
    while True:
        inp = input()
        inp = inp.lower()

        if inp == 'quit':
            return
        elif inp == 'save':
            with open('player_data.json', 'w') as f:
                f.write(json.dumps(player.data))
        elif inp == '\c clear':
            player.data['name'] = ''
            player.data['health'] = 10
            player.data['max_health'] = 10
            player.data['strength'] = 1
            player.data['indurance'] = 1
            player.data['dextarity'] = 1
            player.data['vigor'] = 1
            player.data['intelligence'] = 1

            with open('player_data.json', 'w') as f:
                f.write(json.dumps(player.data))

    return


if __name__ == '__main__':
    main()
