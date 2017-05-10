import requests
import urllib.parse


PLAYER_BASE_URL = "https://en.lichess.org/api/user/"


class Player(object):

    def __init__(self, username):
        self.username = username
        self.player_url = urllib.parse.urljoin(PLAYER_BASE_URL, username)

        r = requests.get(self.player_url)

        if r.status_code == 404:
            raise KeyError('User {} not found'.format(self.username))

    def __str__(self):
        text = 'Player: {}; URL: {}'.format(self.username, self.player_url)
        return text

    def get_total_games(self):
        r = requests.get(self.player_url)
        total = r.json()["count"]["all"]
        return total


if __name__ == '__main__':
    with open('local_data.txt', 'r') as f:
        username = f.readline()
        username = username.strip()

    a_player = Player(username)
    total_games = a_player.get_total_games()

    print("{} has played a total of {} games so far".format(username, total_games))
    print(a_player)

