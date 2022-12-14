#!/usr/bin/env python
# coding: utf8

import requests

"""
This inofficial API is based on the reverse engineering by helvete003
https://github.com/helvete003/bring-api
Thanks for his work!

For information about Bring! please see getbring.com

Everybody feel free to use it, but without any liability or warranty.

Bring! as a Service and Brand is property of Bring! Labs AG
This API was just build because the app is really great and 
its users want to include it in any part of their life.
It can be unavailable when ever Bring! Labs decides to publish an official API,
or want's this API to be disabled.

Until then: Thanks to Bring! Labs for their great service!

Made with ❤ and no ☕ in Germany
"""

import json

class BringApi:
    _bringRestURL = "https://api.getbring.com/rest/v2/"
    _translations = None
    bringUUID=""
    bringListUUID=""
    bearerToken=""
    refreshToken=""
    class AuthentificationFailed(Exception):
        pass

    def __init__(self, email, password):
        print("init")
        try:
            params = {'email': email, 'password': password}
            _headers = {'X-BRING-API-KEY': 'cof4Nc6D8saplXjE3h3HXqHH8m7VU2i1Gs0g85Sp','X-BRING-CLIENT': 'webApp','X-BRING-CLIENT-SOURCE': 'webApp','X-BRING-COUNTRY': 'de','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8' }
            response = requests.post(self._bringRestURL+"bringauth",params=params,headers=_headers)
            response.raise_for_status()
            login = response.json()
            #print(json.dumps(login, indent=4))
            self.bringUUIDbringUUID = login['uuid']
            self.bringListUUID = login['bringListUUID']
            self.bearerToken = login['access_token']
            self.refreshToken = login['refresh_token']
        except (requests.RequestException, KeyError):
            raise self.AuthentificationFailed('email password combination not existing')
            
        
			
        self.headers = {'X-BRING-API-KEY': 'cof4Nc6D8saplXjE3h3HXqHH8m7VU2i1Gs0g85Sp',
                        'X-BRING-CLIENT': 'webApp',
                        'X-BRING-CLIENT-SOURCE': 'webApp',
                        'X-BRING-COUNTRY': 'de',
                        'X-BRING-USER-UUID': self.bringUUID,
                        'Authorization': 'Bearer '+self.bearerToken}
        
        self.addheaders = {'X-BRING-API-KEY': 'cof4Nc6D8saplXjE3h3HXqHH8m7VU2i1Gs0g85Sp',
                           'X-BRING-CLIENT': 'webApp',
                           'X-BRING-CLIENT-SOURCE': 'webApp',
                           'X-BRING-COUNTRY': 'de',
                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                           'X-BRING-USER-UUID': self.bringUUID,
                           'Authorization': 'Bearer  '+self.bearerToken}
    #load all list infos                       
    def load_lists(self):
        return requests.get(f'{self._bringRestURL}bringusers/{self.bringUUID}/lists', headers=self.headers).json()


    #get list of all users in list ID
    def get_users_from_list(self, listUUID):
        return requests.get(f'{self._bringRestURL}bringlists/'+listUUID+'/users', headers=self.headers).json()
    
    #get settings from user
    def get_user_settings(self):
        return requests.get(f'{self._bringRestURL}bringusersettings/{self.bringUUID}', headers=self.headers).json()
    
    #// Hidden Icons? Don't know what this is used for
    def load_products(self):
        return requests.get(f'{self._bringRestURL}bringproducts', headers=self.headers).json()

    #// Found Icons? Don't know what this is used for
    def load_features(self):
        return requests.get(f'{self._bringRestURL}bringusers/{self.bringUUID}/features', headers=self.headers).json()
        
    
    #// Get all items from the shopping list
    def getItems(self,listUUID):
        return requests.get(f'{self._bringRestURL}bringlists/'+listUUID, headers=self.headers).json()
        
    #// Get all items from the shopping list
    def getLocalItems(self,listUUID,locale=None) -> dict:
        items=self.getItems(listUUID)
        if locale:
            self.loadTranslations(locale)
            for item in items['purchase']:
                item['name'] = self._translations.get(item['name']) or item['name']
            for item in items['recently']:
                item['name'] = self._translations.get(item['name']) or item['name']
        return items

        
    #// Get all items from the shopping list
    def getItemsDetails(self,listUUID):
        return requests.get(f'{self._bringRestURL}bringlists/'+listUUID+'/details', headers=self.headers).json()
        
    #// Get all items from the shopping list
    def loadTranslations(self,locale):
        self._translations=requests.get(f'https://web.getbring.com/locale/articles.{locale}.json').json()
        return self._translations
    
    
    #// Add item to list
    def addItem(self,listUUID,itemName,specification):
        files = {'file': f'&purchase={itemName}&recently=&specification={specification}&remove=&sender=null'}
        return requests.put(f'{self._bringRestURL}bringlists/'+listUUID,files=files, headers=self.addheaders)
        
    
    #// Add item to list
    def removeItem(self,listUUID,itemName):
        files = {'file': f'&purchase=&recently=&specification=&remove={itemName}&sender=null'}
        return requests.put(f'{self._bringRestURL}bringlists/'+listUUID,files=files, headers=self.addheaders)