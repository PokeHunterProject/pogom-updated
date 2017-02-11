from __future__ import absolute_import

import ctypes
import json
import base64
import requests
import time

from .hash_engine import HashEngine
from .exceptions import ServerBusyOrOfflineException, ServerSideAccessForbiddenException, UnexpectedResponseException

class HashServer(HashEngine):

    def __init__(self, auth_token):
        self.status = {}
        self.endpoint = "http://pokehash.buddyauth.com/api/v125/hash"
        self.headers = {'content-type': 'application/json', 'Accept' : 'application/json', 'X-AuthToken' : auth_token}

        self._session = requests.session()
		
        self._session.verify = True
        self._session.headers.update({'User-Agent': 'PokeHunter Scanning API'})

    def hash(self, timestamp, latitude, longitude, altitude, authticket, sessiondata, requestslist):
        self.location_hash = None
        self.location_auth_hash = None
        self.request_hashes = []

        payload = {}
        payload["Timestamp"] = json.dumps(timestamp)
        payload["Latitude"] = latitude
        payload["Longitude"] = longitude
        payload["Altitude"] = altitude
        payload["AuthTicket"] = base64.b64encode(authticket)
        payload["SessionData"] = base64.b64encode(sessiondata)
        payload["Requests"] = []
        for request in requestslist:
            payload["Requests"].append(base64.b64encode(request.SerializeToString()))

        # ask hash server how is it going ? and get json
        try:
            response_raw = self._session.post(self.endpoint, json=payload, headers=self.headers, timeout=10)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as error:
            raise ServerBusyOrOfflineException(error)
			
        headers = response_raw.headers
        try:
            self.status['period'] = int(headers.get('X-RatePeriodEnd'))
            self.status['remaining'] = int(headers.get('X-RateRequestsRemaining'))
            self.status['maximum'] = int(headers.get('X-MaxRequestCount'))
        except TypeError:
            pass

        if response_raw.status_code == 400:
            raise UnexpectedResponseException("400 : Bad request, error = " + response_raw.content)
        elif response_raw.status_code == 401:
            raise ServerSideAccessForbiddenException("401 : You are not authorized to use this service")
        elif response_raw.status_code == 429:
            print('\nAPI Request Limit Reached\n')
            print('Time left (sec): ' + str(self.status['period'] - int(time.time())))
            print('Requests remaining: ' + str(self.status['remaining']))
            print('Max requests: ' + str(self.status['maximum']) + '\n')
            raise ServerSideAccessForbiddenException("429 : Request limited, error = " + response_raw.content)
        elif response_raw.status_code != 200:
            error = 'Unexpected HTTP server response - needs 200 got {}'.format(response_raw.status_code)
            raise UnexpectedResponseException(error)

        if response_raw.content is None:
            raise UnexpectedResponseException

        reponse_parsed = json.loads(response_raw.content)
        self.location_auth_hash = ctypes.c_int32(reponse_parsed['locationAuthHash']).value
        self.location_hash = ctypes.c_int32(reponse_parsed['locationHash']).value

        for request_hash in reponse_parsed['requestHashes']:
            self.request_hashes.append(ctypes.c_int64(request_hash).value)
			
        print('Requests remaining: ' + str(self.status['remaining']))
