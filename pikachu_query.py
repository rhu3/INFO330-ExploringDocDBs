# pikachu_query
from pymongo import MongoClient

def pikachu_query():
    mongoClient = MongoClient("mongodb://localhost/pokemon")
    pokemonDB = mongoClient['pokemondb']
    pokemonColl = pokemonDB['pokemon_data']
    pikachu = pokemonColl.find({"name": "Pikachu"})
    return list(pikachu)

if __name__ == "__main__":
    result = pikachu_query()
    print(result)
