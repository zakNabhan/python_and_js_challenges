'''

Given a class for a BasicPlan, write the classes for StandardPlan and PremiumPlan which have class attributes of the following:

BasicPlan	StandardPlan	Premium Plan
✓	           ✓	            ✓	        can_stream
✓	          ✓	               ✓	        can_download
✓	          ✓               	✓	            has_SD
✓	✓	    has_HD
✓	        has_UHD
1	2	4	num_of_devices
$8.99	$12.99	$15.99	price


'''


class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devies = 1
    price = '8.99$'


class StandardPlan(BasicPlan):
    has_HD = True
    num_of_devies = 2
    price = '$12.99'


class PremiumPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devies = 4
    price = '$15.99	'


print(BasicPlan.has_SD)
print(PremiumPlan.has_SD)
print(BasicPlan.has_UHD)
print(BasicPlan.price)
print(PremiumPlan.num_of_devies)