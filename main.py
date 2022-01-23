from flask import Flask, render_template, request, url_for, redirect, session
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_login import login_user, LoginManager, login_required, current_user, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


list_date = 0

app = Flask(__name__)
Bootstrap(app)


app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def mu_func(x):
    if x is None:
        return True
    else:
        return False


# CREATE Todo_list  IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    email = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(1000))
    todo_list = db.relationship("Todo", backref="user")


# CREATE Todo_list  IN DB
class Todo(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100), unique=True)
    day = db.Column(db.String(100))
    # yesterday
    yesterday_1 = db.Column(db.String(1000), default="empty")
    yesterday_2 = db.Column(db.String(1000), default="empty")
    yesterday_3 = db.Column(db.String(1000), default="empty")
    yesterday_4 = db.Column(db.String(1000), default="empty")
    yesterday_5 = db.Column(db.String(1000), default="empty")
    # today
    today_1 = db.Column(db.String(1000), default="empty")
    today_2 = db.Column(db.String(1000), default="empty")
    today_3 = db.Column(db.String(1000), default="empty")
    today_4 = db.Column(db.String(1000), default="empty")
    today_5 = db.Column(db.String(1000), default="empty")
    today_6 = db.Column(db.String(1000), default="empty")
    today_7 = db.Column(db.String(1000), default="empty")
    today_8 = db.Column(db.String(1000), default="empty")
    today_9 = db.Column(db.String(1000), default="empty")
    today_10 = db.Column(db.String(1000), default="empty")
    # top personal_1
    top_1 = db.Column(db.String(1000), default="empty")
    top_2 = db.Column(db.String(1000), default="empty")
    top_3 = db.Column(db.String(1000), default="empty")
    top_4 = db.Column(db.String(1000), default="empty")
    top_5 = db.Column(db.String(1000), default="empty")
    # personal
    personal_1 = db.Column(db.String(1000), default="empty")
    personal_2 = db.Column(db.String(1000), default="empty")
    personal_3 = db.Column(db.String(1000), default="empty")
    personal_4 = db.Column(db.String(1000), default="empty")
    personal_5 = db.Column(db.String(1000), default="empty")
    # notes
    notes_1 = db.Column(db.String(1000), default="empty")
    notes_2 = db.Column(db.String(1000), default="empty")
    notes_3 = db.Column(db.String(1000), default="empty")
    notes_4 = db.Column(db.String(1000), default="empty")
    notes_5 = db.Column(db.String(1000), default="empty")
    notes_6 = db.Column(db.String(1000), default="empty")
    notes_7 = db.Column(db.String(1000), default="empty")
    notes_8 = db.Column(db.String(1000), default="empty")
    # schedule
    schedule_1 = db.Column(db.String(1000), default="empty")
    schedule_2 = db.Column(db.String(1000), default="empty")
    schedule_3 = db.Column(db.String(1000), default="empty")
    schedule_4 = db.Column(db.String(1000), default="empty")
    schedule_5 = db.Column(db.String(1000), default="empty")
    schedule_6 = db.Column(db.String(1000), default="empty")
    schedule_7 = db.Column(db.String(1000), default="empty")
    schedule_8 = db.Column(db.String(1000), default="empty")
    schedule_9 = db.Column(db.String(1000), default="empty")
    schedule_10 = db.Column(db.String(1000), default="empty")
    schedule_11 = db.Column(db.String(1000), default="empty")
    schedule_12 = db.Column(db.String(1000), default="empty")
    schedule_13 = db.Column(db.String(1000), default="empty")
    schedule_14 = db.Column(db.String(1000), default="empty")
    schedule_15 = db.Column(db.String(1000), default="empty")
    schedule_16 = db.Column(db.String(1000), default="empty")
    schedule_17 = db.Column(db.String(1000), default="empty")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


# db.create_all()
# Login Manger
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/todo', methods=["POST", "GET"])
@login_required
def todo():
    if request.method == "GET":
        return render_template("list.html", items=list_date)
    elif request.method == "POST":
        # Yesterday
        list_date.yesterday_1 = request.form['before1']
        list_date.yesterday_2 = request.form['before2']
        list_date.yesterday_3 = request.form['before3']
        list_date.yesterday_4 = request.form['before4']
        list_date.yesterday_5 = request.form['before5']
        # Today
        list_date.today_1 = request.form['today1']
        list_date.today_2 = request.form['today2']
        list_date.today_3 = request.form['today3']
        list_date.today_4 = request.form['today4']
        list_date.today_5 = request.form['today5']
        list_date.today_6 = request.form['today6']
        list_date.today_7 = request.form['today7']
        list_date.today_8 = request.form['today8']
        list_date.today_9 = request.form['today9']
        list_date.today_10 = request.form['today10']
        # Top
        list_date.top_1 = request.form['top1']
        list_date.top_2 = request.form['top2']
        list_date.top_3 = request.form['top3']
        list_date.top_4 = request.form['top4']
        list_date.top_5 = request.form['top5']
        # Personal
        list_date.personal_1 = request.form['personal1']
        list_date.personal_2 = request.form['personal2']
        list_date.personal_3 = request.form['personal3']
        list_date.personal_4 = request.form['personal4']
        list_date.personal_5 = request.form['personal5']
        # Notes
        list_date.notes_1 = request.form['note1']
        list_date.notes_2 = request.form['note2']
        list_date.notes_3 = request.form['note3']
        list_date.notes_4 = request.form['note4']
        list_date.notes_5 = request.form['note5']
        list_date.notes_6 = request.form['note6']
        list_date.notes_7 = request.form['note7']
        list_date.notes_8 = request.form['note8']
        # Schedule
        list_date.schedule_1 = request.form['schedule1']
        list_date.schedule_2 = request.form['schedule2']
        list_date.schedule_3 = request.form['schedule3']
        list_date.schedule_4 = request.form['schedule4']
        list_date.schedule_5 = request.form['schedule5']
        list_date.schedule_6 = request.form['schedule6']
        list_date.schedule_7 = request.form['schedule7']
        list_date.schedule_8 = request.form['schedule8']
        list_date.schedule_9 = request.form['schedule9']
        list_date.schedule_10 = request.form['schedule10']
        list_date.schedule_11 = request.form['schedule11']
        list_date.schedule_12 = request.form['schedule12']
        list_date.schedule_13 = request.form['schedule13']
        list_date.schedule_14 = request.form['schedule14']
        list_date.schedule_15 = request.form['schedule15']
        list_date.schedule_16 = request.form['schedule16']
        list_date.schedule_17 = request.form['schedule17']
        db.session.commit()
        return redirect(url_for("todo"))


@app.route('/login', methods=["POST", "GET"])
def login():
    global list_date
    date = datetime.now().strftime("%Y/%m/%d")
    day = datetime.now().strftime("%A")
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if check_password_hash(user.password, password):
            login_user(user)

            # checking if it's a new list or to get old one to either create one or fetch from the database
            list_date = Todo.query.filter_by(date=date).first()
            if Todo.query.filter_by(date=date).first() is None:  # New
                new_todo_list = Todo(date=date, day=day, user_id=current_user.id, yesterday_1="First: ",
                                     yesterday_2="Second: ", yesterday_3="Third: ", yesterday_4="Forth: ",
                                     yesterday_5="Fifth: ", today_1="First: ", today_2="Second: ", today_3="Third: ",
                                     today_5="Fifth: ", today_6="Sixth: ", today_7="Seventh: ", today_8="Eighth: ",
                                     today_9="Ninth: ", today_10="Tenth: ", top_1="First: ", top_2="Second: ",
                                     top_3="Third: ", top_4="Fourth: ", top_5="Fifth: ", personal_1="First: ",
                                     personal_2="Second: ", personal_3="Third: ", personal_4="Fourth: ",
                                     personal_5="Fifth: ", notes_1="First: ", notes_2="Second: ", notes_3="Third: ",
                                     notes_4="Fourth: ", notes_5="Fifth: ", notes_6="Sixth: ", notes_7="Seventh: ",
                                     notes_8="Eighth: ", schedule_1="First: ", schedule_2="Second: ",
                                     schedule_3="Third: ", schedule_4="Fourth: ", schedule_5="Fifth: ",
                                     schedule_6="Sixth: ", schedule_7="Seventh: ", schedule_8="Eighth: ",
                                     schedule_9="Ninth: ", schedule_10="Tenth: ", schedule_11="Eleventh: ",
                                     schedule_12="Twelev: ", schedule_13="Thirteen: ", schedule_14="Fourteen: ",
                                     schedule_15="Fifteen: ", schedule_16="Sixteen: ", schedule_17="Seventeen: ")
                db.session.add(new_todo_list)
                db.session.commit()
                list_date = new_todo_list
            else:
                list_date = Todo.query.filter_by(date=date).first()
            return redirect(url_for("todo"))
        else:
            return redirect(url_for("login"))


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        first_name = request.form['f-name']
        last_name = request.form['l-name']
        password = request.form['password']
        email = request.form['email']
        new_todo = Todo()
        db.session.add(new_todo)
        encrypted_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=encrypted_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        session['username'] = request.form['f-name']
        return redirect(url_for("home"))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
