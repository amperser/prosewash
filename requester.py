import requests
import time
contents = {
    "text": "Quick brown fox jumped over the lazy dog."
}
base_url = "http://0.0.0.0:5000/document"

response = requests.post(base_url, data=contents)
# response = requests.post("http://prosewash.herokuapp.com/document", data=contents)
# print(response.content)
time.sleep(.5)
second_url = base_url+"/"+response.content.decode('utf-8')
print(second_url)
response2 = requests.get(second_url)
print(response2.content)
