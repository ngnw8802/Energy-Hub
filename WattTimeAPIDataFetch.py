import requests
import sys
from os import path
from requests.auth import HTTPBasicAuth

#CL INPUT CHECK
if len(sys.argv) == 1:
    print("\n\nproper use to get historical data from any BA is: python3 WattTimeAPIDataFetch.py [balancing authority you want]\n\n")
    quit() 

#THIS LOGS YOU IN AND GIVES YOU YOUR TOKEN
login_url = 'https://api2.watttime.org/v2/login'
token = requests.get(login_url, auth=HTTPBasicAuth('justin_energyhub', '4OXv0yc96zHRLLG*ve5mN6ykNp8UNd5'))


#THIS REQUESTS HISTORICAL DATA AND STORES IT IN LOCAL DIRECTORY IN ZIP FORM
historical_url = 'https://api2.watttime.org/v2/historical'
headers = {'Authorization': 'Bearer {}'.format(token)}
ba = sys.argv[1]
params = {'ba': ba}

#THIS IS THE REQUEST
rsp = requests.get(historical_url, headers=headers, params=params)
cur_dir = path.dirname(path.realpath('__file__'))
file_path = path.join(cur_dir, '{}_historical.zip'.format(ba))
with open(file_path, 'wb') as fp:
    fp.write(rsp.content)

print('Wrote historical data for {} to {}'.format(ba, file_path))
