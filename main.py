import flask
from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Todo(db.model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(200),nullable=False )
  date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)