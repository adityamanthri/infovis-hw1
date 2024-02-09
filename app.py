from flask import *
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, 
                          root='hw1/', 
                          prefix='hw1/', 
                          index_file='index.htm', 
                          autorefresh=True)

@app.route('/', methods=['GET'])
def hello():
    return make_response("add /hw1/ to the url")
    
if __name__ == "__main__":
    app.run(threaded=True, port=5000)