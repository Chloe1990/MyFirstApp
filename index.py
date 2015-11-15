from flask import Flask
from flask import render_template
import os
import json
import time


app = Flask(__name__)

def get_data():
    tw = 'ToolsWorkflow_2UA3120YKCAW.08.Jun.15.15.16.23.results.txt'
    response = open(tw).read().splitlines(0)
    begin = response.count('BEGIN')
    end = response.count('END')
    batch = response.count('[MyToolButton] BATCH')
    dico = {'nbbegin': begin, 'nbend': end, 'nbbatch': batch}
    response2 = json.dumps(dico)
    return response2

@app.route("/")
def index():
    data = json.loads(get_data())
    batch = data.get('nbbatch')
    end = data.get('nbend')
    begin = data.get('nbbegin')
    return render_template("index.html", batch=batch, end=end, begin=begin)
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)