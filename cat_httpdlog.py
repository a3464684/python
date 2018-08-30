import re
r =r'^(?P<host>\S+).*\s(?P<status>\d+)\s(?P<length>\d+).*(?=\n)'
class MyFile():
    def __init__(self,x):
        self.f = open(x,'r')
    
    def _read_data(self):
        self.data = self.f.readlines()
        return self.data
    
    def match_data(self):
        self.my_dict={}
        for i in self._read_data():
            d = re.match(r,i)
            if d != None:
                s=d.groupdict()
                print(s)
                if s['host'] not in self.my_dict:
                    self.my_dict[s['host']] = [s['length']]
                else:
                    self.my_dict[s['host']].append(s['length'])
        print(self.my_dict)

                    


        
    
        


if __name__ == '__main__':
    myfile = MyFile('/home/ljs/learning/access_log')
    myfile.match_data()
