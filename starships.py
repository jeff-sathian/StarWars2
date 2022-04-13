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



def get_id2(arrayofurls): #given a pilot url will produce the name of the pilot
    arrayofids = []
    for ele in arrayofurls: #loops through all api links
        pilot = requests.get(ele).json()
        name = pilot["name"]
        id = db.characters.find({"name": name}, {"_id":1}) #searches for pilot name in characters collection
        ids = []
        for item in id:
            ids.append(item["_id"]) #gets information from cursor object
            arrayofids.append(ids[0])
    return arrayofids

# test = get_id2(['https://swapi.dev/api/people/10/','https://swapi.dev/api/people/58/']) #test if function works
# print(test)
#print(get_id2(['https://swapi.dev/api/people/13/', 'https://swapi.dev/api/people/14/', 'https://swapi.dev/api/people/25/', 'https://swapi.dev/api/people/31/']))


stars = db.starships.find({})
for i in stars:
    if i['pilots'] == []:#if no pilots no ids to update
        continue
    else:
        get_id2(i['pilots']) #retrieves pilots character id
        db.starships.update_one({"pilots":i['pilots']},{"$set":{"pilots":get_id2(i['pilots'])}}) # finds pilot record that matches the for loop and updates it to the object id

stars2 = db.starships.find({})
for i in stars2: #checking if object ids were correctly updated
    print(i)
















#Archive/ not used code:

# def get_id(url): #given a pilot url will produce the name of the pilot
#     pilot = requests.get(url).json()
#     name = pilot["name"]
#     id = db.characters.find({"name": name}, {"_id":1}) #searches for pilot name in characters collection
#     ids = []
#     for ele in id:
#         ids.append(ele["_id"]) #gets information from cursor object
#     return ids[0]

# pilots = db.starships.find({"pilots":{"$ne" : []}},{"pilots":1,"_id":0}) #finding all entries where pilots is not empty
# pilot_list =[]
# for p in pilots:
#     print(p)
    #pilot_list.append(p)
# pprint(list(pilot_list[0].values()))
# pprint(pilot_list[0].values())

#pprint(pilot_list)
# print(pilot_list)
# counter = 0
# pilot2=[]
# for ele in pilot_list: #produces api pilot values of the dictionary for each starship
#     #pprint(pilot_list[counter].values())
#     pilot2.append(list(pilot_list[counter].values()))
#     counter += 1
# #pprint(pilot2[0][0][2])
#
# pilot3=[]
# for i in pilot2[0]:
#     pilot3.append(i)



# all_records= db.starships.find({})
# for i in all_records:
#     pprint(i)

# def generate_id:
#print(pilot2)





#
# def replace_url_with_id(url):
#     db.starships.update_one({"pilots":{"$ne":""}},{"$set":{"$pilots":get_id(url)}})



