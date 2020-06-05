from django.shortcuts import render
from pytube import *
from tkinter.filedialog import *

def greetings(request):
	return render(request,'main/index.html')

def download(request):
    if request.method == 'POST':
        video_url=request.POST['video_url']
        yt = YouTube(video_url)
        
        
        yt.streams.first().download()
        return render(request,'main/download.html')

