def parsePhoneNumbers(phonePath):
    phoneDict = {}
    with open(phonePath, 'r') as f:
        content = f.read()
    
    for line in content.split('\n'):
        phoneDict[line] = None

    return phoneDict