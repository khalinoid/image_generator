from flask import Flask,render_template,request
import requests


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")
@app.route("/result",methods = ['POST',"GET"])
def result():
	output = request.form.to_dict()
	name = output["name"]
	r = requests.post(
	    "https://api.deepai.org/api/text2img",
	    data={
	        'text': name,
	    },
	    headers={'api-key': '57469926-b75d-439b-a284-52d7ec4cf944'}
	)
	r_dict = r.json()
	output_image = r_dict['output_url']
	return render_template("index.html",name = output_image)

if __name__=='__main__':
	app.run(debug=True,port=5001) 