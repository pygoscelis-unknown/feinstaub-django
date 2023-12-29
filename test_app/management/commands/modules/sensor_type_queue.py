from .csv import get_header

def register(dictionary, key, url):
    print("sensor type not in queue: register sensor type", key)
    dictionary[key] = get_header(url)

def skip(key):
    print("sensor type", key, "already in queue: skip...")
