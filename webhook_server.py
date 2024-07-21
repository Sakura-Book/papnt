import os
from flask import Flask, jsonify

from pathlib import Path
import click

from papnt.cli import _config_is_ok
from papnt.misc import load_config
from papnt.database import Database, DatabaseInfo
from papnt.mainfunc import (
    add_records_from_local_pdfpath,
    update_unchecked_records_from_doi,
    update_unchecked_records_from_uploadedpdf,
    make_bibfile_from_records, make_abbrjson_from_bibpath)

global config, database
config = load_config('./papnt/config.ini')
database = Database(DatabaseInfo())

app = Flask(__name__)

#@app.route('/webhook', methods=['POST'])
#def webhook():
#    print('*** $ papnt doi') 
#   doi(app.app_context())

@app.route('/webhook', methods=['POST'])
def doi():
    """Fill information in record(s) by DOI"""
    if _config_is_ok():
        update_unchecked_records_from_doi(database, config['propnames'])
        with app.app_context():
            return jsonify({'status': 'success'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
