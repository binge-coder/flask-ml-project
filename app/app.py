# terminal -> python app.y
# browser  -> 127.0.0.1:5000/form


import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))



from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method=='GET':
        return render_template('form.html')
    else:
        Rating = float(request.form['Rating'])
        Age = float(request.form['Age'])
        Python = float(request.form['Python'])
        spark = float(request.form['spark'])
        aws = float(request.form['aws'])
        excel = float(request.form['excel'])
        sql = float(request.form['sql'])
        scikit = float(request.form['scikit'])
        tensor = float(request.form['tensor'])
        tableau = float(request.form['tableau'])

        features = np.array([[Rating, Age, Python, spark, aws, excel, sql, scikit, tensor, tableau]])
        salary = model.predict(features)

        return render_template('form.html', result=salary)


if __name__ == '__main__':
    app.run(debug=True)
