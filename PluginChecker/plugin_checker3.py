#plugin_checker3

#The goal of this script is to display all of the versions listed of all of the plugins that are on the plugin check page and the blocklist page
##############################################################
### block list # version # date ##  plugin # version # date###
#              #         #      ##         #         #     ###
#              #         #      ##         #         #     ###
#              #         #      ##         #         #     ###
#              #         #      ##         #         #     ###
#              #         #      ##         #         #     ###
##############################################################

from urllib2 import * 
import sys
import re

blocklisturl = "https://addons.mozilla.org/en-US/firefox/blocked/"
#list of only plugins in here
pluginlist=["Adobe Flash Player", 
			"Adobe Reader", 
			"Cisco Web Communicator", 
			"Java Runtime Environment",
			"QuickTime Plug-in",
			"RealPlayer",
			"Silverlight Plug-In",
			"VLC Multimedia Plug-in"]
blocklistKeyword =["Java", "Reader", "Communicator", "RealPlayer", "Silverlight", "VLC", "Quicktime"]

def getHtml(string):
	stuff = urlopen(string)
	html  = stuff.read()
	return html
def getDates(strg, sub, endsub, start, end):
	lists = []
	index = 0
	new = strg.find(sub, start, end)
	#newstart = string.find(sub,start, string.find(endsub, start, len(string))) + 17
	#newstart = string.find('<span class="dt">',start, string.find(endsub)) 
	print "string:"
	while index < len(strg):
		index = strg.find(sub, index)
		if index == -1:
			break
		end = strg.find(endsub, index)
		#print "first occurance:"
		#print strg[index+len(sub):end]
		if sub is '<a href="/en-US/firefox/blocked/i':
			lists.append(strg[index+len(sub)+3:end])
			index+=5
		else:	
			lists.append(strg[index+len(sub):end])
			index+=5	
	# remove extra > characters
	i=0
	while i < len(lists):
		lists[i].strip('<')
		i+=1
	return lists

def delPlugins(Namelist, Datelist, keywords):
	#remove all plugins that do not have a keyword
	newList = []

	i = 0
	while i < len(Namelist): 
			if (Namelist[i].find('p', 0, 2)) != -1:
				print "doing someting"
				newList.append({Namelist[i]:Datelist[i]})
			i+=1
	return newList
def printBlocklist(dict):
	return
	#vartype def check if its a dict
	#for key print  
	#for value print
	#http://stackoverflow.com/questions/5904969/python-how-to-print-a-dictionarys-key
	#for key, value in mydic.iteritems() :
    #print key, value

class Plugins(object):

    def __init__(self, name_string,date_string):
        self.Date = date_string
        self.name = name_string

    def apple(self):
        print "I AM CLASSY APPLES!"


def main():
	Html= getHtml(blocklisturl);
	start= Html.find('blocked-items')
	Dates = getDates(Html,'<span class="dt"', ':</span>', start, len(Html))
	#print type(Dates)
	print Dates
	Plugins_block = getDates(Html,'<a href="/en-US/firefox/blocked/', '</a', start, len(Html))	
	#print Plugins_block
	new = delPlugins(Plugins_block, Dates, blocklistKeyword)
	#print delPlugins(Plugins_block, Dates, blocklistKeyword)
	print new
	#call print blocklist
	for value in new.iteritems():
		print value 

	#get the plugin entries Json files? or way to get backend without  
	#final group by plugin version? 
	
		
			

	# iterate one at time for dates looks like this: 
		#newstart = Html.find('<span class="dt">',start, Html.find(':</span>', start, len(Html))) + 17
		#print Html[newstart:newstart+15]
		#newstart = newstart + 15
		#newstart = Html.find('<span class="dt">',newstart) + 17
		#print Html[newstart:newstart+15]


#boiler plate main
if __name__ == '__main__':
	main()