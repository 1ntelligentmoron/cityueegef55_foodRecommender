from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
DOMAIN = 'http://127.0.0.1:5000/'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/choose')
def choose():
    if request.referrer in (DOMAIN, DOMAIN + 'more'):
        return render_template('choose.html')
    else:
        return redirect('/')
        # return f'{request.referrer} // {DOMAIN} // {DOMAIN}/more'

@app.route('/more')
def more():
    restaurant = request.args.get('r')
    return render_template('more.html')

@app.route('/go')
def go():
    restaurant = request.args.get('r')
    return render_template('go.html')
