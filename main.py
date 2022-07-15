from flask import Flask
app = Flask(__name__)

app_color='Blue'

@app.route('/')
def hello:
	return 'Hello World! This is Sumit'
#comment
#This is comment 
My second day or github training
