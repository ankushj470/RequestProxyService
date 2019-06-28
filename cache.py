import datetime

class cache():
    """
    This class is used to cache the request from clients based on clientid
    """
    
    def __init__(self):
        self.cached_dict ={}
        
        
    def getcnt(self,clientid):
        """
        This method returns the count of request from a given clientid in last 1 minute
        """
        count=0
        cur_time = datetime.datetime.now()
        if clientid in self.cached_dict.keys():
            for req in self.cached_dict[clientid]:
                if cur_time - (req) > datetime.timedelta(minutes=1):
                    break
                else:
                    count+=1

        return count
            
        
        

    def inc_cnt(self,clientid):
        """
        This method adds the timestamp of the request for the clientid to track number of requests
        """
        cur_time = datetime.datetime.now()
        if clientid not in self.cached_dict.keys():
            self.cached_dict[clientid] = [cur_time]

        else:
            self.cached_dict[clientid].insert(0,cur_time)
