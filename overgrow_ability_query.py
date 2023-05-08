# overgrow_ability_query.py
from pymongo import MongoClient

def overgrow_query():
    mongoClient = MongoClient("mongodb://localhost/pokemon")
    pokemonDB = mongoClient['pokemondb']
    pokemonColl = pokemonDB['pokemon_data']
    overgrow_pokemon = pokemonColl.find({"abilities": "Overgrow"})
    return list(overgrow_pokemon)

if __name__ == "__main__":
    result = overgrow_query()
    print(result)
