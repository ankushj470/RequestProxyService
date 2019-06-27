from flask import Flask, request,json
app =Flask(__name__)

@app.route("/json_example", methods=["POST"])

def json_example():
    request_dict = parse_request(request)
    validate   
    '''
    req_data = request.get_json()
    ClientID = req_data['ClientID']
    URL = req_data['URL']
    Headers = req_data['Headers']
    Request_type = req_data['Request_type']
    Body = req_data['Request_body']
    
    return <h1>ClientID is {}</h1>
              <h1>URL is {}</h1>
              <h1>Headers are {}</h1>.format(ClientID,URL,Headers)
    '''
    return '''<h1>ClientID is {}</h1>'''.format(request_dict['ClientID'])

def parse_request(req_obj):
    req_data = req_obj.get_json()
    return req_data
    

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='192.168.56.101')
