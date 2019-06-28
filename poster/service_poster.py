import requests
import poster_input

'''
clientid = 
url = 
Headers = raw_input("Please enter the Headers")
Request_Type = raw_input("Enter the Request Type")
Request_Body = raw_input("Please Enter the Request Body")
'''

data = {"ClientID":poster_input.ClientID,"URL":poster_input.URL,"Headers":poster_input.Headers,"Request_Type":poster_input.Request_Type,"Request_Body":poster_input.Request_Body}


response  = requests.post("http://192.168.56.101:5000/proxy_request",json = data)

print "Response Status Code : {} \nResponse Content : {}".format(response.status_code,response.content)
