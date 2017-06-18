from flask import Flask, render_template
from models import *

app = create_app()
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
db.create_all(app=app)


@app.route("/")
def index():
	return render_template('index.html')


@app.route("/customer")
def customer():
	return render_template('customer.html')


@app.route("/admin")
def admin():
	# report of hits on distinct products
	logs = Log.query.filter_by()
	return render_template("admin.html")


@app.route("/support")
def support():
	return render_template("support.html")


@app.route("/webhook/update_accounts/<account_number>")
def update_accounts(account_number):
	""" Update the list of accounts for given account number
	"""
	return "OK"


@app.route("/webhook/mini_statement/<account_number>")
def fetch_mini_statement(account_number):
	""" Update available transactions in database
	"""
	return 'OK'



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
	app.run(debug=True)
