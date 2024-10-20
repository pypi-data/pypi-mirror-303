'''
 script to create
 - conecepts.py
 - __init__.py
 
 Bjoern Annighoefer 2023
'''

import os
import shutil

if __name__ == "__main__":
    FIRST_IMPORT = False
    BUP_FILE = "gen/pyecoremdb.init.py"
    OLD_FILE = "gen/pyecoremdb.prev.py"
    OLD_JSON = "gen/pyecoremdb.prev.json"
    GEN_TEMP = "gen/pyecoremdb.py.mako"
    GEN_FILE = "pyecoremdb.py"
    
    if(FIRST_IMPORT):
        os.system("python -m eoq3conceptsgen.pythontojsoncli -i %s -o %s"%(BUP_FILE,OLD_JSON))    
        os.system("python -m eoq3conceptsgen.generatefromconceptscli -i %s -o %s -d %s"%(GEN_TEMP,GEN_FILE,OLD_JSON))
    #replace old prev version with current one
    else:
        if(os.path.exists(OLD_FILE) and os.path.exists(GEN_FILE)):
            os.remove(OLD_FILE)
        shutil.copy(GEN_FILE, OLD_FILE)
        #convert old python file to json to use it in the template generator. This is not necessary every time
        os.system("python -m eoq3conceptsgen.pythontojsoncli -i %s -o %s"%(OLD_FILE,OLD_JSON))
        #fill pyecore mdb template
        os.system("python -m eoq3conceptsgen.generatefromconceptscli -i %s -o %s -d %s"%(GEN_TEMP,GEN_FILE,OLD_JSON))
  