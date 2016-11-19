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


d = datetime.now()
text = '%s月%s日、%s時%s分、' % (d.month, d.day, d.hour, d.minute)
text = text + "今日は雨が少し降ります。傘を持って行きましょう！"
text = text + '矢野さんですね？！こんにちは！！今日のニュースをお届けします。'
text = text + "先月１７日に打ち上げられた中国の宇宙飛行船の乗組員２人が、約１か月間の宇宙での滞在を終え、１８日に地球に無事帰還。国営新華社通信によると、２人の宇宙飛行士の健康に問題はなく、ミッションは成功したという。中国の宇宙での有人飛行活動は６回目です。"
text = text + 'また、銀座線に遅れが出ています。早めに家を出ましょう。以上です。'
jtalk(text)