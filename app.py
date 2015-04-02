from flask import Flask, render_template

app = Flask(__name__)
CSRF_ENABLED = True
SECRET_KEY = 'caocaoshuodaocaocao'

@app.route('/', methods=['GET'])
def page():
	return render_template('index.html')

app.run(debug=False)
