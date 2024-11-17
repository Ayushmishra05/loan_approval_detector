from flask import Flask, render_template, request, jsonify, redirect, url_for
from src.pipeline.prediction_pipeline import PredictionPipeline
import numpy as np
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('front.html')

@app.route('/learn', methods=['POST'])
def learn_more():
    # Here, you can perform any logic when the form is submitted
    # For example, logging or processing the form data
    print("Learn More button clicked")

    # After handling the POST request, redirect to index.html
    return render_template('index.html')


@app.route('/submit' , methods = ['POST'])
def submit():
    # Collecting the form data
    form_data = request.form

    # Continuous values
    result_array = [
        float(form_data['person_age']),               # Age
        float(form_data['person_income']),            # Income
        float(form_data['person_emp_exp']),           # Employment Experience
        float(form_data['loan_amnt']),                # Loan Amount
        float(form_data['loan_int_rate']),            # Interest Rate
        float(form_data['loan_percent_income']),      # Loan as Percent of Income
        float(form_data['cb_person_cred_hist_length']),  # Credit History Length
        float(form_data['credit_score'])              # Credit Score
    ]

    # Gender: One-hot encode
    gender = form_data['gender']
    result_array.extend([
        1 if gender == 'male' else 0             # Female
    ])

    # One-hot encode Education Level
    education = form_data['education']
    result_array.extend([
        1 if education == 'Bachelor' else 0,         # Bachelor
        1 if education == 'Doctorate' else 0,        # Doctorate
        1 if education == 'High School' else 0,      # High School
        1 if education == 'Master' else 0            # Master
    ])

    # One-hot encode Home Ownership
    home_ownership = form_data['home_ownership']
    result_array.extend([
        1 if home_ownership == 'OTHER' else 0,       # Other
        1 if home_ownership == 'OWN' else 0,         # Own
        1 if home_ownership == 'RENT' else 0         # Rent
    ])

    # One-hot encode Loan Intent
    loan_intent = form_data['loan_intent']
    result_array.extend([
        1 if loan_intent == 'EDUCATION' else 0,          # Education
        1 if loan_intent == 'HOMEIMPROVEMENT' else 0,    # Home Improvement
        1 if loan_intent == 'MEDICAL' else 0,            # Medical
        1 if loan_intent == 'PERSONAL' else 0,           # Personal
        1 if loan_intent == 'VENTURE' else 0             # Venture
    ])

    # Checkbox for Previous Loan Defaults
    previous_loan_defaults = 1 if 'previous_loan_defaults' in form_data else 0
    result_array.append(previous_loan_defaults)          # Previous Loan Defaults

    # Return or process result_array as needed
    pipeline = PredictionPipeline()
    out = pipeline.predict(np.array([result_array]))
    return render_template('predict.html' , eligibility_value = out)


if __name__ == '__main__':
    app.run(debug=True)
