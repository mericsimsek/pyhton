import requests

class Github:
    def __init__(self):
        self.api_url='https://api.github.com'
        self.token='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'
    def getuser(self,username):
        response=requests.get(self.api_url+'/users/'+username)#github/users/mericsimsek kodları buraya taşır
        return response.json()
    
    def getrep(self,username):
        response=requests.get(self.api_url+'/users/'+username+'/repos/')#github/users/mericsimsek kodları buraya taşır
        return response.json()
    
    def createrep(self,username):
        response=requests.post(self.api_url+'/users/repos?acces_token='+self.token,json={
            "name":name,
            "description":"This is your first repository",
            "private":False,
            "has_wiki":True
        })#kodları gönderecek bu sefer yani post
        return response

hub=Github()


while True:
    secim=input('1-finduser\n2-get res.\n3-create res.\n4-exit\nsecim:')

    if secim=='4':
        break
    else:
        if secim=='1':
            username=input('username:')
            result=hub.getuser(username)
            print(f"name:{result['login']}public repos:{result['public_gists']}createdat:{result['created_at']}")
        elif secim=='2':
            username=input('username:')
            result=hub.getrep(username)
            print(f"name:{result['name']}")
        elif secim=='3':
            name=input('rep name:')
            result=hub.createrep(name)
            print(result)
        else:
            print('yanlis secim')