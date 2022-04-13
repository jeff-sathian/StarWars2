import pymongo
import requests
from pprint import pprint


def get_data(url):
    i = 0
    full_data =[]

    while True:
        i += 1
        info = requests.get(url + "/?page={}".format(i)).json()
        if info['next'] == None:
            info = requests.get(url + "/?page={}".format(i)).json()
            for record in range(len(info['results'])):
                full_data.append(info['results'][record])
            break
        else:
            info = requests.get(url + "/?page={}".format(i)).json()
            for record in range(len(info['results'])):
                full_data.append(info['results'][record])
    return full_data

starships_data = get_data("https://swapi.dev/api/starships")

for i in starships_data:
    print (i)
# url="https://swapi.dev/api/starships"
# info = requests.get(url + "/?page={}".format(4)).json()
# info2=requests.get('https://swapi.dev/api/starships/?page=4').json()
# if info2['next'] == None:
#     print("what?")
# else:
#     print("huh?")
#print(info['next'])