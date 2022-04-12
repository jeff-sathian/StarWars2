import pymongo
import requests
from pprint import pprint

client = pymongo.MongoClient()
db = client["starwars"]
db.starships.drop()


starships=db["starships"] #creating a collection for starships
print(db.list_collection_names())

json_return = requests.get("https://swapi.dev/api/starships/").json() #getting starships data from api
json_return2 = requests.get('https://swapi.dev/api/starships/?page=2').json()
json_return3 = requests.get('https://swapi.dev/api/starships/?page=3').json()
json_return4 = requests.get('https://swapi.dev/api/starships/?page=4').json() #hard coded! need to automate!
#pprint(json_return2)

def insert_data(input):
    for i in input['results']:
        db.starships.insert_one(i)
a=insert_data(json_return)
b=insert_data(json_return2)
c=insert_data(json_return3)
d=insert_data(json_return4)

# for i in json_return["results"]: #adds each record into the starships collection
#     db.starships.insert_one(i)
print(db.list_collection_names())
print(len(json_return["next"]))
#looping through all starship pages


starb=db.starships.find({})
for i in starb:
    print(i)


char =db.characters.find({}).limit(2)
for m in char:
    pprint(m)


pilots = db.starships.find({"pilots":{"$ne" : []}},{"pilots":1})
for p in pilots:
    print(p)