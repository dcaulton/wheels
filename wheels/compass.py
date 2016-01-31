import datetime
import json

import tornado.web
import wiringpi2


# the compass is in single read mode right now.  I have some work to do with 
#  writing to it to set its modes.  And if I recall correctly the results come back as
#  twos complement so I will need to massage it further

class CompassHandler(tornado.web.RequestHandler):
    response_arr = []

    @tornado.web.asynchronous
    def get(self):
        self.response_arr = []
        self.add_to_response("testing Compass {0}".format(datetime.datetime.now()))
        self.test_the_compass()
        self.add_to_response('Done Testing Compass')
        self.write(json.dumps(self.response_arr))

    def add_to_response(self, the_message):
        self.response_arr.append(the_message)

    def test_the_compass(self):
	fh = wiringpi2.wiringPiI2CSetup(0x1e)
	result_arr = []
	for i in range(1,1000):
	    result_arr.append(wiringpi2.wiringPiI2CRead(fh))
	self.add_to_response(str(result_arr))
