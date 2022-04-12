import pymongo
import requests
from pprint import pprint

client = pymongo.MongoClient()
db = client["starwars"]
db.starships.drop()


starships=db["starships"] #creating a collection for starships
print(db.list_collection_names())

def get_data(url):
    return requests.get(url).json()

json_return = get_data("https://swapi.dev/api/starships/")
json_return2 = get_data('https://swapi.dev/api/starships/?page=2')
json_return3 = get_data('https://swapi.dev/api/starships/?page=3')
json_return4 = get_data('https://swapi.dev/api/starships/?page=4')


def insert_data(json_file):
    for i in json_file['results']:
        db.starships.insert_one(i)
a=insert_data(json_return)
b=insert_data(json_return2)
c=insert_data(json_return3)
d=insert_data(json_return4)

print(db.list_collection_names())
#looping through all starship pages
#(couldnt figure out)

def get_id(url): #given a pilot url will produce the id of the pilot
    pilot = requests.get(url)
    return pilot["_id"]

pilots = db.starships.find({"pilots":{"$ne" : []}},{"pilots":1,"_id":0}) #finding all entries where pilots is not empty
pilot_list =[]
for p in pilots:
    pilot_list.append(p)
# pprint(pilot_list[0].values())

#pprint(pilot_list)
# print(pilot_list)
counter = 0
pilot2=[]
for ele in pilot_list: #produces api pilot values of the dictionary for each starship
    #pprint(pilot_list[counter].values())
    pilot2.append(pilot_list[counter].values())
    counter += 1
pprint(pilot2[0])

pilot3=[]
for i in pilot2[0]:
    pilot3.append(i)

# def generate_id:
print(pilot2)





#
# def replace_url_with_id(url):
#     db.starships.update_one({"pilots":{"$ne":""}},{"$set":{"$pilots":get_id(url)}})



