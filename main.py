from flask import Flask,render_template,request

import joblib

# load the model
model=joblib.load("model_file.pkl")

# initialize the app
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

"""@app.route('/about-us')
def about():
    return render_template('about.html')
"""
@app.route('/process',methods=['post'])
def form_data():
    preg=request.form.get("preg")
    plas=request.form.get("plas")
    pres=request.form.get("pres")
    skin = request.form.get("skin")
    test= request.form.get("test")
    mass = request.form.get("mass")
    pedi = request.form.get("pedi")
    age = request.form.get("age")

    output=model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])

    if output[0] == 1:
        data="Take care of yourself, You are diabetic"
    else:
        data="You are healthy & perfectly fine"

    return data

# run the application
app.run(host='0.0.0.0',port=7060)
