import requests
r = requests.get('https://en.lichess.org/api/user/MetaEmber')
total = r.json()["count"]["all"]
print("Charles has played a total of {} games so far".format(total))


