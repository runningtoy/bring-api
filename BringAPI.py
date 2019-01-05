import requests
"""
This inofficial API is based on the reverse engineering by helvete003
https://github.com/helvete003/bring-api
"""

class BringApi:
    bringRestURL = "https://api.getbring.com/rest/"
    # to be filled by secrets
    bringUUID = ""
    bringListUUID = ""
    answerHttpStatus = -1

    def __init__(self, uuid, bringuuid, use_login = False):
        if use_login:
            log = self.login(uuid,bringuuid)
            if log.status_code == 200:
                log = log.json()
                self.bringUUID = log['uuid'];
                self.bringListUUID = log['bringListUUID']
            else:
                print("Wrong Login!")
        else:
            self.bringUUID = uuid
            self.bringListUUID = bringuuid
        self.headers = {    'X-BRING-API-KEY': 'cof4Nc6D8saplXjE3h3HXqHH8m7VU2i1Gs0g85Sp',
                            'X-BRING-CLIENT': 'android',
                            'X-BRING-USER-UUID': self.bringUUID,
                            'X-BRING-VERSION': '303070050',
                            'X-BRING-COUNTRY': 'de' }
        self.addheaders = { 'X-BRING-API-KEY': 'cof4Nc6D8saplXjE3h3HXqHH8m7VU2i1Gs0g85Sp',
                            'X-BRING-CLIENT': 'android',
                            'X-BRING-USER-UUID': self.bringUUID,
                            'X-BRING-VERSION': '303070050',
                            'X-BRING-COUNTRY': 'de',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    def login(self, email, password):
        params = {'email': email, 'password': password}
        return requests.get(self.bringRestURL+"bringlists",params=params)
        #return $this->request(self::GET_REQUEST,"bringlists","?email=".$email."&password=".$password);
    
    def get_items(self):
        return requests.get(self.bringRestURL + "bringlists/"+self.bringListUUID, headers=self.headers)
        #return $this->request(self::GET_REQUEST,"bringlists/".$this->bringListUUID,"",true);

    def save_item(self, item, specification):
        files = {'file': "&purchase="+item+"&recently=&specification="+specification+"&remove=&sender=null"}
        print(files)
        return requests.put(self.bringRestURL + "bringlists/"+self.bringListUUID, files=files, headers=self.addheaders)
        #return $this->request(self::PUT_REQUEST,"bringlists/".$this->bringListUUID,"purchase=".$itemName."&recently=&specification=".$specification."&remove=&sender=null",true);

    def recent_item(self, item):
        files = {'file': "&purchase=&recently="+item+"&specification=&remove=&sender=null"}
        print(files)
        return requests.put(self.bringRestURL + "bringlists/"+self.bringListUUID, files=files, headers=self.addheaders)

    def remove_item(self, item):
        files = {'file': "&purchase=&recently=&specification=&remove="+item+"&sender=null"}
        print(files)
        return requests.put(self.bringRestURL + "bringlists/"+self.bringListUUID, files=files, headers=self.addheaders)
        #return $this->request(self::PUT_REQUEST,"bringlists/".$this->bringListUUID, "purchase=&recently=&specification=&remove=".$itemName."&sender=null",true);

    def search_item(self, search):
        params = {'listUuid': self.bringListUUID, 'itemId': search}
        return requests.get(self.bringRestURL + "bringlistitemdetails/", params=params, headers=self.headers)
        #return $this->request(self::GET_REQUEST,"bringlistitemdetails/", "?listUuid=".$this->bringListUUID."&itemId=".$search,true);

    #// Hidden Icons? Don't know what this is used for
    def load_products(self):
      return requests.get(self.bringRestURL+"bringproducts", headers=self.headers)
      #return $this->request(self::GET_REQUEST,"bringproducts", "",true);

    #// Found Icons? Don't know what this is used for
    def load_features(self):
      return requests.get(self.bringRestURL+"bringusers/"+self.bringUUID+"/features", headers=self.headers)
      #return $this->request(self::GET_REQUEST,"bringusers/".$this->bringUUID."/features", "",true);

    def load_lists(self):
        return requests.get(self.bringRestURL+"bringusers/"+self.bringUUID+"/lists", headers=self.headers)
        #return $this->request(self::GET_REQUEST,"bringusers/".$this->bringUUID."/lists", "",true);

    def get_users_from_list(self, listUUID):
        return requests.get(self.bringRestURL+"bringlists/"+listUUID+"/users", headers=self.headers)
        #return $this->request(self::GET_REQUEST,"bringlists/".$listUUID."/users", "",true);

    def get_user_settings(self):
        return requests.get(self.bringRestURL+"bringusersettings/"+self.bringUUID, headers=self.headers)
        #return $this->request(self::GET_REQUEST,"bringusersettings/".$this->bringUUID, "",true);

