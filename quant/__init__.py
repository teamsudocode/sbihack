#!/usr/bin/python3

from flask import Flask, render_template, jsonify, request
from quant.models import *

app = create_app()
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
db.create_all(app=app)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/customer")
def customer():
    return render_template('customer.html')

@app.route("/product/<id>")
def product_info(id):
    product = Product.query.filter_by(id=id).first()
    reviews = Review.query.filter_by(productid=id).all()
    me = User.query.filter_by(id=1).first()
    print(product)
    print(reviews)
    return render_template('product.html',
                           product=product,
                           reviews=reviews,
                           me=me)


def create_issue_if_required(review_object):
    """implement the logic to check problems here
    """
    avg_rating = Review.query(func.avg(Review.rating)).filter(productid = review_object.productid)
    if review_object.rating < avg_rating :
        new_issue = Issue(created_at = datetime.now(), review_id = review_object.id, review = Review.query.filter_by(Review.query.filter_by(id = review_object.id)))
        db.session.add(new_issue)
    print("review handler returning")
    pass


@app.route("/submit_review", methods=["POST"])
def submit_review():
    """ The request form should contain following:
    userid, productid, rating, comment (exact name)
    """
    try:
        productid = int(request.form["productid"])
        userid = int(request.form["userid"])
        rating = request.form["rating"]
        comment = request.form["comment"]
        # check existing review
        old_rev = Review.query.filter_by(productid=productid, userid=userid).first()
        print("existing review", old_rev)
        if not old_rev:
            new_rev = Review(userid=userid, productid=productid, rating=rating, comment=comment)
            db.session.add(new_rev)
            print("new review added")
        else:
            old_rev.rating = rating
            old_rev.comment = comment
            old_rev.created_at = datetime.now()
            new_rev = old_rev
            print("review updated")
        db.session.commit()
    except KeyError:
        return "Incomplete parameters", 400
    except sqlalchemy.exc.IntegrityError:
        # should not happen
        return "Database crashed", 500
    else:
        create_issue_if_required(new_rev)
        return "OK"


@app.route("/admin")
def admin():
    # report of hits on distinct products
    today = datetime.now().strptime("%d-%m-%Y")
    start_time = datetime.strftime(today, "%d-%m-%Y")
    end_time = datetime.now()
    logs = Log.query.filter(Log.timestamp > start_time, Log.timestamp < end_time)
    return render_template("admin.html", logs=logs)


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
