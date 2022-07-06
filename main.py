from flask import Flask
app = Flask(__name__)

app_color='Blue'

@app.route('/')
def hello:
	return 'Hello World! Its our First Python Flask Applicaiton'

