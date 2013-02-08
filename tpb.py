from BeautifulSoup import BeautifulSoup
from subprocess import call
from array import array
import urllib
import datetime
import unicodedata

f = urllib.urlopen("http://thepiratebay.se/browse/200/0/7")
data = f.read()

soup = BeautifulSoup(data)

links = soup.findAll(name = "a", attrs = {"class" : "detLink"})	

torrents = []
i = 0

for link in links:
	torrent = link.contents[0]
	td = link.parent.parent.parent.findAll(name = "td")
	seed = td[2].contents[0]
	leech = td[3].contents[0]
	magnet = link.parent.parent.findAll(name = "a")[1]['href']
	torrents.append(magnet)
	print "[%i] %s : %s/%s" % (i, link.contents[0].string, seed, leech)
	i = i + 1
	
print "Download some torrents?"
val = raw_input('Torrent number : ')

#call (["transmission-remote", "-w", " /home/pi/media ", " -a", torrents[int(val)]])
call (["./add_torrent.sh", torrents[int(val)]])
#call (["echo", "-w /home/pi/media/-a "+torrents[int(val)], "> out"])



