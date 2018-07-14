from flask import Flask, render_template, session, redirect, request, url_for, flash
from validate_email import validate_email

app = Flask(__name__)
app.secret_key = "YouMakeMeVomit"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    errors = False

    # form validation
    if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2:
        flash('Names must be at least 2 characters long', 'danger')
        errors = True

    if len(request.form['email']) < 1:
        flash('Please enter your email address', 'danger')
    
    # validate e-mail
    is_valid = validate_email(request.form['email'])
    if is_valid == False:
        flash('Please enter a valid email address', 'danger')
        errors = True

    # password checks
    password = request.form['password']
    if len(password) < 8:
        flash('Password should be at least 8 digits long', 'danger')
        errors = True
    if password.isalpha() or password.isdigit():
        flash('Password should contain at least one number [0-9] and at least one alpha character [a-z]', 'danger')
        errors = True
    if password.islower():
        flash('Password should contain at least one capitalized alpha character', 'danger')
        errors = True
    if password != request.form['password_confirm']:
        flash('Passwords do not match', 'danger')
        errors = True

    # if validation failed
    if errors == True:
        return redirect('/')

    # if validation passed
    flash('You are reigstered!', 'success')
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

    
app.run(debug=True)