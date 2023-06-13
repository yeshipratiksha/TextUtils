# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


# def ex1(request):
    # sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
    #          '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
    #          '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
    #          '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    # return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    countchar = request.POST.get('countchar', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed

        # return render(request, 'analyze.html', params)

    if extraspaceremover =="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Space Removed' , 'analyzed_text': analyzed}
        djtext=analyzed

        # return render(request, 'analyze.html', params ) 

    if newlineremover =="on":  
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            
            print("pre",analyzed)
        params = {'purpose':'New Line Removed' , 'analyzed_text': analyzed}
        djtext=analyzed

        # return render(request, 'analyze.html', params )
    if(countchar =="on"):
        analyzed = ""
        count = 0
        for char in djtext:
            if char.isalpha():
                count += 1

                analyzed = count
        params = {'purpose':'The number of characters' , 'analyzed_text': analyzed}
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and countchar!="on"):
        return HttpResponse("Please type the text on which the operations are to be performed and do select the operation to be performed.")    

        # return render(request, 'analyze.html', params)
            
    # else:
   #     return HttpResponse("Write Proper Text in the Textarea  <a href = '/'> Back </a>")
    
    return render(request, 'analyze.html', params)

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")

