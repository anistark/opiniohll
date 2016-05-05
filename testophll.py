# Import classes from your brand new package
from OpinioDelivery import OpinioDelivery

# Create an object of Mammals class & call a method of it
ophll = OpinioDelivery()

# Get All orders / History
# ophll.get_orders()

# Get specific Order
# ophll.get_order('order123')

# Cancel Order
# ophll.cancel_order('order123')

# Create Order
# params = {
#     'merchant_id': 'op-999',
#     'phone': '123',
#     'address': 'HSR',
#     'amount': '12',
#     'amount_to_pay': '12',
#     'locality': 'HSR',
#     'order_code': 'order123',  # optional
#     'latitude': '12.565425',  # optional
#     'longitude': '77.11555',  # optional
#     'poc_phone': '12345',  # optional
#     'poc_name': 'POC Name',  # optional
#     'callback_url': 'https://www.facebook.com',  # optional
#     'subLocationId': '1'  # optional
# }
# ophll.create_order(params)

# Create Merchant
# params = {
#     'name': 'Test Py4',
#     'phone': '123',
#     'address': 'HSR',
#     'email': 'test4@py.com',
#     'latitude': '12.565425',
#     'longitude': '77.11555',
#     'app_merchant_id': '1pp1233'  # optional
# }
# ophll.create_merchant(params)

# Check Merchant status
# ophll.merchant_status('2')

# Serviceability for a merchant
# params = {
#     'merchant_id': '2',
#     'latitude': '12.565425',
#     'longitude': '77.11555'
# }
# ophll.serviceability(params)
