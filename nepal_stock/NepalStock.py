from bs4 import BeautifulSoup
import html5lib
import urllib
import sys

def getStock(item):
	url='http://merolagani.com/CompanyDetail.aspx?symbol='+item
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html,"html5lib")
	table = soup.find('div',attrs={"class":"panel-body"})
	spans = table.findAll('span')
	tds = table.findAll('td')
	spanL=[]
	tdL=[]

	for span in spans:
		s=span.text	
		if "FY" not in s: 
			spanL.append(s)
		
	for td in tds:	
		t=td.text
		tdL.append(t)
	for x, y in zip(spanL, tdL):
		#print x + " :" + y	
		if  x==  'Market Price':
			print item  + ' :  ' + y.strip()
