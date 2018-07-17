import json
import sys

import requests

data = {
    'MachineName': 'Jeffs Enigma',
    'Text':sys.argv[2],
    'Rotor1':{
        'RotorNum':'5',
        'Setting':'f'
    },
    'Rotor2':{
        'RotorNum':'4',
        'Setting':'d'
    },
    'Rotor3':{
        'RotorNum':'3',
        'Setting':'z'
    },
    'Plugboard': {
        'Wiring': {'a':'h', 'r':'t', 's':'e', 'w':'f', 'c':'p', 'i':'b'}
    }
}

url = None
if sys.argv[1] == 'azure':
    url = 'https://enigmamachinerestapi.azurewebsites.net/'
else:
    url = 'http://localhost:61467/'

endpoint = 'api/Enigma/Encrypt?leaveWhiteSpace=true'
response = requests.post(url + endpoint, json=data)

#print(f'http status: {response.status_code}')
print(response.text.replace('"', ''))
