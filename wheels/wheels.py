import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import relay_test

define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Wheels main')

class RelayTestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Testing Relay')
        relay_test.test_the_relay()
        self.write('Done Testing Relay')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
                                      (r"/", IndexHandler),
                                      (r"/relay", RelayTestHandler),
                                  ]
          )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
