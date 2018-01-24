from datetime import datetime
import requests, bs4

import SendMessage

class TrainStatus:

	def __init__(self, all):
		self.stations = {'depart':'',
						 'arrive':''}
		self.date = ''
		self.url = ''
		self.all = all

	def setStations(self, depart, arrive):
		self.stations['depart'] = depart
		self.stations['arrive'] = arrive
		
	def setDefaultStations(self):
		if datetime.now().hour < 8:
			self.setStations('EWE', 'LBG')
		else:
			self.setStations('LBG', 'EWE')
	
	def setDate(self):
		if datetime.now().hour < 8:			
			hour = '0700'
		else:
			hour = '1700'
			
		d = datetime.today()
		self.date = '/' + str(d.year) + '/' + '{:02d}'.format(d.month) + '/' + '{:02d}'.format(d.day) + '/' + hour		

	def buildUrl(self):

		url = 'http://www.realtimetrains.co.uk/search/advanced/{0}/to/{1}{2}'.format(self.stations['depart'], self.stations['arrive'], self.date)
		
		self.url = url

	def scrapeRTT(self):		
		text = ''
		res = requests.get(self.url)
		
		try: 
			res.raise_for_status()
		except requests.exceptions.HTTPError:
			text = 'Invalid arguments "{0}" and "{1}"'.format(self.stations['depart'], self.stations['arrive'])
			
		trainSoup = bs4.BeautifulSoup(res.text, 'html5lib')	
		trainElem = trainSoup.select('tr[class="wtt call_public"]')
		
		for elem in trainElem:		
			if elem.find_all('td', class_='realtime')[0].getText() == 'Cancel':
				text += '\n{0} to {1} is cancelled. '.format(elem.find_all('td', class_='time public')[0].getText() , elem.find_all('td', class_='location')[1].getText())
			elif self.all == True:
				text += '\n{0} to {1} is not cancelled. '.format(elem.find_all('td', class_='time public')[0].getText() , elem.find_all('td', class_='location')[1].getText())
		
		if text == '' and self.all == True:
			text = 'No data found.'

		return text
	
if __name__ == '__main__':
	trainStatus = TrainStatus(True)
	
	trainStatus.setDefaultStations()
	trainStatus.setDate()
	
	trainStatus.buildUrl()
	text = trainStatus.scrapeRTT()
	
	if text != '':
		SendMessage.sendMessage(text)