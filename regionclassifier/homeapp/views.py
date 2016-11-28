from django.http import HttpResponse,Http404
from django.shortcuts import render
import urllib2
import json

KEY = "AIzaSyAkc4IsSSZJUJSSANGcHqqKysda-dFY_Sw"

NO_CLUSTERS = 4

CLUSTER =[[0.0285714285714286,0.685714285714286,0.0428571428571429,0.728571428571429,0.0285714285714286,0.0714285714285714,0.0428571428571429,0.385714285714286,0.0857142857142857,0.0571428571428571,0.171428571428571,0.0571428571428571,0.228571428571429,0.0714285714285714,0.142857142857143,0.2,0.114285714285714,0.0857142857142857,0.285714285714286,0,0.0428571428571429,0.214285714285714,0.357142857142857,0.328571428571429,0.114285714285714,0.0428571428571429,0.0428571428571429,0.0285714285714286,0.0428571428571429,0.0571428571428571,0.4,0.0428571428571429,0.0285714285714286,0.0428571428571429,0.0142857142857143,0.0285714285714286,0.0571428571428571,0.0857142857142857,0.0285714285714286,0.171428571428571,0.442857142857143,0.828571428571429,0.0142857142857143,0.0428571428571429,0.0571428571428571,2.14285714285714,0.385714285714286,0.157142857142857,0.0428571428571429],
		  [0,0,0,0.125,1.25,0,0,0,0.375,0,0.125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.25,0,0,0,0,15.5,0.125,0.125,0,0.625,0,0,0,0,0,2.625,0,0,0.125,1.25,0.5,0,0.125,0],
		  [0,0.363636363636364,0.454545454545455,0.96969696969697,0.151515151515152,0.0909090909090909,0.0606060606060606,0,0.272727272727273,0.212121212121212,0.303030303030303,0.121212121212121,0.696969696969697,0.0303030303030303,0.121212121212121,0.454545454545455,0.393939393939394,0.0909090909090909,0.0909090909090909,0.0303030303030303,0.181818181818182,0.181818181818182,0.757575757575758,0.151515151515152,0.242424242424242,0.181818181818182,0.0303030303030303,0,0.0303030303030303,0.0303030303030303,0.818181818181818,0.181818181818182,0.121212121212121,0.0303030303030303,0.0303030303030303,0.0303030303030303,0.0909090909090909,0,0.0909090909090909,0.212121212121212,1.84848484848485,0.272727272727273,0.212121212121212,0.0606060606060606,0.0303030303030303,5.87878787878788,0,0.333333333333333,0.0606060606060606],
		  [0.375,0.21875,0.09375,0.8125,0.65625,0.125,0.09375,0,0.15625,0.09375,0.1875,0,0.0625,0,0.09375,0.09375,0.09375,0,0.0625,0.125,0,0.09375,0.25,0.4375,0.15625,0.0625,0,0.3125,0,0.03125,4.34375,0.09375,0.0625,0.09375,0.0625,0,0,0.03125,0,0.375,2.59375,0.5,0.03125,0,0.21875,2.15625,0,0.84375,0.0625]]

MAP = ["art_gallery","atm","bakery","bank","bar","beauty_salon","book_store","bus_station","cafe","car_dealer","car_repair","church","clothing_store","dentist","doctor","electronics_store","furniture_store","gas_station","gym","hair_care","hardware_store","hindu_temple","home_goods_store","hospital","insurance_agency","jewelry_store","laundry","lawyer","library","local_government_office","lodging","meal_delivery","meal_takeaway","movie_theater","night_club","park","pharmacy","police","post_office","real_estate_agency","restaurant","school","shoe_store","shopping_mall","spa","store","transit_station","travel_agency","university"]


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
    #print page
    return page

def euclideanDist(dict):
	dist_list = []
	for i in range(0,NO_CLUSTERS):
		dist = 0.0
		for x in range(0,len(MAP)):
			dist = dist + (dict[MAP[x]]-CLUSTER[i][x])**2
		dist_list.append(dist)
	print(dist_list)
	return dist_list.index(min(dist_list))


###parsing json format to get objects
def jsonparse( data):
    data = json.loads(data)
    results = data["results"]
    dict = { "art_gallery":0,"atm":0, "bakery":0, "bank":0,"bar":0, "beauty_salon":0, "book_store":0,"bus_station":0, "cafe":0, "car_dealer":0,"car_repair":0,"church":0, "clothing_store":0,"dentist":0, "doctor":0, "electronics_store":0, "furniture_store":0, "gas_station":0, "gym":0, "hair_care":0, "hardware_store":0,  "hindu_temple":0,"home_goods_store":0,"hospital":0,  "insurance_agency":0,"jewelry_store":0, "laundry":0, "lawyer":0,"library":0, "local_government_office":0, "lodging":0, "meal_delivery":0, "meal_takeaway":0,"movie_theater":0,"night_club":0,"park":0,"pharmacy":0,"police":0,"post_office":0,"real_estate_agency":0,"restaurant":0,"school":0,"shoe_store":0,"shopping_mall":0,"spa":0,"store":0,"transit_station":0,"travel_agency":0,"university":0}
    for x in results:
        for i in  x["types"]:
            key = i.encode("utf-8","ignore")
            if key in dict:
                dict[key] = dict[key]+1
    return dict

def extract(lat,lng):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(lat)+","+str(lng)+"&radius=1000&key="
    data_x = fetch_source(url+KEY)
    dict = jsonparse(str(data_x))
    return euclideanDist(dict)

def home(request):
	context = {
	}
	return render(request, 'home.html', context)

def classify(request):
	lat = request.GET['latitude']
	lng = request.GET['longtitude']
	context = {
	}
	return HttpResponse(extract(lat,lng))
