from flask import Flask, request, redirect, render_template
import re
import cgi
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
app.config['DEBUG'] = True

def isValidEmail(email):
    try:
        v = validate_email(email) # validate and get info
        email = v["email"] # replace with normalized form
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))
        return False
    

#Check user sign up
@app.route("/register", methods=['POST'])
def register_validate():
    # look inside the request to figure out what the user typed
    #new_movie = request.form['new-movie']

    user=request.form['user']
    email=request.form['email']
    password=request.form['password']
    passwordConfirm=request.form['passwordConfirm']

    # if the user typed nothing at all, redirect and tell them the error
    if (not user) or (user.strip() == ""):
        error = "Please specify name."
        return redirect("/?error=" + errorn)

    if (len(user)<4) or (len(user)>20):
        error = "Valid name is more than 3 characters and less than 20."
        return redirect("/?error=" + errorn)

    
    if isValidEmail(email) == False :
        error = "Please specify valid email."
        return redirect("/?error=" + errore)
                    

    if (not email) or (email.strip() == ""):
        error = "Please specify email."
        return redirect("/?error=" + errore)

    if (not password) or (password.strip() == ""):
        error = "Please use a password."
        return redirect("/?error=" + errorp)

    if (not passwordConfirm) or (passwordConfirm.strip() == ""):
        error = "Please use a password."
        return redirect("/?error=" + errorp)

    if (passwordConfirm !=password):
        error = "Passwords don't match."
        return redirect("/?error=" + errorp)

    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    user_escaped = cgi.escape(user, quote=True)
    email_escaped = cgi.escape(email, quote=True)
    password_escaped = cgi.escape(password, quote=True)
    passwordConfirm_escaped = cgi.escape(passwordConfirm, quote=True)

    # TODO:
    # Create a template called add-confirmation.html inside your /templates directory
    # Use that template to render the confirmation message instead of this temporary message below
    encoded_error = request.args.get("error")
    return render_template('homepage.html', username=user_escaped, error=encoded_error and cgi.escape(encoded_error, quote=True))

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('welcome.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()