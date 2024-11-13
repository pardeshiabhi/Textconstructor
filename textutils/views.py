
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')

def analyze(request):
    text = request.POST.get('text','default')
    remover = request.POST.get('remover','off')
    full_caps = request.POST.get('full_caps','off')
    newline_remover = request.POST.get('newline_remover','off')
    space_remover= request.POST.get('space_remover','off')

    if remover == "on":
        punctuation ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuation:
                analyzed = analyzed + char
        abhi = {'purpose':'remove punctuations', 'analyzed_text': analyzed}
        text = analyzed

    if(full_caps=="on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()

        abhi = {'purpose': 'change to upper case', 'analyzed_text': analyzed}
        text = analyzed

    if(newline_remover=="on"):
        analyzed = ""
        for char in text:
            if char != "/n":
                analyzed = analyzed + char

        abhi = {'purpose': 'change to upper case', 'analyzed_text': analyzed}
        text = analyzed

    if(space_remover=="on"):
        analyzed = ""
        for index,char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                 analyzed = analyzed + char
        abhi = {'purpose': 'change to upper case', 'analyzed_text': analyzed}

    if( remover != "on" and full_caps!="on" and newline_remover!="on" and space_remover!="on"):
        return HttpResponse("Please select any operation to run textutils")

    return render(request, 'analyze.html',abhi)







