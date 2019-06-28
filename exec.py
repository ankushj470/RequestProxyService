from flask import Flask, request,Response
from urlparse import urlparse
import validictory
import config
import requests

from service_utils import ValidationFailureException,RequestParseException,InvalidURLException,TimeOutException,RequestMaxedException

import cache

app =Flask(__name__)

cache_obj = cache.cache()

@app.route("/proxy_request", methods=["POST","GET"])

def proxy_request():
    try:
        request_dict = parse_request(request)

        validate_request(request_dict)

        validate_req_cnt(request_dict['ClientID'])
        
        #validate_url(request_dict['URL'])

        response = send_Request(request_dict)
        
        resp = response.text

        status = response.status_code        
    
        return Response(resp,status = status, mimetype='application/json')
    
         
    
    except(ValidationFailureException) :
        return Response("Validation Error",status ='400',mimetype='application/json')
    
    except(RequestParseException) :
        return Response("Parsing Error",status ='400',mimetype='application/json')
    
    except(InvalidURLException) :
        return Response("400:Bad Request(Http url not allowed)",status ='400',mimetype='application/json')
    
    except(TimeOutException):
        return Response("Not able to get the data from URL within 5 secs",status ='500',mimetype='application/json')
    
    except(RequestMaxedException):
        return Response("Too many Requests",status ='429',mimetype='application/json')
        

def parse_request(req_obj):
    try:
        req_data = req_obj.get_json()
        return req_data
    except:
        raise RequestParseException

def validate_request(req_dict):
    try:
        validictory.validate(req_dict, config.VALIDATION_SPEC)

    except validictory.FieldValidationError:
        raise ValidationFailureException

def validate_req_cnt(ClientID):
    if cache_obj.getcnt(ClientID) < config.MAX_COUNT:
        cache_obj.inc_cnt(ClientID)
    else:
        raise RequestMaxedException


def validate_url(url):
    url_param = urlparse(url)
    if url_param.scheme=='https':
        return 1
    else:
        raise InvalidURLException
            
        
def send_Request(req_dict):
    try:
        url = req_dict['URL']
        data = req_dict['Request_Body']
        Headers = req_dict['Headers']
        req_type = req_dict['Request_Type']
        if req_type == 'GET':
            response =  requests.get(url,data,headers = eval(Headers),timeout=config.TIMEOUT)

        elif req_type == 'POST':
            response =  requests.post(url,data,headers=eval(Headers),timeout=config.TIMEOUT)
            
        return response

    except:
        raise TimeOutException
    

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='192.168.56.101')
