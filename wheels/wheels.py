import json

import couchdb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from relay import RelayHandler

define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r"/", IndexHandler),
            (r"/relay/*", RelayHandler)
        ]
        self.set_up_db()
        tornado.web.Application.__init__(self, handlers, debug=True)

    def set_up_db(self):
	couch = couchdb.Server()
	try:
	   self.db = couch['wheels']
	except couchdb.http.ResourceNotFound as e:
	    couch.create('wheels')
	    self.db = couch['wheels']

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.test_db()
        self.write('Wheels main')

    def test_db(self):
        the_doc = self.application.db.info()
        self.write(json.dumps(the_doc))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
