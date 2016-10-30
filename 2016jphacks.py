#coding: utf-8
import urllib,json,random,string,requests,numpy,cv2,subprocess,urllib,urllib2,re
from datetime import datetime
import feedparser

def jtalk2(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed=['-r','0.8']
    outwav=['-ow','open_jtalk2.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk2.wav']
    wr = subprocess.Popen(aplay)
    
def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed=['-r','0.8']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)

def say_datetime(isMorning):
    d = datetime.now()
    text = '%s月%s日、%s時%s分、' % (d.month, d.day, d.hour, d.minute)
    say_weather(isMorning,text)

def say_news():
    text = 'プロ野球・日本シリーズの第６戦が２９日、マツダスタジアムで行われ、日本ハムが１０－４で広島を破り、１０年ぶりの日本一に輝いた。'
    jtalk(text)

def say_hello():
    text = 'こんにちは！あなたは...'
    jtalk(text)

def say_who():
    text = 'あなたは誰ですか？'
    jtalk(text)

def say_hi(name):
    text = name+'さんですね？！こんにちは！！今日のニュースをお届けします。'
    text += descs[6].encode('utf_8');
    jtalk(text)

def say_weather(isMorning,  text):
    if(isMorning):
        if(weather_data['query']['results']['channel']['item']['forecast'][0]['text'].find('Partly Cloudy') > -1):
            jtalk2(text+'今日の天気は晴れ時々曇りです。')
        if(weather_data['query']['results']['channel']['item']['forecast'][0]['text'].find('Mostly Cloudy') > -1):
            jtalk2(text+'今日の天気は曇りのち晴れです。')
        if(weather_data['query']['results']['channel']['item']['forecast'][0]['text'].find('Mostly Sunny') > -1):
            jtalk2(text+'今日は晴れのち曇りです！')
        if(weather_data['query']['results']['channel']['item']['forecast'][0]['text'].find('Sunny') > -1):
            jtalk2(text+'今日は晴れですよ！')
        if(weather_data['query']['results']['channel']['item']['forecast'][0]['text'].find('Scattered Showers') > -1):
            jtalk2(text+'今日は雨が少し降ります。傘を持って行きましょう！')
        if(weather_data['query']['results']['channel']['item']['forecast'][0]['text'].find('Heary rain') > -1):
            jtalk2(text+'今日はたくさん雨が降ります。傘を持って行きましょう！気をつけて行ってらっしゃいませ。')
    else:
        if(weather_data['query']['results']['channel']['item']['forecast'][1]['text'].find('Partly Cloudy') > -1):
            jtalk2(text+'明日の天気は晴れ時々曇りです。')
        if(weather_data['query']['results']['channel']['item']['forecast'][1]['text'].find('Mostly Cloudy') > -1):
            jtalk2(text+'明日の天気は曇りのち晴れです。')
        if(weather_data['query']['results']['channel']['item']['forecast'][1]['text'].find('Mostly Sunny') > -1):
            jtalk2(text+'明日は晴れのち曇りです！')
        if(weather_data['query']['results']['channel']['item']['forecast'][1]['text'].find('Sunny') > -1):
            jtalk2(text+'明日は晴れですよ！')
        if(weather_data['query']['results']['channel']['item']['forecast'][1]['text'].find('Scattered Showers') > -1):
            jtalk2(text+'明日は雨が少し降ります。傘を持って行きましょう！')
        if(weather_data['query']['results']['channel']['item']['forecast'][1]['text'].find('Hearay rain') > -1):
            jtalk2(text+'明日はたくさん雨が降ります。傘を持って行きましょう！気をつけて行ってらっしゃいませ。')


    
    
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
                        if  len(result['face']) > 0:
                                name=result['face'][0]['candidate'][0]['person_name']
                                print 'You must be '+name+" . "
                                print 'Hello!!' + name + "!!!"
                                say_name = '';
                                if(name == 'yano'):  say_name = '矢野'
                                elif(name == 'kudo'): say_name = '工藤'
                                elif(name == 'nagai'): say_name = '永井'
                                say_datetime(True)
                                say_hi(say_name)
                                cv2.waitKey(30000)
                        else:
                                print 'who are you ?'
                                say_who()
                
	except ValueError :
		print "error"

def send():
	url = 'http://cu76nat-aj3-app000.c4sa.net/'
	filename = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)]) + '.jpg'
	image = open('face.jpg')
	files = {'file':(filename,image,'image/jpeg')}
	data = {}
	r=requests.post(url+'images/add',files=files,data=data)
	image_path = url+'img/'+filename
	checkface(image_path)


#weather
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="sendai")'
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
result = urllib2.urlopen(yql_url.decode('UTF_8')).read()
weather_data = json.loads(result)

#news

RSS_URL = "http://feed.rssad.jp/rss/news24/index.rdf"
news_dic = feedparser.parse(RSS_URL)
descs = []
for entry in news_dic.entries:
        desc = entry.description
        desc = desc[3:]
        desc = desc[:len(desc)-4]
        descs.append( desc )
        #print desc

cascade_path = './haarcascade_frontalface_alt.xml'
cap = cv2.VideoCapture(0)
filename="face.jpg"
face_flag = False

while True:
        ret,frame = cap.read()
        image = frame
        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(image, scaleFactor=1.1,minNeighbors=1,minSize=(1,1))
        if len(facerect) <= 0:
                face_flag = False
                print("Anyone disappeared")
                #say_datetime()

        if len(facerect) > 0 and face_flag == False:
                face_flag = True
                print("hello! you are ...")
                rect=facerect[0]
                for r in facerect:
                        if rect[2] < r[2]:
                                rect = r
                x,y,w,h = rect[0],rect[1],rect[2],rect[3]
                cv2.imwrite(filename,image)
                send()
        k = cv2.waitKey(200)
        if k == 27:cap.release(); break;
