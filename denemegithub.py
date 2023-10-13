import requests
class deneme:
    def __init__(self):
        self.api_url='https://api.github.com'
        self.token='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'

    def finduser(self,name):
        response=requests.get(self.api_url+'/users/'+name)
        return response.json()#jsonlamamız lazım siteden veri çekme..

    
    def getrep(self,name):
        response=requests.get(self.api_url+'/users/'+name+'/repos/')
        return response.json()
    
    def createrep(self,name):
        response=requests.post(self.api_url+'/users/repos?acces_token='+self.token,json={
            "name":name,
            "description":"This is your first repository",
            "private":False,
            "has_wiki":True
        })
        return response

called=deneme()

while True:
    choose=(input("1-Finduser\n 2-Getrep\n 3-Createres \n 4-Exit\n:"))

    if choose=="1":
        name=input("Please enter username:")
        result=called.finduser(name)
        print(f"Username:{result['login']}followers:{['followers']}following:{['following']}")
    elif choose=="2":
        name=input("Please enter username:")
        result=called.finduser(name)
        print(f"Username:{result['name']}")
    elif choose=="3":
        name=input('rep name:')
        result=called.createrep(name)
        print(result)
    else:
        break