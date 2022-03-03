'''

Video Streaming Plans
Given a class for a BasicPlan, write the classes for StandardPlan and PremiumPlan which have class attributes of the following:

BasicPlan	StandardPlan	Premium Plan
✓	✓	✓	can_stream
✓	✓	✓	can_download
✓	✓	✓	has_SD
✓	✓	has_HD
✓	has_UHD
1	2	4	num_of_devices
$8.99	$12.99	$15.99	price
'''


class BasicPlan:
    can_stream = True
    can_download = True
    num_of_devices = 1
    has_SD = True
    has_HD = False
    has_UHD = False
    price = '$8.99'


class StandardPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '$12.99'


class PremiumPlan(BasicPlan):
    has_HD = True
    num_of_devices = 4
    price = '$15.99'


def bit_length(self):
    s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
    s = s.lstrip('-0b') # remove leading zeros and minus sign
    return len(s)
print(bit_length(-37))



import requests

url = "https://docs.solarisbank.com/5w3pledb/api/v1/#5Sq3SDBB-post-create-repayment-plans"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))