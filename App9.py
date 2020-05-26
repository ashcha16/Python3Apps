from flask import Flask,render_template,request
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from send_email import send_email

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__= "data"
    id=db.Column(db.Integer,primary_key=True)
    email_db=db.Column(db.String(120),unique=True)
    height_db=db.Column(db.Integer)

    def __init__(self,email_db,height_db):
        self.email_db=email_db
        self.height_db=height_db



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods=['POST']) #default value of methods is GET
def success():
    if request.method=="POST":
        email=request.form["email_name"]
        height=request.form["height_name"]
        data=Data(email,height)
        if db.session.query(Data).filter(Data.email_db==email).count()==0:
            db.session.add(email,height)
            db.session.commit()
            avg_height=db.session.query(func.avg(Data.height_db)).scalar()
            avg_height=round(avg_height,1)
            count_db=db.session.query(Data.height_db).count()
            send_email(email,height,avg_height,count_db)
            return render_template("success.html")
    return render_template("index.html",
    text="Email already exists")

if __name__=="__main__":
    app.run(debug=True)