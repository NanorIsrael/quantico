from flask import  Flask, render_template, request
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy

# csrf = CSRFProtect()

app = Flask(__name__)
app.config['SECRET_KEY']='gs9df3nkj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
with app.app_context():

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), index=True, unique=True)
        password = db.Column(db.String(128))

        def __repr__(self):
             return f'User {self.username}'

    class ShippingInfo(db.Model):
        ship_id = db.Column(db.Integer, primary_key=True)
        full_name = db.Column(db.String(50))
        address = db.Column(db.String(50))
        user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

        def __repr__(self):
            return f"{self.full_name}'s address is {self.address}."

    db.create_all()
    ship1 = ShippingInfo(full_name="Claudia Reyes", address="Amsterdam 210, CDMX, Mexico", user_id=2)
    ship2 = ShippingInfo(full_name="Roy Latte", address="Beau St, Bath BA1 1QY, UK", user_id=1)
    db.session.add(ship1)
    db.session.add(ship2)
    db.session.commit()
    
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
            user_match = User.query.filter_by(username=username).first()
            if user_match:
                message = f"User {username} already exist!"
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            message = f"Successfully registered {username}!"
        else:
            message = "Registration failed."

    return render_template("register.html", message=message, form=form)

import json
@app.route("/user/<string:username>", methods=["GET"])
def get_user(username):
    print('request.params', username)
    user_match = User.query.filter_by(username=username).first()
    return json.dumps({"user_id": user_match.id})

@app.route("/admin", methods=["GET"])
def admin():
    users = User.query.all()
    shippers = ShippingInfo.query.all()
    return render_template("admin.html", users=users, shippers=shippers)
# user1 = User(username = "coffeeaddict", password = "1234")
# db.session.add(user1)
# db.session.commit()


# csrf.exempt(register)
if __name__ == '__main__':
    app.run(debug=True)