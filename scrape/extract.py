import urllib2
import json

KEY = "AIzaSyAkc4IsSSZJUJSSANGcHqqKysda-dFY_Sw"

MapList = ["accounting","airport","amusement_park","aquarium","art_gallery","atm","bakery","bank","bar","beauty_salon","bicycle_store","book_store","bowling_alley","bus_station","cafe","campground","car_dealer","car_rental","car_repair","car_wash","casino","cemetery","church","city_hall","clothing_store","convenience_store","courthouse","dentist","department_store","doctor","electrician","electronics_store","embassy","establishment ","finance ","fire_station","florist","food ","funeral_home","furniture_store","gas_station","general_contractor ","grocery_or_supermarket ","gym","hair_care","hardware_store","health ","hindu_temple","home_goods_store","hospital","insurance_agency","jewelry_store","laundry","lawyer","library","liquor_store","local_government_office","locksmith","lodging","meal_delivery","meal_takeaway","mosque","movie_rental","movie_theater","moving_company","museum","night_club","painter","park","parking","pet_store","pharmacy","physiotherapist","place_of_worship ","plumber","police","post_office","real_estate_agency","restaurant","roofing_contractor","rv_park","school","shoe_store","shopping_mall","spa","stadium","storage","store","subway_station","synagogue","taxi_stand","train_station","transit_station","travel_agency","university","veterinary_care","zoo"]
names_list = []
type_list = []

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

###parsing json format to get objects
def jsonparse( data ):
    data = json.loads(data)
    results = data["results"]
    for x in results:
        names_list.append(str(x["name"]))
        type_list.append(x["types"])
        print(names_list)
        print(type_list)

def extract(name,lat,lng):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+lat+","+lng+"&radius=500&key="
    print(url+KEY)
    data_x = fetch_source(url+KEY)
    print(data_x)
    jsonparse(str(data_x))
