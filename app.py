from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder="templates")

with open('emp_turnover.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home(): 
    return render_template('pro_index.html', **locals())

@app.route("/predict",methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        satisfaction_level = float(request.form['satisfaction_level'])
        last_evaluation = float(request.form['last_evaluation'])
        number_project = float(request.form['number_project'])
        average_montly_hours = float(request.form['average_montly_hours'])
        time_spend_company = float(request.form['time_spend_company'])
        prediction = model.predict([[satisfaction_level,last_evaluation,number_project,average_montly_hours,time_spend_company]])
        
        result = prediction[0]
        if result == 1:
            return render_template("left.html")
        else:
            return render_template("stay.html")
    return render_template('pro_index.html', **locals())
                     
if __name__=='__main__':
	app.run(debug=True)