# All Packages required
import requests
import ujson as json
import urllib
import collections
import hmac
import hashlib
from base64 import b64encode
from constants import API_ENDPOINT, API_MERCHANT_ENDPOINT, API_SERVICEABILITY_ENDPOINT, STAGING_URL_HOST, PRODUCTION_URL_HOST
from .errors import HTTPError


class OpinioDelivery:
    def __init__(self, access_key, secret_key, sandbox=False, debug=False):
        self.ACCESS_KEY = access_key
        self.SECRET_KEY = secret_key
        if sandbox:
            self.SERVER_HOST = STAGING_URL_HOST
        else:
            self.SERVER_HOST = PRODUCTION_URL_HOST
        self.API_ENDPOINT = 'http://'+self.SERVER_HOST+API_ENDPOINT
        self.API_MERCHANT_ENDPOINT = 'http://'+self.SERVER_HOST+API_MERCHANT_ENDPOINT
        self.API_SERVICEABILITY_ENDPOINT = 'http://'+self.SERVER_HOST+API_SERVICEABILITY_ENDPOINT
        self.DEBUG = debug

    def get_req_header(self, params, method, path):
        if params:
            sorted_params = collections.OrderedDict(sorted(params.items()))
            qstring = '&'+urllib.urlencode(sorted_params)
            qstring = qstring.replace('+', '%20')
            qstring = qstring.replace('*', '%2A')
            qstring = qstring.replace('%7E', '~')
        else:
            qstring = ''
        encode_request = '\n'.join([
            method,
            self.SERVER_HOST,
            path,
            self.ACCESS_KEY,
            qstring,
            '&SignatureVersion=1',
            '&SignatureMethod=HmacSHA1'])
        sig = hmac.new(self.SECRET_KEY, encode_request, hashlib.sha1)
        auth_key = "Opinio "+self.ACCESS_KEY+":"+b64encode(sig.digest())
        headers = {"Authorization": auth_key}
        return headers

    def _get_repsonse_dict(self, response):
        if response.status_code not in [200, 201]:
            raise HTTPError(response.content)
        return json.loads(response.content)

    def create_order(self, params):
        if self.DEBUG:
            print '-- Create New Order --'
        headers = self.get_req_header(params, 'POST', API_ENDPOINT)
        response = requests.post(self.API_ENDPOINT, data=params, headers=headers)
        if self.DEBUG:
            print response.content
        return self._get_repsonse_dict(response)

    def get_order(self, order_id):
        if self.DEBUG:
            print '-- Getting Order '+order_id+' --'
        headers = self.get_req_header({}, 'GET', API_ENDPOINT+'/'+order_id)
        response = requests.get(self.API_ENDPOINT+'/'+order_id, headers=headers)
        if self.DEBUG:
            print response.content
        return self._get_repsonse_dict(response)

    def cancel_order(self, order_id):
        if self.DEBUG:
            print '-- Cancelling Order '+order_id+' --'
        params = {'is_cancelled': 1}
        headers = self.get_req_header(params, 'PUT', API_ENDPOINT+'/'+order_id)
        response = requests.put(self.API_ENDPOINT+'/'+order_id, data=params, headers=headers)
        if self.DEBUG:
            print response.content
        return self._get_repsonse_dict(response)

    def get_orders(self):
        if self.DEBUG:
            print '-- Getting All Orders --'
        headers = self.get_req_header({}, 'GET', API_ENDPOINT)
        if self.DEBUG:
            print headers
        response = requests.get(self.API_ENDPOINT, headers=headers)
        if self.DEBUG:
            print response.content
        return self._get_repsonse_dict(response)

    def create_merchant(self, params):
        if self.DEBUG:
            print '-- Create New Merchant --'
        headers = self.get_req_header(params, 'POST', API_MERCHANT_ENDPOINT)
        response = requests.post(self.API_MERCHANT_ENDPOINT, data=params, headers=headers)
        if self.DEBUG:
            print response.content
        return self._get_repsonse_dict(response)

    def merchant_status(self, merchant_id):
        if self.DEBUG:
            print '-- Getting Merchant Status '+merchant_id+' --'
        headers = self.get_req_header({}, 'GET', API_MERCHANT_ENDPOINT+'/'+merchant_id)
        response = requests.get(self.API_MERCHANT_ENDPOINT+'/'+merchant_id, headers=headers)
        if self.DEBUG:
            print response.content
        return self._get_repsonse_dict(response)

    def serviceability(self, params):
        if self.DEBUG:
            print '-- Serviceability --'
            print API_SERVICEABILITY_ENDPOINT
            print '++++++++++++++++++'
        headers = self.get_req_header(params, 'GET', API_SERVICEABILITY_ENDPOINT)
        response = requests.get(self.API_SERVICEABILITY_ENDPOINT, params=params, headers=headers)
        if self.DEBUG:
            print response.content
        return self._get_repsonse_dict(response)
