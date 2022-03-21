# author: ononemli

from requests import get
import json
from pyfiglet import Figlet

url1 = 'http://ipinfo.io/json'
response = get(url1)
data = json.loads(response.text)

ip = data['ip']
hostname = data['hostname']
city = data['city']
region = data['region']
country = data['country']
loc = data['loc']
org = data['org']
postal = data['postal']
timezone = data['timezone']

title = Figlet(font='digital')
print(title.renderText('IP Info - ononemli'))

print('IP Address: ' '\t'+ip+ '\n' + 'Hostname: ' '\t'+hostname + '\n''City: ' '\t''\t'+city + '\n''Region: ' '\t'+region + '\n''Country: ' '\t'+country + '\n''Location: ' '\t'+loc + '\n''ISP: ' '\t''\t'+org + '\n''Postal Code: ' '\t'+postal + '\n''Timezone: ' '\t'+timezone)

input('\n''Press enter to exit')
if input: exit()