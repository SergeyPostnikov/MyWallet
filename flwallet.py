from flask import Flask, render_template
from my_wallet.storage import initialize
app = Flask(__name__)


 

if __name__ == '__main__':
	# app.run(debug=True)
	initialize(creation_schema='creation_shcema.sql')