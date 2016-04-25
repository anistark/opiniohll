# All Packages required
import requests
import ujson as json
import urllib
import collections
import hmac
import hashlib
from base64 import b64encode
from constants import API_ENDPOINT, PRODUCTION_HOST, TESTING_HOST, LOCAL_HOST, ACCESS_KEY, SECRET_KEY, API_MERCHANT_ENDPOINT, API_SERVICIBILITY_ENDPOINT
from .errors import HTTPError


class OpinioDelivery:
    def __init__(self):
        # Create some member animals
        self.SERVER_HOST = LOCAL_HOST
        self.ACCESS_KEY = ACCESS_KEY
        self.SECRET_KEY = SECRET_KEY
        self.API_ENDPOINT = 'http://'+self.SERVER_HOST + API_ENDPOINT
        self.API_MERCHANT_ENDPOINT = 'http://'+self.SERVER_HOST + API_MERCHANT_ENDPOINT
        self.API_SERVICIBILITY_ENDPOINT = 'http://'+self.SERVER_HOST + API_SERVICIBILITY_ENDPOINT

    def get_req_header(self, params, method, path):
        if params:
            sorted_params = collections.OrderedDict(sorted(params.items()))
            qstring = '&'+urllib.urlencode(sorted_params)
        else:
            qstring = ''
        encode_request = '\n'.join([method, self.SERVER_HOST, path, self.ACCESS_KEY, qstring, '&SignatureVersion=1', '&SignatureMethod=HmacSHA1'])
        sig = hmac.new(self.SECRET_KEY,encode_request,hashlib.sha1)
        auth_key = "Opinio "+self.ACCESS_KEY+":"+b64encode(sig.digest())
        headers = {"Authorization": auth_key}
        return headers

    def _get_repsonse_dict(self, response):
        if not response.status_code in [200, 201]:
            raise HTTPError(response.content)
        return json.loads(response.content)

    def create_order(self, params):
        print '-- Create New Order --'
        headers = self.get_req_header(params, 'POST', API_ENDPOINT)
        response = requests.post(self.API_ENDPOINT, data=params, headers=headers)
        print response.content
        return self._get_repsonse_dict(response)

    def get_order(self, order_id):
        print '-- Getting Order '+order_id+' --'
        headers = self.get_req_header({}, 'GET', API_ENDPOINT+'/'+order_id)
        response = requests.get(self.API_ENDPOINT+'/'+order_id, headers=headers)
        print response.content
        return self._get_repsonse_dict(response)

    def cancel_order(self, order_id):
        print '-- Cancelling Order '+order_id+' --'
        params = {'is_cancelled':1}
        headers = self.get_req_header(params, 'PUT', API_ENDPOINT+'/'+order_id)
        response = requests.put(self.API_ENDPOINT+'/'+order_id, data=params, headers=headers)
        print response.content
        return self._get_repsonse_dict(response)

    def get_orders(self):
        print '-- Getting All Orders --'
        headers = self.get_req_header({}, 'GET', API_ENDPOINT)
        print headers
        response = requests.get(self.API_ENDPOINT, headers=headers)
        print response.content
        return self._get_repsonse_dict(response)

    def create_merchant(self, params):
        print '-- Create New Merchant --'
        headers = self.get_req_header(params, 'POST', API_MERCHANT_ENDPOINT)
        response = requests.post(self.API_MERCHANT_ENDPOINT, data=params, headers=headers)
        print response.content
        return self._get_repsonse_dict(response)

    def merchant_status(self, merchant_id):
        print '-- Getting Merchant Status '+merchant_id+' --'
        headers = self.get_req_header({}, 'GET', API_MERCHANT_ENDPOINT+'/'+merchant_id)
        response = requests.get(self.API_MERCHANT_ENDPOINT+'/'+merchant_id, headers=headers)
        print response.content
        return self._get_repsonse_dict(response)

    def serviceability(self, params):
        print '-- Serviceability --'
        print params
        headers = self.get_req_header({}, 'GET', API_SERVICIBILITY_ENDPOINT)
        response = requests.get(self.API_SERVICIBILITY_ENDPOINT, params=params, headers=headers)
        print response.content
        return self._get_repsonse_dict(response)
