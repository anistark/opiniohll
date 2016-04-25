# Import classes from your brand new package
from OpinioDelivery import OpinioDelivery

# Create an object of Mammals class & call a method of it
ophll = OpinioDelivery()

# Get All orders / History
# ophll.get_orders()

# Get specific Order
# ophll.get_order('2203')

# Cancel Order
# ophll.cancel_order('2203')

# Create Order
# params = {
#     'merchant_id': '2',
#     'phone': '123',
#     'address': 'HSR',
#     'amount': '12',
#     'amount_to_pay': '12'
# }
# ophll.create_order(params)

# Create Merchant
# params = {
#     'name': 'Test Py1',
#     'phone': '123',
#     'address': 'HSR',
#     'email': 'test1@py.com',
#     'latitude': '12.565425',
#     'longitude': '77.11555'
# }
# ophll.create_merchant(params)

# Check Merchant status
# ophll.merchant_status('2')

# Serviceability for a merchant
params = {
    'merchant_id': '2',
    'latitude': '12.565425',
    'longitude': '77.11555'
}
ophll.serviceability(params)
