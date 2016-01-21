import wiringpi2
from time import sleep


#quick and dirty command line script to test the relay connections.
#invoke with sudo privs
#when all is well, relays 1, 2, 3 and 4 will turn on, then off, in sequence

def test_the_relay():
    wiringpi2.wiringPiSetupGpio() # go with GPIO non-sequential numbers 
    wiringpi2.pinMode(12,1) # Set pin 12 to 1 ( OUTPUT )
    wiringpi2.pinMode(16,1) # Set pin 16 to 1 ( OUTPUT )
    wiringpi2.pinMode(20,1) # Set pin 20 to 1 ( OUTPUT )
    wiringpi2.pinMode(21,1) # Set pin 21 to 1 ( OUTPUT )

    wiringpi2.digitalWrite(12,1) #turn all pins on
    wiringpi2.digitalWrite(16,1) #turn all pins on
    wiringpi2.digitalWrite(20,1) #turn all pins on
    wiringpi2.digitalWrite(21,1) #turn all pins on
    print 'turning on pin 32'
    wiringpi2.digitalWrite(12,0) # Write 0 (LOW) to pin 12
    sleep(2)
    wiringpi2.digitalWrite(12,1)
    print 'turning on pin 36'
    wiringpi2.digitalWrite(16,0)
    sleep(2)
    wiringpi2.digitalWrite(16,1)
    print 'turning on pin 38'
    wiringpi2.digitalWrite(20,0)
    sleep(2)
    wiringpi2.digitalWrite(20,1)
    print 'turning on pin 40'
    wiringpi2.digitalWrite(21,0)
    sleep(2)
    wiringpi2.digitalWrite(21,1)

