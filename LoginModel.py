
data = {}
def saveToFile(data) :
    userFile = open("User.txt", "a")
    # Loop through the dictionary and return the key->value
    # txt = ', '.join("{!s}={!r}".format(key,val) for key,val in data.items())
    '''
    One liner convert dictionary to string
    can be write in multiple lines to
    '''
    txt = ', '.join("{!s}".format(val) for val in data.values())
    userFile.write(txt + '\n')
    userFile.close()
    return True

def save(data) :
    if not saveToFile(data) :
        return False
    return True

def readFile() :
    f = open('User.txt', 'r')
    info = f.read().split('\n')
    f.close()
    return info