#coding: utf-8
import subprocess
from datetime import datetime

def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)

def say_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)

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
    text = name+'さんですね？！こんにちは！！'
    jtalk(text)
    

