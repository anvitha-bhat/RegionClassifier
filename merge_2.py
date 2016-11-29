import urllib2

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

g = open("out_2.txt","a")
with open("in_2.txt") as f:
    loc = f.readlines()
    for i in loc:
        x = i.split(",")
        cluster = fetch_source("http://127.0.0.1:8000/classify?latitude="+x[0]+"&longtitude="+x[1])
        g.write(x[0]+","+x[1]+","+x[2].strip()+","+cluster+"\n")
