from urlparse import urlparse
import validictory
import config
import requests
from service_utils import ValidationFailureException,RequestParseException,InvalidURLException,TimeOutException,RequestMaxedException
import cache

cache_obj = cache.cache()
class RequestProcessor():
    """
    This class processes the request
    """

    def __init__(self):
        self.req_dict={}
    
    def parse_request(self,req_obj):
        """
        This method takes the request object and returns the request dictionary
        """
        try:
            req_data = req_obj.get_json()
            self.req_dict = req_data
            return req_data
        except:
            raise RequestParseException

    def validate_request(self):
        """
        This method validates the req_dict based on validation_spec provided in config
        """

        try:
            validictory.validate(self.req_dict, config.VALIDATION_SPEC)

        except validictory.FieldValidationError:
            raise ValidationFailureException

    def validate_req_cnt(self):
        """
        This method validates the number of requests per clientid
        """
        ClientID = self.req_dict['ClientID']
        if cache_obj.getcnt(ClientID) < config.MAX_COUNT:
            cache_obj.inc_cnt(ClientID)
        else:
            raise RequestMaxedException


    def validate_url(self):
        """
        This method validates the url provided by the client and throws exception if non https url
        """
        url_param = urlparse(self.req_dict['URL'])
        if url_param.scheme=='https':
            return
        else:
            raise InvalidURLException


    def send_Request(self):
        """
        This method sends the request to the url and returns the response
        """
        try:
            url = self.req_dict['URL']
            data = self.req_dict['Request_Body']
            Headers = self.req_dict['Headers']
            req_type = self.req_dict['Request_Type']
            if req_type == 'GET':
                response =  requests.get(url,data,headers = eval(Headers),timeout=config.TIMEOUT)

            elif req_type == 'POST':
                response =  requests.post(url,data,headers=eval(Headers),timeout=config.TIMEOUT)
            return response

        except:
            raise TimeOutException


