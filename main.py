from flask import Flask, render_template, request
from testemergency import run_emergency_script

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            gender = request.form['gender']
            forename = request.form['forename']
            surname = request.form['surname']
            dob_day = request.form['dob_day']
            dob_month = request.form['dob_month']
            dob_year = request.form['dob_year']
            home_postcode = request.form['home_postcode']

            run_emergency_script(
                gender, forename, surname,
                dob_day, dob_month, dob_year,
                home_postcode,
                progress_callback=None
            )

            return render_template('success.html')


        print("✅ Rendering form.html...")
        return render_template('form.html')
  import traceback  # Make sure this is at the top of your file

# Inside your route:
import traceback

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            print("✅ Received POST request...")

            gender = request.form['gender']
            forename = request.form['forename']
            surname = request.form['surname']
            dob_day = request.form['dob_day']
            dob_month = request.form['dob_month']
            dob_year = request.form['dob_year']
            home_postcode = request.form['home_postcode']

            print(f"👤 Patient: {forename} {surname}, {dob_day}/{dob_month}/{dob_year}, {gender}, {home_postcode}")

            run_emergency_script(
                gender, forename, surname,
                dob_day, dob_month, dob_year,
                home_postcode,
                progress_callback=None
            )

            print("✅ Script triggered successfully.")
            return render_template('success.html')

        print("✅ Rendering form.html...")
        return render_template('form.html')
    except Exception as e:
        print("❌ EXCEPTION OCCURRED:")
        traceback.print_exc()
        return f"An error occurred: {str(e)}"
