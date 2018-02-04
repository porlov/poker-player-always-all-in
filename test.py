import json

from player import Player


def main():
    data = json.loads(open('./data.json', 'r').read())
    player = Player()
    result = player.betRequest(data)
    print result


if __name__ == '__main__':
    main()
