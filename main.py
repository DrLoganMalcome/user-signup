from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

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
        return redirect("/?error=" + error)

    if (not email) or (email.strip() == ""):
        error = "Please specify email."
        return redirect("/?error=" + error)

    if (not password) or (password.strip() == ""):
        error = "Please use a password."
        return redirect("/?error=" + error)

    if (not passwordConfirm) or (passwordConfirm.strip() == ""):
        error = "Please use a password."
        return redirect("/?error=" + error)

    if (passwordConfirm !=password):
        error = "Passwords don't match."
        return redirect("/?error=" + error)

    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    user_escaped = cgi.escape(user, quote=True)
    email_escaped = cgi.escape(email, quote=True)
    password_escaped = cgi.escape(password, quote=True)
    passwordConfirm_escaped = cgi.escape(passwordConfirm, quote=True)

    # TODO:
    # Create a template called add-confirmation.html inside your /templates directory
    # Use that template to render the confirmation message instead of this temporary message below
    encoded_error = request.args.get("error")
    return render_template('homepage.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('welcome.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()