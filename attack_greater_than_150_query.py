
# attack_greater_than_150_query.
from pymongo import MongoClient

def attack_gt_150_query():
    mongoClient = MongoClient("mongodb://localhost/pokemon")
    pokemonDB = mongoClient['pokemondb']
    pokemonColl = pokemonDB['pokemon_data']
    strong_pokemon = pokemonColl.find({"attack": {"$gt": 150}})
    return list(strong_pokemon)

if __name__ == "__main__":
    result = attack_gt_150_query()
    print(result)
