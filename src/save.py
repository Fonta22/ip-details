folder = 'saves'
name = 'details.log'

def save(data):
    file = open(f'{folder}/{name}', 'w+')
    file.write(data)
    file.close()