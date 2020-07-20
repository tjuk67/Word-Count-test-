from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddic = {}

    for word in wordlist:
        if word in worddic:
            #Increase
            worddic[word] += 1
        else:
            #add to the dictionary
            worddic[word] = 1

    SortedWords = sorted(worddic.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'SortedWords': SortedWords})

def about(request):
    return render(request, 'about.html')

def Liverpool(request):
    return HttpResponse('We are the Champions'
        ' We are the Champions'
        ' No time For losers'
        ' As we are the Champions'
        ' Of the world')
