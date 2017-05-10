import requests

with open('local_data.txt', 'r') as f:
    username = f.readline()
    username = username.strip()

url = "https://en.lichess.org/api/user/"+username


r = requests.get(url)
total = r.json()["count"]["all"]

print("{} has played a total of {} games so far".format(username,total))


