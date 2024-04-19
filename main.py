from flask import Flask, request, jsonify, redirect
import hashlib, base64
# instance of flask application
app = Flask(__name__)

allUrls = dict()

def shortenUrl(url):
	hasher = hashlib.sha256(str(url).encode('utf-8'))
	return base64.urlsafe_b64encode(hasher.digest()[:10]).decode('utf-8')

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
	return "<p>URL SHORTNER</p>"

@app.route("/urls", methods=["GET", "POST"])
def handleUrlReqs():
	if request.method == "GET":
		return jsonify(allUrls)
	if request.method =="POST":
		orig_url = request.json
		if orig_url != None:
			allUrls[shortenUrl(orig_url["data"])] = orig_url["data"]
			return shortenUrl(orig_url["data"]), 201
		else:
			data = {"ERROR": "NO URLS SENT TO SHORTEN"}
			return jsonify(data), 201

@app.route("/url/<urlShortId>", methods=["GET"])
def getOrigUrl(urlShortId):
	print(request.headers)
	if "type" in request.headers:
		if urlShortId in allUrls.keys():
			return allUrls[urlShortId]
		else:
			return "Error: Short url not found on server"
	elif urlShortId in allUrls.keys():
		return redirect(allUrls[urlShortId], code=301)

@app.route("/url/<urlShortId>", methods=["DELETE"])
def delOrigUrl(urlShortId):
	del allUrls[urlShortId]
	return {},200

if __name__ == '__main__':
	app.run()
