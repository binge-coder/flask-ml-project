import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("form.html")

@app.route('/form', methods=['GET', 'POST'])
def form():
    result = ""  # Initialize result as an empty string

    if request.method == 'POST':
        Rating = float(request.form['Rating'])
        Age = float(request.form['Age'])
        # Convert checkbox values to 1 if checked, 0 otherwise
        Python = 1 if 'Python' in request.form else 0
        spark = 1 if 'spark' in request.form else 0
        aws = 1 if 'aws' in request.form else 0
        excel = 1 if 'excel' in request.form else 0
        sql = 1 if 'sql' in request.form else 0
        scikit = 1 if 'scikit' in request.form else 0
        tensor = 1 if 'tensor' in request.form else 0
        tableau = 1 if 'tableau' in request.form else 0

        features = np.array([[Rating, Age, Python, spark, aws, excel, sql, scikit, tensor, tableau]])
        salary = model.predict(features)[0]
        formatted_salary = "{:.2f}".format(salary)
        return render_template('form.html', result=formatted_salary)

    # For GET request, return the form template with initial result as ""
    return render_template('form.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
