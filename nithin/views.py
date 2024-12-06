from django.shortcuts import render
from .data import articles_data
from django.http import HttpResponse
from gtts import gTTS
import os
from hulk.settings import BASE_DIR

def num(r):
    return render(r,'home.html',{'a':articles_data,"c":1})
def next(r,id):
    for i in articles_data:

        if i['id']==id:
            print(id)
            k=i["content"]
            l=i["title"]
            n=i['id']
            # red=gTTS(k,'en')
            # red.save("id.mp3")
            # os.system("start id.mp3")
            
            break
    return render(r,'nextpage.html',{'a':k,'b':l,'e':n})

def contact_us(r):
    return render(r,'contact.html')


def about_us(r):
    return render(r,'about.html')


def solution(r):
    return render(r,'help.html')




def recodr(r,id):
    for i in articles_data:

        if i['id']==id:
            a=gTTS(i['content'],lang='kn')
            pth=os.path.join("audiofile",f"audio_{i["id"]}.mp3")
            k=a.save(pth)
            with open(pth,'rb') as f:
                audio_data=f.read()
                return render(r,'audio.html',{'auto':k},)





# Create your views here.
