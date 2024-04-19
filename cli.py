import requests
import sys

def handleCliFns(func):
  if func == "list":
    resp = requests.get("http://localhost:5000/urls").json()
    for k,v in resp.items():
      print(k,v)
  if func == "create":
    if len(sys.argv)>2:
      resp = requests.post("http://localhost:5000/urls", headers={"Content-Type": "application/json"},json={"data": sys.argv[2]})
      print(resp.text,resp.status_code)
    else:
      print("Error: No url sent to shorten")
  if func == "lookup":
    if len(sys.argv)>2:
      resp = requests.get("http://localhost:5000/url/"+sys.argv[2], headers={"type": "cli"})
      if "Error:" in resp.text:
        print(resp.text,400)
      else:
        print(resp.text, resp.status_code)
    else:
      print("Error: No key provided to lookup url")
  if func == "delete":
    if len(sys.argv)>2:
      resp = requests.delete("http://localhost:5000/url/"+sys.argv[2], headers={"Content-Type": "application/json"})
      print(resp.status_code)
    else:
      print("Error: No url provided to delete")

handleCliFns(sys.argv[1])
