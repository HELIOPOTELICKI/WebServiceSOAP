from pymongo import MongoClient


def mongoConnect():
    client = MongoClient(
        "mongodb+srv://HelioPotelicki:123@soapdb.scfky.mongodb.net/SOAPDB?retryWrites=true&w=majority"
    )
    db = client['SOAPDB']
    return db


def addAlbum(db, album):
    collection = db['Albuns']
    albumID = collection.insert_one(album).inserted_id
    return albumID
