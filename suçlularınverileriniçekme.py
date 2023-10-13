import requests

class succriminal():
    def __init__(self,area,date,criminaltype='crimeallm'):
        self.area=area
        self.date=date
        self.criminaltype=criminaltype
        self.call=self.criminalfind()
        
    def criminalfind(self):
        url="https://data.police.uk/docs/method/crimes-no-location/"
        mericparams={
            'category':self.criminaltype,
            'force':self.area,
            'date':self.date
        }
        response=requests.get(url,params=mericparams)
        return response.json()
    
sr=succriminal('city-of-london','2020-01')
print(sr.call)
