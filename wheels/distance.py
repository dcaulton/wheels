import datetime
import json
from time import sleep

import tornado.web
import wiringpi2

#quick and dirty script to test the distance between the front of the robot and the nearest obstacle
#invoke with sudo privs

class DistanceHandler(tornado.web.RequestHandler):
    response_arr = []

    @tornado.web.asynchronous
    def get(self):
        self.response_arr = []
        self.add_to_response("testing Relay {0}".format(datetime.datetime.now()))
        self.test_db()
        self.test_the_relay()
        self.add_to_response('Done Testing Relay')
        self.write(json.dumps(self.response_arr))

    def add_to_response(self, the_message):
        self.response_arr.append(the_message)

    def test_db(self):
        the_doc = self.application.db.info()
        self.add_to_response(json.dumps(the_doc))

    def test_the_relay(self):
	wiringpi2.wiringPiSetupGpio() # go with GPIO non-sequential numbers 
	wiringpi2.pinMode(12,1) # Set pin 12 to 1 ( OUTPUT )
	wiringpi2.pinMode(16,1) # Set pin 16 to 1 ( OUTPUT )
	wiringpi2.pinMode(20,1) # Set pin 20 to 1 ( OUTPUT )
	wiringpi2.pinMode(21,1) # Set pin 21 to 1 ( OUTPUT )

	wiringpi2.digitalWrite(12,1) #turn all pins on
	wiringpi2.digitalWrite(16,1) #turn all pins on
	wiringpi2.digitalWrite(20,1) #turn all pins on
	wiringpi2.digitalWrite(21,1) #turn all pins on

	self.add_to_response('turning on pin 32')
	wiringpi2.digitalWrite(12,0) # Write 0 (LOW) to pin 12.  This turns on the relay for motor 1
	sleep(2)
	wiringpi2.digitalWrite(12,1) # Write 1 (HIGH) to pin 12.  This disables the relay for motor 1
	self.add_to_response('turning on pin 36')
	wiringpi2.digitalWrite(16,0)
	sleep(2)
	wiringpi2.digitalWrite(16,1)
	self.add_to_response('turning on pin 38')
	wiringpi2.digitalWrite(20,0)
	sleep(2)
	wiringpi2.digitalWrite(20,1)
	self.add_to_response('turning on pin 40')
	wiringpi2.digitalWrite(21,0)
	sleep(2)
	wiringpi2.digitalWrite(21,1)
