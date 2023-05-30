from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
    
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        params = {'purpose':'Changed to Uppercase', 'analyzed_text':analyzed}
    
    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'Extra Space Removed:', 'analyzed_text':analyzed}
    
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'New Lines Removed:', 'analyzed_text':analyzed}
    
    # if charcount == 'on':
    #     num = len(djtext)
    #     print(num)
    #     params = {'purpose':'Total number of characters:', 'analyzed_text':num, 'count':num}
        # return render(request, 'analyze.html', params)
    
    if(removepunc != 'on' and fullcaps != 'on' and extraspaceremover != 'on' and newlineremover != 'on'): # and charcount != 'on'):
        return HttpResponse("Error")
    
    return render(request, 'analyze.html', params)
