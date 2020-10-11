from spyne import Application, ServiceBase, Unicode, rpc
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11
import mongo as mg
global db


class Methods(ServiceBase):
    @rpc(_returns=Unicode)
    def addAlbumInData(self):
        albumID = "\nnot Implemented dude"
        return albumID

    @rpc(_returns=Unicode)
    def getAlbuns(self):
        return mg.getAllAlbuns(db)


application = Application(services=[Methods],
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