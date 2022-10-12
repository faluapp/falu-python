from abc import abstractmethod
from urllib.request import Request


class IAuthenticationProvider(object):

    @abstractmethod
    def process(self, request: Request):
        """
        Process a request before sending
        """
        pass


class EmptyAuthenticationHeaderProvider(IAuthenticationProvider):
    def process(self, request: Request):
        # nothing to do here
        return request


class AuthenticationHeaderProvider(IAuthenticationProvider):

    def __init__(self, scheme="Bearer"):
        self.scheme = scheme

    def process(self, request: Request):
        parameter = self.get_parameter(request)
        request.add_header("Authorization", "{} {}".format(self.scheme, parameter))
        return request

    @abstractmethod
    def get_parameter(self, request):
        pass
