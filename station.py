import math, threading, time, requests, googlemaps, os, json

class API(object):
    def __init__(self, interval=30):
        self.interval=interval
        self.station_status={}
        self.station_information={}
        self.time=time.astime()
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True 
        thread.start() 

    def run(self):
        URL_status = 'https://gbfs.citibikenyc.com/gbfs/en/station_status.json'
        URL_info='https://gbfs.citibikenyc.com/gbfs/en/station_information.json'
        while True:
            self.station_status = requests.get(URL_status).json()['data']['stations']
            self.station_information = requests.get(URL_info).json()['data']['stations']
            self.time = time.asctime()
            print('Arrival Of Fresh Data ->', "|", time.asctime())
            time.sleep(self.interval)

    def getStationStatus(self):
        return self.station_status, self.time

    def getStationInfo(self):
        return self.station_information, self.time
