import mechanize
import urllib2
from bs4 import BeautifulSoup
import sys
url = "http://www.nepalstock.com/todaysprice"

def getData(item):
	try:
		br = mechanize.Browser()
		br.addheaders = [('User-agent', 'Firefox')]
		br.set_handle_robots(False)
		br.set_handle_equiv(False)
		response = br.open(url)
		br.select_form(nr=1)  
		br['stock_symbol'] = item
		response = br.submit()
		html=response.read() 
		soup = BeautifulSoup(html, "lxml")
		dt = soup.find('div', {'id': 'date'})
		print "*** " + dt.text + " ***\n"

		table = soup.find('table', {'class': 'my-table'})
		tds = table.find_all('td')
		return tds
	except:
		print "Error occured... try again after sometime"
		exit(0)
def dispStock(item):
	tds=getData(item)
	print tds[3].text + " : " +tds[4].text
	print tds[5].text + " : " +tds[6].text
	print tds[7].text + " : " +tds[8].text 
	print tds[9].text + " : " +tds[10].text 
	print tds[11].text + " : "+ tds[12].text 
	print tds[13].text + " : "+ tds[14].text 
	print tds[15].text + " : " +tds[16].text 
	print tds[17].text + " : " +tds[18].text 
	print tds[19].text + " : "+ tds[20].text
	print tds[21].text + " : "+ tds[22].text
	print tds[23].text + " : " +tds[24].text 
	print tds[25].text + " : "+ tds[26].text 


#Name:
def getName(tds):
	return tds[3].text + " : " +tds[4].text

#Address 
def getAddr(tds):
	return tds[5].text + " : " +tds[6].text

#Email
def getEmail(tds):
	return tds[7].text + " : " +tds[8].text 

#Website
def getSite(tds):
	return tds[9].text + " : " +tds[10].text 

#Last Traded Price (Rs.)
def getStock(item):
	tds=getData(item)
	print getName(tds)
	print getAddr(tds)
	print getEmail(tds)
	print getSite(tds)
	return tds[11].text + " : "+ tds[12].text + " & " + tds[13].text + " : "+ tds[14].text

#Change (Rs.) and (%)
def getChage(item):
	tds=getData(item)
	return tds[13].text + " : "+ tds[14].text 
#Total Listed Shares

def getTotalListedShares(item):
	tds=getData(item)
	return tds[15].text + " : " +tds[16].text 
#Total Bonus Shares

def getTotalBonusShares(item):
	tds=getData(item)
	return tds[17].text + " : " +tds[18].text 
	
#Paid Up Value (Rs.)
def getPaidValue(item):
	tds=getData(item)
	return tds[19].text + " : "+ tds[20].text
	
#Total Paid Up Value (Rs.)
def getTotalPaidValue(item):
	tds=getData(item)
	return tds[21].text + " : "+ tds[22].text
#Closing Market Price (Rs.)
def getClosingValue(item):
	tds=getData(item)
	return tds[23].text + " : " +tds[24].text 
#Market Capitalization (Rs.)
def getMarketCap(item):
	tds=getData(item)
	return tds[25].text + " : "+ tds[26].text 

#dispStock("SBI")	
#print(getStock("SBI"))
#print(getStock(sys.argv[1]))