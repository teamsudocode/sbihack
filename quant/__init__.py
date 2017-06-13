from flask import Flask

app = Flask(__name__)

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

