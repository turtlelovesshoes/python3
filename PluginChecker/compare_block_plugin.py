#Compare pluginlist to blocklist

# This will be the part that retreives the list of plugin verions from plugins.mozilla.org page
# https://plugins.mozilla.org/en-us/plugins_list.json
# https://docs.python.org/2/library/json.html

#libraries
import json 
import urllib
from urllib2 import * 
import sys
import collections

#globals
pluginurl = "https://plugins.mozilla.org/en-us/plugins_list.json" 
plugin_keys= ['adobe-flash-player',
	"adobe-reader",
	'CiscoWebCommunicatorplugincheck',
	'java-runtime-environment',
	'apple-quicktime',
	'realplayer',
	'microsoft-silverlight',
	'videolan-vlc']

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
blocklistKeyword =["Java", "Reader", "Cisco Web Communicator", "RealPlayer", "Silverlight", "VLC", "Quicktime"]


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
	#print "string:"
	while index < len(strg):
		index = strg.find(sub, index)
		if index == -1:
			break
		end = strg.find(endsub, index)
		#print "first occurance:"
		#print strg[index+len(sub):end]
		if sub is '<a href="/en-US/firefox/blocked/i':
			lists.append(strg[index+len(sub):end])
			index+=5
		else:	
			lists.append(strg[index+len(sub)+5:end])
			index+=5
	return lists

def getLatest(pluginname,Plugin_json):
	#check if its a valid key:
	store = {}
	for s in plugin_keys:
		if(s == 'adobe-flash-player') or (s == "adobe-reader"):
			print "Name" + " " +Plugin_json["plugins"][s]["display_name"]
			print "Latest Windows and Mac" + " " + Plugin_json["plugins"][s]["versions"]["win"]["latest"][0]["version"]
			print "Latest Linux" + " " + Plugin_json["plugins"][s]["versions"]["lin"]["latest"][0]["version"]
			store[Plugin_json["plugins"][s]["display_name"]] = Plugin_json["plugins"][s]["versions"]["win"]["latest"][0]["version"], Plugin_json["plugins"][s]["versions"]["lin"]["latest"][0]["version"]
		if (s is 'CiscoWebCommunicatorplugincheck') or (s is 'realplayer'):
			print "Name" + " " +Plugin_json["plugins"][s]["display_name"]
			print "win version" + " " +Plugin_json["plugins"][s]["versions"]["win"]["latest"][0]["version"]
			store [Plugin_json["plugins"][s]["display_name"]]= Plugin_json["plugins"][s]["versions"]["win"]["latest"][0]["version"]
			continue
		# quictktime latest is empty
		if (s == 'apple-quicktime'):
			print "Name" + " " +Plugin_json["plugins"][s]["display_name"]
			print "there are none"
			#Plugin_json["plugins"][s]["versions"]["all"]["latest"][0] is []):
			print "there are none"
			store[Plugin_json["plugins"][s]["display_name"]] =  "there are none"
		else:
			print "Latest" + " " +Plugin_json["plugins"][s]["display_name"]
			print Plugin_json["plugins"][s]["versions"]["all"]["latest"][0]["version"]
			store[Plugin_json["plugins"][s]["display_name"]] = Plugin_json["plugins"][s]["versions"]["all"]["latest"][0]["version"]
	#key.versions.all.latest.
	#key.versions.win.latest.version 
	#key.versions.mac.latest.version
	#key.versions.lin.latest.version

	#return value for true false?

	return store
# def getVulnerable(pluginname,Plugin_json):

# 	for s in plugin_keys:
# 		if(s == 'adobe-flash-player') or (s == "adobe-reader"):
# 			print "Name" + " " + Plugin_json["plugins"][s]["display_name"]
# 			print "last vul Windows and Mac" + " " + Plugin_json["plugins"][s]["versions"]["win"]["vulneratble"][0]["version"]
# 			print "last vul Linux" + " " + Plugin_json["plugins"][s]["versions"]["lin"]["vulnerable"][0]["version"]
# 		if (s is 'CiscoWebCommunicatorplugincheck') or (s is 'realplayer'):	
# 			print "Name" + " " +Plugin_json["plugins"][s]["display_name"]
# 			print "win version" + " " +Plugin_json["plugins"][s]["versions"]["win"]["vulnerable"][0]["version"]
# 			continue
# 		if (s == 'apple-quicktime'):
# 			print "Name" + " " +Plugin_json["plugins"][s]["display_name"]
# 		else:
		
# 			print "Vulnerable" + " " +Plugin_json["plugins"][s]["display_name"]
# 			print Plugin_json["plugins"][s]["versions"]["all"]["vulnerable"][0]["version"]
# 			print "Vulnerable Windows and Mac" + " " + Plugin_json["plugins"][s]["versions"]["win"]["vulnerable"][0]["version"]
# 			print "Vulnerable Linux" + " " + Plugin_json["plugins"][s]["versions"]["lin"]["vulnerable"][0]["version"]
			
# 	#key.versions.all.vulnerable.version == number
# 	#key.versions.win.vulnerable.version
# 	#key.versions.mac.vulnerable.version
# 	#key.versions.lin.vulnerable.version
	
# 	#return value for true false? 
# 	return 

def main():
	
	#get the url stuff from  https://plugins.mozilla.org/en-us/plugins_list.json
	stuff = urllib.urlopen(pluginurl)

	#now its a dict type and stored
	Plugin_json= json.load(stuff)

	if(type(Plugin_json) is not dict):
		print "Error () json is not dict type!"
		exit()
	

	for x in plugin_keys:
		latest = getLatest(x,Plugin_json)

	#for y in plugin_keys:
	#	getVulnerable(y, Plugin_json)
	# to clean it up: separators=(',', ': ') 
	# how to print: json.dumps(great, sort_keys=True, indent=1, separators=(',',':'))


	#sturcture of this jsons
	###############################################
	# plugin : 
	#	name as key: { display_name: "Adobe Flash Player"
	#		versions: { all: { latest:[ status, version, os, platform {}]
	#								vulnerable:[ status,"vulnerability_description": "Vendor information","vulnerability_url":,"version":"detected_version": "detection_type": "*","os_name": "*","platform": {...} }}
	#
	#}
	#
	#####################################################################



	#check type and type def error
	##plugin check stuff
	Html= getHtml(blocklisturl);
	start= Html.find('blocked-items')
	Dates = getDates(Html,'<span class="dt"', ':</span>', start, len(Html))
	Plugins_block = getDates(Html,'<a href="/en-US/firefox/blocked/i', '</a>', start, len(Html))	
	
	Plugin_list_dict = dict(zip(Plugins_block, Dates))
	#print Plugin_list_dict
	#print "lalalalalalalal"
	print latest

	#are keys of latest in plugin_list_dict
	#print set(latest.keys).issubset(Plugins_list_dict.keys)
	for key in Plugin_list_dict:
		print key
		if key in latest: 
			print key
	#compare the dict to list
	




#boiler plate main
if __name__ == '__main__':
	main()
