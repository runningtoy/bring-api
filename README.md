# bring-api
Fork of Python version  by (philipp2310)[https://github.com/philipp2310/bring-api]  

Incomplete, reverse-engineered and unofficial Bring! API

Updated Version to Api V2

### Credits
Reverse Engineering   by helvet003<br/>
PHP version   by helvet003<br/>
Example: https://twitter.com/HelveteD/status/836262765719347202



Node version by foxriver76<br/>
https://github.com/foxriver76/node-bring-api


### Example

'''

from BringApi import BringApi 
import json

bring = BringApi("USERNAME","PASSWORD")

bring.addItem("XXXXXXXX-XXXX-XXXX-XXXX-xxxxxxxxxxxx","Smarthome","python")
bring.removeItem("XXXXXXXX-XXXX-XXXX-XXXX-xxxxxxxxxxxx","Smarthome","python")


shoppinglist=bring.getLocalItems("XXXXXXXX-XXXX-XXXX-XXXX-xxxxxxxxxxxx","de-DE")

with open('completeShoppinglist.json', 'w', encoding ='utf8') as json_file:
    json.dump(shoppinglist, json_file,ensure_ascii = True,sort_keys=True)

with open('purchaseShoppinglist.json', 'w', encoding ='utf8') as json_file:
    json.dump(shoppinglist["purchase"], json_file,ensure_ascii = True,sort_keys=True)

'''
