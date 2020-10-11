import mongo as mg
import pymongo as pym
from bson.objectid import ObjectId
#=======================
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
#=======================
transport = Transport(cache=SqliteCache())
client = Client('http://localhost:8000/?wsdl', transport=transport)

# TODO -> ls retornando TypeError: 'NoneType' object is not iterable
ls = client.service.getAlbuns()
print 'RETORNO DE LS ->' + ls

#db = mg.mongoConnect()
#ls = mg.getAllAlbuns(db)
for i in range(len(ls)):
    print '\n====================================='
    print 'ID:', ls[i]["_id"]
    print 'Titulo:', ls[i]["titulo"]
    print 'Artista:', ls[i]["artista"]
    print 'Gravadora:', ls[i]["gravadora"]
    print 'Ano:', ls[i]["ano"]
"""
=======================================================================================================================
class ExampleService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def slow_request(self, request_id):
        time.sleep(1)

        return u'Request: %s' % request_id
=======================================================

album = {
    "titulo": "Kamikaze",
    "artista": "Eminem",
    "gravadora": "Aftermath",
    "ano": 2018
}
objectID = mg.addAlbum(db, album)
print objectID
"""