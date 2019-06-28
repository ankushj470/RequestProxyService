from flask import Flask, request,Response
import request_processor
from service_utils import ValidationFailureException,RequestParseException,InvalidURLException,TimeOutException,RequestMaxedException
import config
app =Flask(__name__)

@app.route("/proxy_request", methods=["POST","GET"])

def proxy_request():
    try:
        req_proc_obj = request_processor.RequestProcessor()
        request_dict = req_proc_obj.parse_request(request)

        req_proc_obj.validate_request()

        req_proc_obj.validate_req_cnt()
        
        req_proc_obj.validate_url()

        response = req_proc_obj.send_Request()
        
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
        

if __name__ == '__main__':
    app.run(debug=True,port=config.PORT,host=config.HOST)
