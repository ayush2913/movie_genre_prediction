import sys
import urllib2
from bs4 import BeautifulSoup

def get_review(soup,genre):
	data = {}
	review = soup.find('div', class_="review large-first-letter").text
	name = soup.find('div', class_="movie_page").find('h1').text.strip()
	data.update({'name':name,'review':review,'genre':genre})
	
	return data


'''def get_name(soup,genre):
	list = []
	for tr in soup.findAll("tr", {"class":["even", "odd"]}):
		data = {}
		division = (tr.find('div', class_="button related_pages review "))
		try:
			 if(division.find('a').text=="wogma review"):
				link = "http://wogma.com"+division.find('a')['href']
#				print link
				web_page = urllib2.urlopen(link).read()
				soup1 = BeautifulSoup(web_page)
				data.update(get_review(soup1,genre))
				list.add(data)
		except:
			continue
	return list
'''


def get_genre(soup):
	list = []
	for tr in soup.findAll("tr", {"class":["even", "odd"]}):
		genre = tr.text.strip()
		link = "http://wogma.com" + tr.find("a")['href'].strip()
		web_page = urllib2.urlopen(link).read()
		soup1 = BeautifulSoup(web_page)
		for tr in soup1.findAll("tr", {"class":["even", "odd"]}):
			data = {}
			division = (tr.find('div', class_="button related_pages review "))
			try:
				 if(division.find('a').text=="wogma review"):
					link1 = "http://wogma.com"+division.find('a')['href']
#					print link1
					web_page1 = urllib2.urlopen(link1).read()
					soup2 = BeautifulSoup(web_page1)
					data.update(get_review(soup2,genre))
					list.append(data)
			except:
				continue


	return list



try :
    list = []
    web_page = urllib2.urlopen("http://wogma.com/genres/").read()
    soup = BeautifulSoup(web_page)
    list = get_genre(soup)
    for item in list:
	print item
except urllib2.HTTPError :
    print("HTTPERROR!")
except urllib2.URLError :
    print("URLERROR!")

