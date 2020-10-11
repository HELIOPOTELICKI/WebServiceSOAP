from pymongo import MongoClient


def mongoConnect():
    client = MongoClient(
        "mongodb+srv://HelioPotelicki:123@soapdb.scfky.mongodb.net/SOAPDB?retryWrites=true&w=majority"
    )
    db = client['SOAPDB']
    return db


def addAlbum(db, album):
    db = db['Albuns']
    albumID = db.insert_one(album).inserted_id
    return albumID


def getAllAlbuns(db):
    retorno = []
    for Albuns in db['Albuns'].find():
        retorno.append(Albuns)
    return retorno
