from flask import Flask, render_template, request, url_for
from flask_wtf import CSRFProtect as CSRF
from flask_wtf.csrf import CSRFError
from secrets import token_urlsafe as key
import backend
app = Flask(__name__)
app.secret_key = key(32)
app.config['SECRET_KEY'] = app.secret_key
csrf = CSRF(app)
DOMAIN = 'http://127.0.0.1:5000'


@app.route('/', methods=['GET', 'POST'])
def main():
    
    errors = []  # error messages
    
    # Form submitted
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
                if not (5 <= round(float(_range), 0) <= 25):
                    errors.append('Range must be between 1 and 25 km!')
                if not (22.15 <= float(_lat) <= 22.58):
                    errors.append('Latitude must be in Hong Kong (22.15-22.58)!')
                if not (113.83 <= float(_long) <= 114.41):
                    errors.append('Longitude must be in Hong Kong (113.83-114.41)!')
            except ValueError:
                errors.append('All fields must only contain numbers and decimal points!')
            
        
        if len(errors) == 0:
            _budget = float(_budget)
            _range = float(_range)
            _lat = float(_lat)
            _long = float(_long)
            ai = backend.recommend(_budget, _range, _lat, _long)
            return render_template('choose.html',
                budget = round(_budget),
                range = round(_range, 1),
                lat = round(_lat, 4),
                long = round(_long, 4),
                ai = ai)
    
    # Chosen restaurant
    r_id = request.args.get('r')
    if r_id:
        try:
            confirmation = backend.chosen(int(r_id))  # Send result to backend
            errors.append(confirmation)
        except ValueError:
            redirect('/')
    
    # Render index.html if form not submitted (successfully)
    return render_template('index.html', errors=errors, num_errors=len(errors))

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


if __name__ == "__main__":
    app.run()
