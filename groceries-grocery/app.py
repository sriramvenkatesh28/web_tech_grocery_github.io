from flask import Flask, url_for, session, request, redirect, render_template, flash

flag = 0

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/", methods=["POST", "GET"])
def login():
	global flag
	if request.method == "POST":
	 	user = request.form["nm"]
	 	password = request.form["pwd"]

	 	if user == "admin" and password == "root":
	 		
	 		flag = 1
	 		flash("Welcome to Central Jail!")
	 		return render_template("index.html")
	 	else:
	 		flash("Wrong credentials!")
	 		return render_template("login.html")
	else:
	 	return render_template("login.html")


@app.route("/products.html", methods=["POST", "GET"])
def products():
	return render_template("products.html")

if __name__ == "__main__":
    app.run(debug=True)
