# Make an animated web-scraper from a Wikipedia page of your
# choice. Refer to this for the exact problem statement. Your scraper, if
# given a link to a Wikipedia webpage, should make a visual graph
# using matplotlib. Sample output can be seen below. You can get
# creative in your own ways to present the graph (gif, animation) 

import urllib.request as urllib2
from bs4 import BeautifulSoup # Need BeautfulSoup4 installed for this

url = "https://en.wikipedia.org/wiki/Phenomenon"

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

print(soup.title.string)

i = 0

def get_link(mw_text):
    for para in mw_text.find_all('p'):
        for l in para.find_all('a'):
            if not (l.has_attr('title')):
                #print("No title")
                continue
            if (l['title'] == soup.title.string):
                #print("Title leads to same page")
                continue
            if (l['title'] == "Latin language"):
                #print("Title leads to Latin")
                continue
            if(l.has_attr('class')):
                if(l['class']=="new"):
                    #print("Has class so must be red")
                    continue
            if(l.parent.name == 'i'):
                #print("Parent is i")
                continue
            if (l['href'].startswith("https://en.wiktionary.org/wiki")):
                #print("Not a wiki page")
                continue
            if (l['href'].startswith("https://en.wikipedia.org/wiki/Help:IPA")):
                #print("Not a wiki page")
                continue
            
            return l
    

while(True):
    body = soup.find('div', attrs={'id': 'bodyContent'})
    mw_text = body.find('div', attrs={'id': 'mw-content-text'})
    
    link = get_link(mw_text)

    print(link['title'])
    
    if(link['title']=="Philosophy"):
        break
    
    link_new = "https://en.wikipedia.org" + link['href']
    page = urllib2.urlopen(link_new)
    soup = BeautifulSoup(page, 'html.parser')
    
    i+=1
    if(i>30):
        break