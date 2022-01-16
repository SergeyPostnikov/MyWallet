from flask import Flask, render_template

app = Flask(__name__)

menu = ['About', 'Signin', 'Log in']

@app.route('/')
def index():
	return render_template('base.html', title='MyWallet')

@app.route('/login')
def login():
	return '<form><textarea>Login</textarea><button>Log in</button></form>'

@app.route('/signin')
def signin():
	return '<form><textarea>Login</textarea><button>Sign in</button></form>'
 

if __name__ == '__main__':
	app.run(debug=True)