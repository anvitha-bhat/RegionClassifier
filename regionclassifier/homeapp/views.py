from django.http import HttpResponse,Http404
from django.shortcuts import render
import urllib2

# Create your views here.
def fetch_source(url):
    "fetches the page content(html) from the given url"
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url, None, headers)
    try:
        response = urllib2.urlopen(req)
        page = response.read()
        response.close()
    except:
        page = ""
return page


def home(request):
	context = {
	}
	return render(request, 'home.html', context)

def classify(request):
	lat = request.POST['lat']
	lng = request.POST['long']


	context = {
	}
	return
