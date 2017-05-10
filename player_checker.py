import requests
import urllib.parse
import datetime

PLAYER_BASE_URL = "https://en.lichess.org/api/user/"


class Player(object):
    """
    Gives basic player information
    """

    def __init__(self, username):
        """
        Creates new Player instance

        Args:
            username (str): Username of player in Lichess
        """
        self.username = username
        self.player_url = urllib.parse.urljoin(PLAYER_BASE_URL, username)

        r = requests.get(self.player_url)

        if r.status_code == 404:
            raise KeyError('User {} not found'.format(self.username))

    def __str__(self):
        """
        Returns:
            str: Basic information about the player
        """
        text = 'Player: {}; URL: {}'.format(self.username, self.player_url)
        return text


    def __repr__(self):
        return self.__str__()


    def get_total_games(self):
        """
        Returns:
            int: Number of games played in total
        """
        r = requests.get(self.player_url)
        total = r.json()["count"]["all"]
        return total

    def get_last_games(self, count):
        suffix = "/games?nb={}".format(count)
        r = requests.get(self.player_url+suffix)
        return r.json()



def get_username_from_file(file_name='local_data.txt'):
    """
    Reads plain text file to get username

    Args:
        file_name (str): Name or path of text file

    Returns:
        str: username from file
    """
    with open(file_name, 'r') as f:
        username = f.readline()
        username = username.strip()
    return username


if __name__ == '__main__':
    username = get_username_from_file()

    a_player = Player(username)
    total_games = a_player.get_total_games()
    games = a_player.get_last_games(10)

    print("{} has played a total of {} games so far".format(username, total_games))
    print(a_player)

    for g in games['currentPageResults']:
        ts = g['createdAt']//1000 # it's in miliseconds
        dt = datetime.datetime.fromtimestamp(ts)
        print(dt.strftime("%A, %d. %B %Y %I:%M%p"))
