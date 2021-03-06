# All the constants
# Get keys
import config

# All the Base Endpoints
STAGING_URL_HOST = 'test.deliver.opinioapp.com'
PRODUCTION_URL_HOST = 'deliver.opinioapp.com'

ACCESS_KEY = config.ACCESS_KEY
SECRET_KEY = config.SECRET_KEY

# Api Endpoints
API_BASE_ENDPOINT = '/api'
API_VERSION = 'v1'

API_ENDPOINT = API_BASE_ENDPOINT + '/' + API_VERSION + '/orders'
API_MERCHANT_ENDPOINT = API_BASE_ENDPOINT + '/' + API_VERSION + '/merchants'
API_SERVICEABILITY_ENDPOINT = API_BASE_ENDPOINT + '/' + API_VERSION + '/serviceability'
