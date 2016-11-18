# -*- coding:utf-8 -*-
import numpy,cv2,urllib,requests,sys,random,string,json

def saveFace(image_path):  
    url = "https://apius.faceplusplus.com/detection/detect";
    param = [
        ( "api_key", "db262d0ebc7bdee61600c99cdd836b6e"),
        ( "api_secret", "gjL4nZD2DdDd0_FrnUDHg0Sij2nJGlgW"),
        ( "url", image_path)
    ]
    url += "?{0}".format( urllib.urlencode( param ) )
    result = None
    try :
        result = json.loads(urllib.urlopen( url ).read())
        if  len(result['face']) > 0:
            print result['face'][0]['face_id'];
    except ValueError :
        print "error"



def send(imagenumber):
    url = 'http://version1.xyz/emmer/'
    filename = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)]) + '.jpg'
    image = open('face_'+str(imagenumber)+'.jpg')
    files = {'file':(filename,image,'image/jpeg')}
    data = {}
    r=requests.post(url+'images/add',files=files,data=data)
    image_path = url+'img/'+filename
    print image_path;
    saveFace(image_path);



valiable = sys.argv
send(valiable[1]);
