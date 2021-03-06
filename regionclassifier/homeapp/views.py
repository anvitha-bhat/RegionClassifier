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

SECTOR = [[0.130434782608696,0.405797101449275,0.173913043478261,0.623188405797101,0.246376811594203,0.159420289855072,0.0869565217391304,0.304347826086957,0.101449275362319,0.101449275362319,0.231884057971014,0.072463768115942,0.246376811594203,0.0579710144927536,0.144927536231884,0.246376811594203,0.144927536231884,0.101449275362319,0.260869565217391,0.0434782608695652,0.072463768115942,0.217391304347826,0.347826086956522,0.333333333333333,0.115942028985507,0.0289855072463768,0.0144927536231884,0.101449275362319,0.0289855072463768,0.0289855072463768,1.07246376811594,0.0579710144927536,0.0289855072463768,0.072463768115942,0.0434782608695652,0.0144927536231884,0.072463768115942,0.072463768115942,0.0289855072463768,0.202898550724638,1.23188405797101,0.768115942028985,0.101449275362319,0.0289855072463768,0.115942028985507,2.76811594202899,0.304347826086957,0.318840579710145,0.072463768115942],
		  [0.0952380952380952,0.404761904761905,0.166666666666667,0.80952380952381,0.285714285714286,0.0238095238095238,0.0238095238095238,0.0476190476190476,0.166666666666667,0.0714285714285714,0.238095238095238,0.0476190476190476,0.404761904761905,0.0238095238095238,0.119047619047619,0.19047619047619,0.19047619047619,0,0.0714285714285714,0.0476190476190476,0.0238095238095238,0.0476190476190476,0.428571428571429,0.238095238095238,0.119047619047619,0.214285714285714,0.0476190476190476,0.0952380952380952,0.0476190476190476,0,3.30952380952381,0.119047619047619,0.0952380952380952,0.0476190476190476,0.0714285714285714,0,0.0476190476190476,0.0476190476190476,0.0238095238095238,0.285714285714286,1.5952380952381,0.380952380952381,0,0.0238095238095238,0.166666666666667,3.11904761904762,0.0476190476190476,0.5,0],
		  [0,1.8,0,2.6,0,0,0,0,0.2,0,0,0,0.4,0,0,0,0,0.4,0,0,0,0.2,0.2,0,0.6,0,0,0,0,0.2,0.4,0,0,0,0,0,0,0,0.2,0.2,0.4,0.4,0.2,0,0,2.6,0,0.4,0],
		  [0,0.428571428571429,0.142857142857143,0.857142857142857,0.571428571428571,0,0,0,0.428571428571429,0.0714285714285714,0.142857142857143,0.0714285714285714,0.142857142857143,0,0.142857142857143,0.428571428571429,0.142857142857143,0,0,0,0.142857142857143,0.142857142857143,0.571428571428571,0.285714285714286,0.285714285714286,0.142857142857143,0,0,0,0.214285714285714,6.57142857142857,0.0714285714285714,0.0714285714285714,0,0.214285714285714,0.0714285714285714,0,0,0,0,1.64285714285714,0.214285714285714,0.0714285714285714,0.0714285714285714,0.5,3,0,0.0714285714285714,0.142857142857143],
		  [0.0769230769230769,0.538461538461538,0,0.615384615384615,0.0769230769230769,0,0.0769230769230769,0.307692307692308,0.153846153846154,0.230769230769231,0.0769230769230769,0,0.230769230769231,0.0769230769230769,0,0.0769230769230769,0.307692307692308,0,0.307692307692308,0,0.0769230769230769,0.307692307692308,0.538461538461538,0.384615384615385,0.0769230769230769,0,0.0769230769230769,0.0769230769230769,0,0,0.846153846153846,0.230769230769231,0.153846153846154,0,0,0.0769230769230769,0,0,0.0769230769230769,0.307692307692308,1.46153846153846,0.692307692307692,0,0.153846153846154,0,3.07692307692308,0.307692307692308,0.307692307692308,0]]

food_map_type = ["chinese","pizza","cafe","icecream","continental","fastfood","italian","mexican","indian"]

score = [[3.7962264150943392, 3.7972972972972974, 3.9499999999999997, 3.922222222222222, 4.3, 3.75, 3.4, 4.3, 3.725],
 		 [3.8951807228915665, 3.9282352941176466, 4.071428571428571, 4.121428571428571, 4.08125, 3.689189189189189, 4.06, 4.003636363636363, 3.81875],
		 [3.776190476190476, 3.819, 3.925, 4.00327868852459, 3.975, 3.788372093023256, 3.6666666666666665, 3.9499999999999997, 3.7235294117647055],
		 [3.791758241758242,3.892477876106195, 3.9911764705882353, 4.033333333333333, 4.35, 3.5885496183206107, 3.841428571428571, 4.02051282051282, 3.972]]


SECTOR_MAP = ["residential","commercial","industrial","entertainment","commercial"]

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
	return dist_list

def findsector(dict):
	print("finding sector")
	dist_list = []
	for i in range(0,5):
		dist = 0.0
		for x in range(0,len(MAP)):
			dist = dist + (dict[MAP[x]]-SECTOR[i][x])**2
		dist_list.append(dist)
	print(dist_list)
	return SECTOR_MAP[dist_list.index(min(dist_list))]

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
    print(url+KEY)
    data_x = fetch_source(url+KEY)
    dict = jsonparse(str(data_x))
    return dict

def home(request):
	context = {
	}
	return render(request, 'home.html', context)

def specify(request):
	lat = request.GET['latitude']
	lng = request.GET['longtitude']
	url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(lat)+","+str(lng)+"&radius=1000&type=food&key="
	print(url+KEY)
	data_x = fetch_source(url+KEY)
	data = json.loads(data_x)
	print(data_x)
	t = ""
	for x in data["results"]:
		t = t + x["name"] +"<br>"
	return HttpResponse(t)

def classify(request):
	lat = request.GET['latitude']
	lng = request.GET['longtitude']
	dit = extract(lat,lng)
	cluster = euclideanDist(dit)
	print("cluster = "+ str(cluster))
	sector = findsector(dit)
	print("sector = "+ str(sector))
	commercial_comment = ["Not Commercial Region","Likely commercial","Region good for commerce","Region good for commerce"]
	residential_comment = ["Very likely Residential Region","Not Residential","Residential Region","Residential Region"]
	industry_comment = ["Might be Industrial/Residential","Not Industrial","Might be Industrial/Residential","Not Industrial"]
	entertainment_comment = ["Very likely a region of entertainment(crowd pulling)","Very likely a region of entertainment(crowd pulling)","not an entertainment region","partially entertainment region"]
	it_comment = ["Can be IT region","Not IT region","IT region probable","mostly not IT region"]
	cluster_index = cluster.index(min(cluster))
	context = {
		'cluster':cluster_index,
		'lat':lat,
		'lng':lng,
		'sector':sector,
		'cluster_dist1':cluster[0],
		'cluster_dist2':cluster[1],
		'cluster_dist3':cluster[2],
		'cluster_dist4':cluster[3],
		'commercial_comment': commercial_comment[int(cluster_index)],
		'residential_comment': residential_comment[int(cluster_index)],
		'industry_comment': industry_comment[int(cluster_index)],
		'entertainment_comment': entertainment_comment[int(cluster_index)],
		'score':score[cluster_index],
		'food_map_type':food_map_type,
	}
	return render(request, 'classify.html', context)
