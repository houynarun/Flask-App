from flask import Flask, render_template

app = Flask(__name__)

@app.route('/appView', methods=['GET','POST'])
def appView():

	return render_template('templ/index.html')
