from flask import Flask ,render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_beer():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    beerjson = r.json()
    dicti = {
        'name' : beerjson[0]['name'],
        'tag' : beerjson[0]['tagline'],
        'img' : beerjson[0]['image_url'],
        'per': beerjson[0]['abv'],
        'desc' : beerjson[0]['description']

    }
    return render_template('index.html',dic=dicti)

if __name__ == '__main__':
    app.run(debug=True)