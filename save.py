name = 'details.log'

def save(data):
    file = open(name, 'w+')
    file.write(data)
    file.close()