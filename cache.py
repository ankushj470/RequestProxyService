import datetime

class cache():
    
    def __init__(self):
        self.cached_dict ={}
        
        
    def getcnt(self,clientid):
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
        cur_time = datetime.datetime.now()
        if clientid not in self.cached_dict.keys():
            self.cached_dict[clientid] = [cur_time]

        else:
            self.cached_dict[clientid].insert(0,cur_time)
