import json

from player import Player


def main():
    data = json.loads(open('./data.json', 'r').read())
    player = Player()
    player.betRequest(data)


if __name__ == '__main__':
    main()
