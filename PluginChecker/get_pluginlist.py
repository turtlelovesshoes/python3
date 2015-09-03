# This will be the part that retreives the list of plugin verions from plugins.mozilla.org page
# https://plugins.mozilla.org/en-us/plugins_list.json
# https://docs.python.org/2/library/json.html

#libraries
import json 
import urllib

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

def getLatest(pluginname,Plugin_json):
	#check if its a valid key:
	
	for s in plugin_keys:
		if(s == 'adobe-flash-player') or (s == "adobe-reader"):
			print "Name" + " " +Plugin_json["plugins"][s]["display_name"]
			print "Latest Windows and Mac" + " " + Plugin_json["plugins"][s]["versions"]["win"]["latest"][0]["version"]
			print "Latest Linux" + " " + Plugin_json["plugins"][s]["versions"]["lin"]["latest"][0]["version"]
		if (s is 'CiscoWebCommunicatorplugincheck') or (s is 'realplayer'):
			print "Name" + " " +Plugin_json["plugins"][s]["display_name"]
			print "win version" + " " +Plugin_json["plugins"][s]["versions"]["win"]["latest"][0]["version"]
			continue
		# quictktime latest is empty
		if (s == 'apple-quicktime'):
			print "Name" + " " +Plugin_json["plugins"][s]["display_name"]
			print "there are none"
			#Plugin_json["plugins"][s]["versions"]["all"]["latest"][0] is []):
			print "there are none"
		else:
			print "Latest" + " " +Plugin_json["plugins"][s]["display_name"]
			print Plugin_json["plugins"][s]["versions"]["all"]["latest"][0]["version"]
	#key.versions.all.latest.
	#key.versions.win.latest.version 
	#key.versions.mac.latest.version
	#key.versions.lin.latest.version

	#return value for true false?
	return 
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
		getLatest(x,Plugin_json)
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




#boiler plate main
if __name__ == '__main__':
	main()



