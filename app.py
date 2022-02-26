from unittest import result
from flask import Flask, render_template, redirect, url_for, request, current_app
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():

    data=[]
    data2=[]
    if request.method == 'POST':
        print("Post Call")
        if request.form.get('pred') == 'Predict':
            print("Prediction")
            model = pickle.load(current_app.open_resource('model.pkl'))
            print(model)
            pclass=request.form.get('pclass')
            sex=request.form.get('sex')
            age=request.form.get('age')
            sibsp=request.form.get('sibsp')
            parch=request.form.get('parch')
            fare=request.form.get('fare')
            data2=[[float(pclass),int(sex),float(age),float(sibsp),float(parch),float(fare)]]
            # data2.append(data)
            # data = [[float(lstat), float(rad), float(indus), float(nox), float(rm), float(tax), float(ptratio)]]
            print(data2)
            prediction= model.predict(data2)
            print(prediction[0])
            # pred="{:.2f}".format(prediction)
            print(prediction)
            # final_price=f"${str(pred)}"
            if(prediction[0]==1):
                final='Survived'
            else:
                final=' Sorry Not Survived'
            return render_template('predict.html', prediction=final)
        if request.form.get('back') == 'Back':
            print("Prediction")
            return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
