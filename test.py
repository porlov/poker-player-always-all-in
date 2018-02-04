from player import Player

def main():
    json = open('./data.json', 'r').read()
    player = Player()
    result = player.betRequest(json)
    print result


if __name__ == '__main__':
    main()