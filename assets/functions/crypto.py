import uuid

def getRandomString(string_length):
    string = str(uuid.uuid4()).replace("-","")
    return string[0:string_length]