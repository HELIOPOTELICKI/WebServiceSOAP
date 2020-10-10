from spyne import Application, ServiceBase, Unicode, rpc
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11
import mongo as mg
import time
global db
import re
import inspect
"""
class ExampleService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def slow_request(self, request_id):
        time.sleep(1)

        return u'Request: %s' % request_id
"""


class Album(ServiceBase):
    def __init__(self, titulo, artista, gravadora, ano):
        self.titulo = titulo
        self.artista = artista
        self.gravadora = gravadora
        self.ano = ano

    @rpc(Unicode, _returns=Unicode)
    def addAlbumInData(self, db):
        newAlbum = {
            "titulo": self.titulo,
            "artista": self.artista,
            "gravadora": self.gravadora,
            "ano": self.ano
        }
        albumID = mg.addAlbum(db, newAlbum)
        return albumID


#db = mg.mongoConnect()
#piranha = Album("vagina", "cu", "chupa", 2020)
#piranha.addAlbumInData(db)

application = Application(services=[Album],
                          tns='http://tests.python-zeep.org/',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

application = WsgiApplication(application)

if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server

    try:
        db = mg.mongoConnect()
    except:
        print 'Error connecting to the database'

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, application)
    server.serve_forever()