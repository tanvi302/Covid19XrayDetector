from flask import Flask, render_template,redirect,request
import Predict_xray


#__name__=__main__
app=Flask(__name__)
@app.route('/')
def hello():
	return render_template("index.html")


@app.route('/',methods=['POST'])
def detect():
	if request.method == 'POST':
		name=request.form['username']
		f=request.files['userfile']
		path="./static/{}".format(f.filename) #./static/image.jpg
		f.save(path)
		res=Predict_xray.xray(path)
		result_dic={
		'image' : path,
		'res' : res
		}
		
	return render_template("index.html",your_result=result_dic,name=name)

if __name__=='__main__':
	#app.debug=True
	app.run(debug=True)