import requests

s = requests.session()
id_art, amount = [int(x) for x in input().split(' ')]

# print(str(id_art) + "---" + str(amount))

for i in range(0, amount):
    s.get("http://localhost:8000/article/addlike/{0}/".format(id_art))
    s.cookies.clear()
