"""
pgoapi - Pokemon Go API
Copyright (c) 2016 tjado <https://github.com/tejado>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

Author: tjado <https://github.com/tejado>
"""


class AuthException(Exception):
    pass


class NotLoggedInException(Exception):
    pass


class ServerBusyOrOfflineException(Exception):
    pass


class PleaseInstallProtobufVersion3(Exception):
    pass


class NoPlayerPositionSetException(Exception):
    pass


class EmptySubrequestChainException(Exception):
    pass


class ServerSideRequestThrottlingException(Exception):
    pass


class ServerSideAccessForbiddenException(Exception):
    pass


class UnexpectedResponseException(Exception):
    pass


class AuthTokenExpiredException(Exception):
    pass
	
class HashServerException(Exception):
    """Parent class of all hashing server errors"""
	
class BadRequestException(Exception):
    """Raised when HTTP code 400 is returned"""

class BadHashRequestException(BadRequestException):
    """Raised when hashing server returns code 400"""
	
class BannedAccountException(Exception):
    """Raised when an account is banned"""
	
class MalformedResponseException(Exception):
    """Raised when the response is empty or not in an expected format"""

class MalformedNianticResponseException(Exception):
    """Raised when a Niantic response is empty or not in an expected format"""

class MalformedHashResponseException(Exception):
    """Raised when the response from the hash server cannot be parsed."""
	
class HashingOfflineException(Exception):
    """Raised when unable to establish a conection with the hashing server"""

class HashingForbiddenException(Exception):
    """Raised when the hashing server returns 403"""

class TempHashingBanException(Exception):
    """Raised when your IP is temporarily banned for sending too many requests with invalid keys."""
	
class HashingQuotaExceededException(Exception):
    """Raised when you exceed your hashing server quota"""
	
class UnexpectedHashResponseException(Exception):
    """Raised when an unhandled HTTP code is received from the hash server"""

class ServerApiEndpointRedirectException(Exception):
    def __init__(self):
        self._api_endpoint = None

    def get_redirected_endpoint(self):
        return self._api_endpoint

    def set_redirected_endpoint(self, api_endpoint):
        self._api_endpoint = api_endpoint
