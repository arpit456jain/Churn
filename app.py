# from keras.models import load_model
from flask import Flask,render_template,request,redirect

app = Flask("diabetic_app")
# m = load_model('churn.h5')

@app.route("/")
def slash():
        return ("Hello")
params = {}
@app.route("/home",methods=['POST', 'GET'])
def Home():
    if request.method == "POST":
        print('post')
        global params
        params['FULL_NAME'] = request.form["FULL_NAME"]
        params['MOBILE_NUMBER'] = request.form["MOBILE_NUMBER"]
        params['EMAIL_ADDRESS'] = request.form["EMAIL_ADDRESS"]
        print(params)
        return redirect('/form')
    else:
        print('get')
    return render_template("home.html")

@app.route("/form",methods=['POST', 'GET'])
def Form():
    if request.method == "POST":
        global params
        print('post',params)
        params['Credit_score'] = request.form['Credit_score']
        params['Age'] = request.form['Age']
        params['tenure'] = request.form['tenure']
        params['Balance'] = request.form['Balance']
        params['NumofProducts'] = request.form['NumofProducts']
        params['Estimated_salary'] = request.form['Estimated_salary']
        params['Is_Active_member'] = request.form['Is_Active_member']
        params['Gender'] = request.form['Gender'] 
        params['Country'] = request.form['Country']
        params['Has_Credit_Card'] = request.form['Has_Credit_Card']
        print(params)
        params['output'] =  'Job excited'
        print("data saved success now make a report of it")
        
        return render_template('report.html',params=params)
    else:
        print('get')
    return render_template("form.html")

@app.route("/output" , methods=[ "GET" ])
def dia():
    x1 = request.args.get("y1")
    x2 = request.args.get("y2")
    x3 = request.args.get("y3")
    x4 = request.args.get("y4")
    x5 = request.args.get("y5")
    x6 = request.args.get("y6")
    x7 = request.args.get("y7")
    x8 = request.args.get("y8")
    x9 = request.args.get("y9")
    x10 = request.args.get("y10")
    x11 = request.args.get("y11")
    output = m.predict([[ int(x1) , int(x2) , int(x3) , float(x4) , int(x5) , float(x6) ,int(x7) , int(x8),int(x9),int(x10),int(x11) ]])
    if output == '1':
        return ("Job excited")
    else:
        return ("Job not excited")

app.run(debug=True)