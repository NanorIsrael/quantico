from flask import  Flask, render_template, request
from forms import RegistrationForm

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
	return render_template("home.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        errors = []

        # handle form submission here
        # print()
        username = request.form['uname']
        password = request.form['password']
        confirm = request.form['password2']
        if not username:
            errors.append("Username can't be blank!")
        if not password:
            errors.append("Password can't be blank!")
        if not confirm:
            errors.append("Password cannot be blank!")
        if len(username) < 3:
            errors.append("Username must be greater than 3 characters!")
        if password != confirm:
            errors.append("Passwords don't match!")

        if errors:
            message = "Registration failed! See errors below:"
        else:
            message = f"Successfully registered {username}."
        return render_template('register.html', message=message, errors=errors)

    return render_template('register.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""

    form = RegistrationForm()

    if request.method == "POST":
        if form.validate_on_submit():
            username = form.data["uname"]
            password = form.data["pword"]
            confirm = form.data["confirm"]
            message = f"Successfully registered {username}!"
        else:
            message = "Registration failed."

    return render_template("register.html", message=message, form=form)