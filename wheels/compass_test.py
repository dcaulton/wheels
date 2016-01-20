import wiringpi2

#quick and dirty command line script to test the 3 axis compass which is on i2c
# the compass is in single read mode right now.  I have some work to do with 
#  writing to it to set its modes.  And if I recall correctly the results come back as
#  twos complement so I will need to massage it further

fh = wiringpi2.wiringPiI2CSetup(0x1e)
result_arr = []
for i in range(1,1000):
    result_arr.append(wiringpi2.wiringPiI2CRead(fh))
print result_arr
