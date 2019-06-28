"""
This file stores all the variable which are required to be configurable
"""

#Request Validation Specifications
VALIDATION_SPEC = {"type": "object",
                   "properties":{"ClientID": {'type': 'string',
                                              'required': True
                                             },
                                  "URL":     {'type':'string',
                                              'required':True
                                             },
                                  "Headers": {'type':'string',
                                              'required':True
                                             },
                                  "Request_Type":{'type':'string',
                                                  'required':True
                                                 },
                                  "Request_Body":{'type':'string',
                                                  'required':True
                                                 }

                                }


                   }

#Request Timeout
TIMEOUT = 5

#Number of requests per client can send in a minute
MAX_COUNT = 50

#Port where to start the flask service
PORT = 5000

#Host to host the flask service
HOST = "192.168.56.101"
