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


TIMEOUT = 5

MAX_COUNT = 5
