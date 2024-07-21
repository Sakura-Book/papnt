import os
from flask import Flask
from papnt.cli import doi

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print('*** $ papnt doi')
    doi()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
