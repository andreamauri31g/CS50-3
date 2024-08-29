from flask import session, Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# set the secret key to some random bytes. Keep this really secret!
app.secret_key = "pp11ss"

P = ["ciao1234", "ciao4321"]

@app.route("/")
def index():
    if "password" in session:
        return render_template("index.html", password=session["password"])
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST" and request.form["password"] in P:
        session["password"] = request.form["password"]
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop("password", None)
    return redirect(url_for("index"))