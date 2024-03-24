from flask import Flask, request, render_template
import pickle
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def events():
    return render_template('About.html')

@app.route('/prediction')
def predict_diabetes():
    return render_template('prediction.html')

@app.route('/predict',methods=['POST'])

def predict():
    glucose=int(request.form.get('glucose'))
    bloodpressure=int(request.form.get('bloodpressure'))

    output = model.predict([[glucose,bloodpressure]])

    if output==0:
        res="Not Diabetic"
    else:
        res="Diabetic"
    
    return render_template('/prediction.html', prediction_text=res)
    #return redirect(url_for('/prediction.html', prediction=res))



if __name__ == "__main__":
    app.run( debug=True)
