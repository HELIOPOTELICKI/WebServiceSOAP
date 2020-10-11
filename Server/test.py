import mongo as mg
import pymongo as pym
from bson.objectid import ObjectId

db = mg.mongoConnect()

album = {
    "titulo": "The Gereg",
    "artista": "The HU",
    "gravadora": "Papa Roach",
    "ano": 2019
}

print mg.getAllAlbuns(db)
#db = db.Albuns
#objectID = mg.addAlbum(db, album)
"""
class ExampleService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def slow_request(self, request_id):
        time.sleep(1)

        return u'Request: %s' % request_id
"""