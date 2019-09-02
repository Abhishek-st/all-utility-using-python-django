from django.shortcuts import render
import requests
import wikipedia
import PyPDF2
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    data = {
    'key': '2e4b0da059a449b3249f668e88d1bbec',
    'data': 'Despite all the talk about Tendulkar’s failures under pressure, his performances in big events were difficult to ignore. In his two World Cup final appearances, Tendulkar flattered to deceive with scores of 4 (2003 final vs. Australia) and 18 (2011 final vs. Sri Lanka). Nevertheless, his overall performances and contributions over the course of the aforementioned tournaments played a huge part in getting India to the final in the first place'
    }

    response = requests.post('https://www.prepostseo.com/apis/checkPlag', data=data)
    k = {'s': response.json()}
    k = {'s': "hello"}

    return render(request, 'allutility/index.html', k)


def ide(request):
    if request.method == 'POST':

        cod = request.POST['co']
        inp = request.POST['input']

        print(cod)

        url = "https://ide.geeksforgeeks.org/main.php"

        data = {
            'lang': 'python3',
            'code': cod,
            'input': inp,
            'save': True
        }

        r = requests.post(url, data=data)

        k = {'s': r.json(), 'c': cod, 'i':inp}

        return render(request, 'allutility/index.html', k)


def plaren(request):
    k={'s':1}
    return render(request, 'allutility/plag.html',k)


def plares(request):
    if request.method == 'POST':
        dat = request.POST['cod']

        data = {
        'key': '2e4b0da059a449b3249f668e88d1bbec',
        'data': dat
        }

        response = requests.post('https://www.prepostseo.com/apis/checkPlag', data=data)

        k = {'c': dat, 'o': response.json(), 's':0}
        return render(request, 'allutility/plag.html', k)


def wikiren(request):
    return render(request, 'allutility/wiki.html')


def wikires(request):
    if request.method == 'POST':
        dat = request.POST['title']
        x = wikipedia.summary(dat)

        k = {'content': x, 'tit': dat}

        return render(request, 'allutility/wiki.html', k)


def docren(request):
    return render(request, 'allutility/doc.html')


def docres(request):
    if request.method == 'POST':
        upfi = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(upfi.name, upfi)

        return render(request, 'allutility/doc.html')
        

