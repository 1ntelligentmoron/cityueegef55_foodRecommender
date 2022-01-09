from flask import Flask, render_template, request, url_for, redirect
from markupsafe import escape
from flask_wtf import CSRFProtect as CSRF
from secrets import token_urlsafe as key
import backend
app = Flask(__name__)
app.secret_key = key(32)
app.config['SECRET_KEY'] = app.secret_key
csrf = CSRF(app)
DOMAIN = 'http://127.0.0.1:5000'


@app.route('/', methods=['GET', 'POST'])
def main():
    errors = []
    
    if request.method == 'POST':
        
        _budget = request.form.get('budget')
        _range = request.form.get('range')
        _lat = request.form.get('lat')
        _long = request.form.get('long')
        
        if not (_budget and _range and _lat and _long):
            errors.append('All fields must not be empty!')
        else:
            try:
                if round(float(_budget), 0) < 20:
                    errors.append('Budget must be at least HKD20!')
                if not (1 <= round(float(_range), 0) <= 25):
                    errors.append('Range must be between 1 and 25 km!')
                if not (22.15 <= float(_lat) <= 22.58):
                    errors.append('Latitude must be in Hong Kong (22.15-22.58)!')
                if not (113.83 <= float(_long) <= 114.41):
                    errors.append('Longitude must be in Hong Kong (113.83-114.41)!')
            except ValueError:
                errors.append('All fields must only contain numbers and decimal points!')
            
        
        if len(errors) == 0:
            return render_template('choose.html',
                budget = escape(_budget),
                range = escape(_range),
                lat = escape(_lat),
                long = escape(_long),
                ai = backend.recommend(_budget, _range, _lat, _long))
        
    return render_template('index.html', errors=errors, num_errors=len(errors))


if __name__ == "__main__":
    app.run(debug=True)
    