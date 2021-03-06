from time import gmtime, strftime

def checkFloats(field):
    try:
        return float(field)
    except:
        return None

def checkInt(field):
    try:
        return int(field)
    except:
        return None

def getNow():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())
