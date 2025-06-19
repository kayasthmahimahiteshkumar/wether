from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("register.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    success_message = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # You can store or print data here
        print(f"User registered: {name}, {email}")

        success_message = "Registration Successful!"

    return render_template("register.html", success=success_message)

if __name__ == "__main__":
    app.run(debug=True)