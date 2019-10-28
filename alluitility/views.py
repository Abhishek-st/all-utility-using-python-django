from django.shortcuts import render
import requests
import wikipedia
import pypandoc
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    k = {'s': "hello"}

    return render(request, 'allutility/index.html', k)



def home(request):
    return render(request, 'allutility/home.html')

def ide(request):
    if request.method == 'POST':

        cod = request.POST['co']
        inp = request.POST['input']
        lang = request.POST['lang']

        print(lang)

        url = "https://ide.geeksforgeeks.org/main.php"

        data = {
            'lang': lang,
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
        'key': 'ee78c85bc8505e964bca35ca7c966d4a',
        'data': dat
        }

        response = requests.post('https://www.prepostseo.com/apis/checkPlag', data=data)

        k = {'c': dat, 'o': response.json(), 's':0}
        print(response.json())
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

        print(upfi.name)
        print(upfi.content_type)

        output = pypandoc.convert_file(f'./media/{upfi.name}', 'docx', outputfile="./media/somefile.odt", extra_args=['-V', 'geometry:margin=1.5cm', '--pdf-engine', '/usr/bin/xelatex'])
        assert output == ""

        s = './media/somefile.odt'
        k = {'s': s, 'c': 1}
        return render(request, 'allutility/doc.html',k)
        

