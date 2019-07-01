#RequestProxyService
Request Proxy Service acts like a typical proxy to replay an HTTPS request to specified URL and returns back the response.

#Prerequisite
This service is made on Python 2.7.10 and flask 0.10.1

You should have following modules to run this service:

1. flask
2. requests
3. urlparse
4. validictory


#Steps to Run Service
Please Follow following steps to run service:

1. Run exec.py file : python exec.py (Currently host is given in localhost and port =5000, to change please change HOST and PORT value in config.py file)
   This step will run the flask service

2. To run the sample input: python poster/service_poster.py (service_poster fetches the sample input from poster_input.py,please change the input based on your testing data)
   This step will post the request to our RequestProxyService with sample data given in poster_input.py file


