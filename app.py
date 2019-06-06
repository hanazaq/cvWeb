from flask import Flask ,render_template ,request
app = Flask(__name__)

@app.route("/")
def website():
	return render_template('03-cv-business.html')
@app.route("/read")
def about():
	return render_template('letter.html')
@app.route("/cer11")
def form():
	return render_template('certf11.html')
@app.route("/cer10")
def us():
	return render_template('certf10.html')


if __name__== "__main__":
	app.run(debug=True)