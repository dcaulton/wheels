import wiringpi2

#quick and dirty command line script to test the gps antenna

serial = wiringpi2.serialOpen('/dev/ttyAMA0',9600)
get_array = []
letter_array = []
for i in range(1,1000):
    get_array.append(wiringpi2.serialGetchar(serial))

for x in get_array:
    letter_array.append(chr(x))

letter_string = ''.join(letter_array)

#print get_array
#print letter_array
print letter_string

#for adafruit ultimate gps breakout:
#connect rpi tx to gps rx, rpi rx to gps tx, and give the gps 3.3v and a ground
#when we have a fix on enough satellites here is what we get
#,3,31,10,12,22,,,,,,,,,2.52,2.33,0.96*0A
#$GPGSV,2,1,07,22,82,266,14,10,55,137,31,31,50,208,31,12,22,057,16*7F
#$GPGSV,2,2,07,24,06,045,,43,,,,25,,,18*46
#$GPRMC,194033.000,A,4143.6242,N,08756.9917,W,0.28,269.06,200116,,,A*7F
#$GPVTG,269.06,T,,M,0.28,N,0.52,K,A*3B
#$GPGGA,194034.000,4143.6242,N,08756.9918,W,1,04,2.33,197.1,M,-34.0,M,,*52
#$GPGSA,A,3,31,10,12,22,,,,,,,,,2.52,2.33,0.96*0A
#$GPRMC,194034.000,A,4143.6242,N,08756.9918,W,0.27,304.42,200116,,,A*72
#$GPVTG,304.42,T,,M,0.27,N,0.50,K,A*3C
#$GPGGA,194035.000,4143.6243,N,08756.9919,W,1,03,3.18,197.1,M,-34.0,M,,*5C
#$GPGSA,A,2,31,10,22,,,,,,,,,,3.34,3.18,1.00*0F
#$GPRMC,194035.000,A,4143.6243,N,08756.9919,W,0.38,320.87,200116,,,A*72
#$GPVTG,320.87,T,,M,0.38,N,0.71,K,A*3E
#$GPGGA,194036.000,4143.6244,N,08756.9920,W,1,03,3.18,197.1,M,-34.0,M,,*52
#$GPGSA,A,2,31,10,22,,,,,,,,,,3.34,3.18,1.00*0F
#$GPRMC,194036.000,A,4143.6244,N,08756.9920,W,0.51,331.49,200116,,,A*71
#$GPVTG,331.49,T,,M,0.51,N,0.95,K,A*39
#$GPGGA,194037.000,4143.6245,N


# heres what we get from the parallax gps breakout:
#$GPRMC,195211.00,V,,,,,,,200116,,,N*76
#$GPVTG,,,,,,,,,N*30
#$GPGGA,195211.00,,,,,0,00,99.99,,,,,,*69
#$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30
#$GPGSV,2,1,05,14,68,034,18,18,18,138,22,22,82,227,,25,35,094,*71
#$GPGSV,2,2,05,31,56,211,26*4B
#$GPGLL,,,,,195211.00,V,N*45
#$GPRMC,195212.00,V,,,,,,,200116,,,N*75
#$GPVTG,,,,,,,,,N*30
#$GPGGA,195212.00,,,,,0,00,99.99,,,,,,*6A
#$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30
#$GPGSV,2,1,05,14,68,034,17,18,18,138,22,22,82,227,,25,35,094,*7E
#$GPGSV,2,2,05,31,56,211,26*4B
#$GPGLL,,,,,195212.00,V,N*46
#$GPRMC,195213.00,V,,,,,,,200116,,,N*74
#$GPVTG,,,,,,,,,N*30
#$GPGGA,195213.00,,,,,0,00,99.99,,,,,,*6B
#$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30
#$GPGSV,2,1,05,14,68,034,18,18,18,138,21,22,82,227,,25,35,094,*72
#$GPGSV,2,2,05,31,56,211,26*4B
#$GPGLL,,,,,195213.00,V,N*47
#$GPRMC,195214.00,V,,,,,,,200116,,,N*73
#$GPVTG,,,,,,,,,N*30
#$GPGGA,195214.00,,,,,0,00,99.99,,,,,,*6C
#$GPGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*30
#$GPGSV,2,1,05,14,68,034,18,18

