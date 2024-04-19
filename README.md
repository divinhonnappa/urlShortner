# urlShortner

## Description
Implements a simple Python app server that will encode and store "url safe" url short id along with a cli that can be used to query server and perform basic operations like list, create, lookup and delete.<br>

### Server implementation
The server also implements the following HTTP endpoint methods<br>

  - GET /urls : returns a list of all urls currently stored in server along with original url map.
  - POST /url : accepts url to be shortened in request body and returns the "url safe" encoded shorteded url.
  - GET /url/{shortUrlId}  : redirects to browser requests to original url if the short url id is present on server.
  - DELETE /url/{shortUrlId} : deletes the short url id and it's original url record from server

### Client implementation
The client is a cli tool that takes args from cli and queries server to call the http endpoints to perform similar operation

  - ./cli.py list : calls the GET urls method endpoint and prints the map of short url id and original urls
  - ./cli.py create {original url} : calls POST method endpoint to create and return the short url id
  - ./cli.py lookup {short url} : calls GET url method with the short url and returns the mapped original url
  - ./cli.py delete {short url} : calls DELETE url method and deletes the map of the short url and original url from server

### Running the app server
Run the main.py app with `python3 ./main.py` and use the cli or curl commands to interact with the app server
