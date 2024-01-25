# pip install flask
from flask import Flask, render_template, request, redirect, session
# render_template load html files

from db import Database
from api import API
dbo = Database()
api = None
app = Flask(__name__)
app.secret_key = 'mysecretkey123'

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
@app.route('/') # url create and when you hit / this index function load
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=["post"]) # always mention which method data is coming
def perform_registration():
    name=request.form.get('user_ka_name')
    email=request.form.get('user_ka_email')
    password=request.form.get('user_ka_password')
    if email.endswith() == '@gmail.com' and len(password) >=6:
        response=dbo.insert(name, email, password)
        if response == 1:
            return render_template('login.html',message = "Registration successful, kindly login to proceed!")
        else:
            return render_template('register.html',message = "Email already exists")
    else:
        return render_template('register.html',message = "Please provide a valid email address")

    


@app.route('/perform_login', methods = ['post'])
def perform_login():
    email=request.form.get('user_ka_email')
    password=request.form.get('user_ka_password')

    response=dbo.search(email,password)
    if response == 1:
        session['logged_in'] = True  # Initialize the 'logged_in' key to True
        return render_template('check_api.html')
    else:
        return render_template('login.html', message = "Login failed, kindly login again")

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
@app.route("/perform_api",methods = ['post'])
def API_check():
    global api
    if session['logged_in']:
        text=request.form.get('user_ka_api')
        try:
            api = API(text)
            return render_template('profile.html', message="API verified successfully")
        except ValueError:
            return render_template('check_api.html', message="API unverified, kindly verify your API")
    else:
        return redirect('/')

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------    
@app.route("/profile")
def profile():
    if session['logged_in']:
        return render_template('profile.html')
    else:
        return redirect('/')

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
@app.route("/ner")
def ner():
    if session['logged_in']:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route("/perform_ner", methods=['post'])
def perform_ner():
    if session['logged_in']:
        text = request.form.get('ner_text')
        response = api.ner_analysis(text)
        return render_template('ner.html', response = response)
    else:
        return redirect ('/')

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
@app.route("/SA")
def SA():
    if session['logged_in']:
        return render_template('SA.html')
    else:
        return redirect('/')

@app.route("/perform_sa", methods=['post'])
def perform_sa():
    if session['logged_in']:
        text = request.form.get('sa_text')
        response = api.sentiment_analysis(text)
        return render_template('SA.html', response = response)
    else:
        return redirect ('/')

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

@app.route("/ER")
def ER():
    """
    A function that handles the "/ER" route.
    Returns:
        If the user is logged in, it renders the "ER.html" template.
        If the user is not logged in, it redirects to the home page.
    """

    if session['logged_in']:
        return render_template('ER.html')
    else:
        return redirect('/')

# app.py
@app.route("/perform_er", methods=['post'])
def perform_er():
    if session.get('logged_in'):
        text = request.form.get('er_text')
        
        # Check if the 'api' object is None
        if api is None:
            return render_template('ER.html', error_message='API object is not initialized')

        try:
            # Pass the text as a list to the emp_analysis method
            response = api.emp_analysis([text])
            return render_template('ER.html', response=response)
        except ValueError as e:
            return render_template('ER.html', error_message=str(e))
    else:
        return redirect('/')
    
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

@app.route("/Sarcasm")
def sarca():
    if session['logged_in']:
        return render_template('Sarcasm.html')
    else:
        return redirect('/')

# app.py
@app.route("/perform_sarcasm", methods=['post'])
def perform_sarca():
    if session.get('logged_in'):
        text = request.form.get('Sarcasm_text')
        
        # Check if the 'api' object is None
        if api is None:
            return render_template('Sarcasm.html', error_message='API object is not initialized')

        try:
            # Pass the text as a list to the emp_analysis method
            response = api.sarcasm_analysis([text])
            return render_template('Sarcasm.html', response=response)
        except ValueError as e:
            return render_template('Sarcasm.html', error_message=str(e))
    else:
        return redirect('/')

# --------------------------------------------------------------------------------------------------------
@app.route("/Abusive")
def abu():
    if session['logged_in']:
        return render_template('Abuse.html')
    else:
        return redirect('/')
@app.route("/perform_abusive", methods=['post'])
def perform_abus():
    if session.get('logged_in'):
        text = request.form.get("Abuse_text")
        
        # Check if the 'api' object is None
        if api is None:
            return render_template('Abuse.html', error_message='API object is not initialized')

        try:
            # Pass the text as a list to the emp_analysis method
            response = api.abuse_analysis([text])
            return render_template('Abuse.html', response=response)
        except ValueError as e:
            return render_template('Abuse.html', error_message=str(e))
    else:
        return redirect('/')

    

app.run(debug=True) # when you write debug = True you don't need to run code again and again