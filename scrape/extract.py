import urllib2
import json

KEY = "#"

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
def jsonparse( data,name,typ):
    data = json.loads(data)
    results = data["results"]
    for x in results:
        data_string = name
        data_string = data_string +","+ x["name"].encode("utf-8","ignore")+","+typ
        typelist = []
        for i in  x["types"]:
            typelist.append(i.encode("utf-8","ignore"))
        for i in MapList:
            if i in typelist:
                data_string = data_string + ",1"
            else:
                data_string = data_string + ",0"
        #print(data_string)
        with open("out.txt", "a") as myfile:
            myfile.write(data_string+"\n")


def extract(lat,lng,name,typ):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(lat)+","+str(lng)+"&radius=1000&key="
    print(url+KEY)
    data_x = fetch_source(url+KEY)
    print("fetching done.")
    jsonparse(str(data_x),name,typ)
    print("parsing done.")

def run_extract():
    with open("in2.txt") as f:
        content = f.readlines()
        for line in content:
            line = line.split(",")
            extract(line[0],line[1],line[2],line[3].strip())
