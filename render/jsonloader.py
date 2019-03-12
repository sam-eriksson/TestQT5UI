import json

class JsonLoader():
    def __init__(self, directory):
        #print("__init__")
        self.directory = directory
    
    def load(self, filename):
        print ("load")
        
        with open(self.directory+ filename, 'r') as myfile:
            st= myfile.read()
        a = json.loads(st)
        return a