from flask import Flask, render_template, request
from testemergency import run_emergency_script

app = Flask(__name__)  # ✅ Keep this one (only once!)

@app.route('/', methods=['GET', 'POST'])
def index():
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
        return "✅ Script has been triggered. Check the automated Chrome window."

    return render_template('form.html')
