import requests

contents = {
    "text": "Quick brown fox jumped over the lazy dog."
}
requests.post("http://0.0.0.0:5000/document", data=contents)
