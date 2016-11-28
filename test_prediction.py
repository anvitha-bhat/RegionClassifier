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
    #print page
    return page


w = open('prediction.txt','a')
with open("in.txt") as f:
    x = f.readlines();
    for line in x:
        temp = line.split(',')
        cluster = fetch_source("http://127.0.0.1:8000/classify?latitude="+temp[0]+"&longtitude="+temp[1])
        t = temp[2]+","+cluster+"\n"
        w.write(t)
w.close()
