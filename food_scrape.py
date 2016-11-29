import urllib2
import json

KEY = "AIzaSyAkc4IsSSZJUJSSANGcHqqKysda-dFY_Sw"

food_count = [{"chinese":0,"pizza":0,"cafe":0,"icecream":0,"continental":0,"fastfood":0,"italian":0,"mexican":0,"indian":0},
             {"chinese":0,"pizza":0,"cafe":0,"icecream":0,"continental":0,"fastfood":0,"italian":0,"mexican":0,"indian":0},
             {"chinese":0,"pizza":0,"cafe":0,"icecream":0,"continental":0,"fastfood":0,"italian":0,"mexican":0,"indian":0},
             {"chinese":0,"pizza":0,"cafe":0,"icecream":0,"continental":0,"fastfood":0,"italian":0,"mexican":0,"indian":0},
             {"chinese":0,"pizza":0,"cafe":0,"icecream":0,"continental":0,"fastfood":0,"italian":0,"mexican":0,"indian":0}]

food_score = [{"chinese":0,"pizza":0,"cafe":0,"icecream":0,"continental":0,"fastfood":0,"italian":0,"mexican":0,"indian":0},
             {"chinese":0,"pizza":0,"cafe":0,"icecream":0,"continental":0,"fastfood":0,"italian":0,"mexican":0,"indian":0},
             {"chinese":0,"pizza":0,"cafe":0,"icecream":0,"continental":0,"fastfood":0,"italian":0,"mexican":0,"indian":0},
             {"chinese":0,"pizza":0,"cafe":0,"icecream":0,"continental":0,"fastfood":0,"italian":0,"mexican":0,"indian":0},
             {"chinese":0,"pizza":0,"cafe":0,"icecream":0,"continental":0,"fastfood":0,"italian":0,"mexican":0,"indian":0}]


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

def scrape(lat,lng,ind):
    type = ["chinese","pizza","cafe","icecream","continental","fastfood","italian","mexican","indian"]
    for i in type:
        print(i)
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(lat)+","+str(lng)+"&type=food&keyword="+i+"&radius=1000&key="
        data_x = fetch_source(url+KEY)
        data = json.loads(data_x)
        results = data["results"]
        for x in results:
            if("rating" in x):
                food_count[ind][i] = food_count[ind][i] + 1
                food_score[ind][i] = food_score[ind][i] + float(x["rating"])

with open("out_2.txt") as f:
    x = f.readlines()
    for line in x:
        t = line.split(",")
        scrape(t[0],t[1],int(t[3]))

t = open("food_cnt.txt","a")
t.write("chinesecount0 = "+str(food_count[0]["chinese"])+"\n")
t.write("pizzacount0 = "+str(food_count[0]["pizza"])+"\n")
t.write("cafecount0 = "+str(food_count[0]["cafe"])+"\n")
t.write("icecreamcount0 = "+str(food_count[0]["icecream"])+"\n")
t.write("continentalcount0 = "+str(food_count[0]["continental"])+"\n")
t.write("fastfoodcount0 = "+str(food_count[0]["fastfood"])+"\n")
t.write("italiancount0 = "+str(food_count[0]["italian"])+"\n")
t.write("mexicancount0 = "+str(food_count[0]["mexican"])+"\n")
t.write("indiancount0 = "+str(food_count[0]["indian"])+"\n")


t.write("chinesecount1 = "+str(food_count[1]["chinese"])+"\n")
t.write("pizzacount1 = "+str(food_count[1]["pizza"])+"\n")
t.write("cafecount1 = "+str(food_count[1]["cafe"])+"\n")
t.write("icecreamcount1 = "+str(food_count[1]["icecream"])+"\n")
t.write("continentalcount1 = "+str(food_count[1]["continental"])+"\n")
t.write("fastfoodcount1 = "+str(food_count[1]["fastfood"])+"\n")
t.write("italiancount1 = "+str(food_count[1]["italian"])+"\n")
t.write("mexicancount1 = "+str(food_count[1]["mexican"])+"\n")
t.write("indiancount1 = "+str(food_count[1]["indian"])+"\n")


t.write("chinesecount2 = "+str(food_count[2]["chinese"])+"\n")
t.write("pizzacount2 = "+str(food_count[2]["pizza"])+"\n")
t.write("cafecount2 = "+str(food_count[2]["cafe"])+"\n")
t.write("icecreamcount2 = "+str(food_count[2]["icecream"])+"\n")
t.write("continentalcount2 = "+str(food_count[2]["continental"])+"\n")
t.write("fastfoodcount2 = "+str(food_count[2]["fastfood"])+"\n")
t.write("italiancount2 = "+str(food_count[2]["italian"])+"\n")
t.write("mexicancount2 = "+str(food_count[2]["mexican"])+"\n")
t.write("indiancount2 = "+str(food_count[2]["indian"])+"\n")


t.write("chinesecount3 = "+str(food_count[3]["chinese"])+"\n")
t.write("pizzacount3 = "+str(food_count[3]["pizza"])+"\n")
t.write("cafecount3 = "+str(food_count[3]["cafe"])+"\n")
t.write("icecreamcount3 = "+str(food_count[3]["icecream"])+"\n")
t.write("continentalcount3 = "+str(food_count[3]["continental"])+"\n")
t.write("fastfoodcount3 = "+str(food_count[3]["fastfood"])+"\n")
t.write("italiancount3 = "+str(food_count[3]["italian"])+"\n")
t.write("mexicancount3 = "+str(food_count[3]["mexican"])+"\n")
t.write("indiancount3 = "+str(food_count[3]["indian"])+"\n")

t.write("chinesescore0 = "+str(food_score[0]["chinese"])+"\n")
t.write("pizzascore0 = "+str(food_score[0]["pizza"])+"\n")
t.write("cafescore0 = "+str(food_score[0]["cafe"])+"\n")
t.write("icecreamscore0 = "+str(food_score[0]["icecream"])+"\n")
t.write("continentalscore0 = "+str(food_score[0]["continental"])+"\n")
t.write("fastfoodscore0 = "+str(food_score[0]["fastfood"])+"\n")
t.write("italianscore0 = "+str(food_score[0]["italian"])+"\n")
t.write("mexicanscore0 = "+str(food_score[0]["mexican"])+"\n")
t.write("indianscore0 = "+str(food_score[0]["indian"])+"\n")


t.write("chinesescore1 = "+str(food_score[1]["chinese"])+"\n")
t.write("pizzascore1 = "+str(food_score[1]["pizza"])+"\n")
t.write("cafescore1 = "+str(food_score[1]["cafe"])+"\n")
t.write("icecreamscore1 = "+str(food_score[1]["icecream"])+"\n")
t.write("continentalscore1 = "+str(food_score[1]["continental"])+"\n")
t.write("fastfoodscore1 = "+str(food_score[1]["fastfood"])+"\n")
t.write("italianscore1 = "+str(food_score[1]["italian"])+"\n")
t.write("mexicanscore1 = "+str(food_score[1]["mexican"])+"\n")
t.write("indianscore1 = "+str(food_score[1]["indian"])+"\n")


t.write("chinesescore2 = "+str(food_score[2]["chinese"])+"\n")
t.write("pizzascore2 = "+str(food_score[2]["pizza"])+"\n")
t.write("cafescore2 = "+str(food_score[2]["cafe"])+"\n")
t.write("icecreamscore2 = "+str(food_score[2]["icecream"])+"\n")
t.write("continentalscore2 = "+str(food_score[2]["continental"])+"\n")
t.write("fastfoodscore2 = "+str(food_score[2]["fastfood"])+"\n")
t.write("italianscore2 = "+str(food_score[2]["italian"])+"\n")
t.write("mexicanscore2 = "+str(food_score[2]["mexican"])+"\n")
t.write("indianscore2 = "+str(food_score[2]["indian"])+"\n")


t.write("chinesescore3 = "+str(food_score[3]["chinese"])+"\n")
t.write("pizzascore3 = "+str(food_score[3]["pizza"])+"\n")
t.write("cafescore3 = "+str(food_score[3]["cafe"])+"\n")
t.write("icecreamscore3 = "+str(food_score[3]["icecream"])+"\n")
t.write("continentalscore3 = "+str(food_score[3]["continental"])+"\n")
t.write("fastfoodscore3 = "+str(food_score[3]["fastfood"])+"\n")
t.write("italianscore3 = "+str(food_score[3]["italian"])+"\n")
t.write("mexicanscore3 = "+str(food_score[3]["mexican"])+"\n")
t.write("indianscore3 = "+str(food_score[3]["indian"])+"\n")


t.write("chinesemean0 = "+str(food_score[0]["chinese"]/food_count[0]["chinese"])+"\n")
t.write("pizzamean0 = "+str(food_score[0]["pizza"]/food_count[0]["pizza"])+"\n")
t.write("cafemean0 = "+str(food_score[0]["cafe"]/food_count[0]["cafe"])+"\n")
t.write("icecreammean0 = "+str(food_score[0]["icecream"]/food_count[0]["icecream"])+"\n")
t.write("continentalmean0 = "+str(food_score[0]["continental"]/food_count[0]["continental"])+"\n")
t.write("fastfoodmean0 = "+str(food_score[0]["fastfood"]/food_count[0]["fastfood"])+"\n")
t.write("italianmean0 = "+str(food_score[0]["italian"]/food_count[0]["italian"])+"\n")
t.write("mexicanmean0 = "+str(food_score[0]["mexican"]/food_count[0]["mexican"])+"\n")
t.write("indianmean0 = "+str(food_score[0]["indian"]/food_count[0]["indian"])+"\n")


t.write("chinesemean1 = "+str(food_score[1]["chinese"]/food_count[1]["chinese"])+"\n")
t.write("pizzamean1 = "+str(food_score[1]["pizza"]/food_count[1]["pizza"])+"\n")
t.write("cafemean1 = "+str(food_score[1]["cafe"]/food_count[1]["cafe"])+"\n")
t.write("icecreammean1 = "+str(food_score[1]["icecream"]/food_count[1]["icecream"])+"\n")
t.write("continentalmean1 = "+str(food_score[1]["continental"]/food_count[1]["continental"])+"\n")
t.write("fastfoodmean1 = "+str(food_score[1]["fastfood"]/food_count[1]["fastfood"])+"\n")
t.write("italianmean1 = "+str(food_score[1]["italian"]/food_count[1]["italian"])+"\n")
t.write("mexicanmean1 = "+str(food_score[1]["mexican"]/food_count[1]["mexican"])+"\n")
t.write("indianmean1 = "+str(food_score[1]["indian"]/food_count[1]["indian"])+"\n")


t.write("chinesemean2 = "+str(food_score[2]["chinese"]/food_count[2]["chinese"])+"\n")
t.write("pizzamean2 = "+str(food_score[2]["pizza"]/food_count[2]["pizza"])+"\n")
t.write("cafemean2 = "+str(food_score[2]["cafe"]/food_count[2]["cafe"])+"\n")
t.write("icecreammean2 = "+str(food_score[2]["icecream"]/food_count[2]["icecream"])+"\n")
t.write("continentalmean2 = "+str(food_score[2]["continental"]/food_count[2]["continental"])+"\n")
t.write("fastfoodmean2 = "+str(food_score[2]["fastfood"]/food_count[2]["fastfood"])+"\n")
t.write("italianmean2 = "+str(food_score[2]["italian"]/food_count[2]["italian"])+"\n")
t.write("mexicanmean2 = "+str(food_score[2]["mexican"]/food_count[2]["mexican"])+"\n")
t.write("indianmean2 = "+str(food_score[2]["indian"]/food_count[2]["indian"])+"\n")


t.write("chinesemean3 = "+str(food_score[3]["chinese"]/food_count[3]["chinese"])+"\n")
t.write("pizzamean3 = "+str(food_score[3]["pizza"]/food_count[3]["pizza"])+"\n")
t.write("cafemean3 = "+str(food_score[3]["cafe"]/food_count[3]["cafe"])+"\n")
t.write("icecreammean3 = "+str(food_score[3]["icecream"]/food_count[3]["icecream"])+"\n")
t.write("continentalmean3 = "+str(food_score[3]["continental"]/food_count[3]["continental"])+"\n")
t.write("fastfoodmean3 = "+str(food_score[3]["fastfood"]/food_count[3]["fastfood"])+"\n")
t.write("italianmean3 = "+str(food_score[3]["italian"]/food_count[3]["italian"])+"\n")
t.write("mexicanmean3 = "+str(food_score[3]["mexican"]/food_count[3]["mexican"])+"\n")
t.write("indianmean3 = "+str(food_score[3]["indian"]/food_count[3]["indian"])+"\n")
