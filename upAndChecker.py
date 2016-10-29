import urllib
import json
import random
import string
import requests




def checkface(image_path):  
	url = "http://apius.faceplusplus.com/recognition/identify"
	param = [
		( "api_key", "db262d0ebc7bdee61600c99cdd836b6e"),
		( "api_secret", "gjL4nZD2DdDd0_FrnUDHg0Sij2nJGlgW"),
		( "group_name", "jphacks"),
		( "url", image_path)
	]

	url += "?{0}".format( urllib.urlencode( param ) )

	result = None
	try :
		result = json.loads(urllib.urlopen( url ).read())
	#	print result
		print result['face'][0]['candidate'][0]['person_name']
	except ValueError :
		print "error"

def send():
	url = 'http://cu76nat-aj3-app000.c4sa.net/'
	filename = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)]) + '.jpg'
	image = open('face.jpg')
	files = {'file':(filename,image,'image/jpeg')}
	data = {}
	r=requests.post(url+'images/add',files=files,data=data)
	print(r.text)
	image_path = url+'img/'+filename
	checkface(image_path)
