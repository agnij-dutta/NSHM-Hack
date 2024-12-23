from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import init_db, add_user, get_user_by_username  # Import from models.py
from flask import session

main = Blueprint('main', __name__)

# Initialize the database
init_db()

def get_subscribed_pods(userid):
    # Replace with your logic to get the actual list of names
    return ["Subscribed POD 1a", "Subscribed POD 2b", "Subscribed POD 3c"]

def get_my_pods(userid):
    return ["Subscribed MyPOD 1a", "Subscribed MyPOD 2b", "Subscribed MyPOD 3c"]


@main.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            user = get_user_by_username(username)

            if user and user["password"] == password:
                # Save the user session
                session["user_id"] = user["id"]
                session["username"] = user["username"]

                # Redirect to the dashboard
                flash("Login successful!", "success")
                return redirect(url_for('main.dashboard'))
            else:
                flash("Invalid username or password.", "error")
        else:
            flash("Both username and password are required.", "error")

        return redirect(url_for("main.index"))
    return render_template('login.html')

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        print(f"Received data: username={username}, email={email}, password={password}")

        if username and email and password:
            print("Trying to register...")
            if get_user_by_username(username):
                flash("Username already exists. Please choose a different one.", "error")
            else:
                try:
                    add_user(username, email, password)
                    flash("Registration successful! Please log in.", "success")
                    return redirect(url_for("main.index"))
                except Exception as e:
                    flash(f"An error occurred: {e}", "error")
        else:
            flash("All fields are required.", "error")

    return render_template("register.html")

@main.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    userid = session['user_id']
    subscribed_pods = get_subscribed_pods(userid) # placeholder for getting subscribed pods of user with id
    my_pods = get_my_pods(userid)
    return render_template("dashboard.html", subscribed_pods=subscribed_pods, my_pods=my_pods)

@main.route("/createpod", methods=['GET', 'POST'])
def createpod():
    if request.method == "GET":
        return render_template("createpod.html")
    if request.method == "POST":
        pass # handle input of video link and personal file upload