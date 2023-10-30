from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fcmb.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
app.app_context().push()

#table one for account owners
class account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email  = db.Column(db.String(200))
    birthdate  = db.Column(db.String(200))
    address  = db.Column(db.String(200))
    accountbalance  = db.Column(db.Integer)
    employment = db.Column(db.String(200))
    salary  = db.Column(db.Integer)
    loan  = db.Column(db.Integer)
    period  = db.Column(db.Integer)
    accountnumber = db.Column(db.Integer)
    loanname = db.Column(db.String(200))
    message = db.Column(db.String(200))
    loanemail  = db.Column(db.String(200))
    loannumber  = db.Column(db.Integer)
    loanaddress  = db.Column(db.String(200))
    loanemployment = db.Column(db.String(200))
    loansalary  = db.Column(db.Integer)
    loanamount  = db.Column(db.Integer)
    loanperiod  = db.Column(db.Integer)
    loanaccountnumber = db.Column(db.Integer)
    garantorname1  = db.Column(db.String(200))
    garantorname2  = db.Column(db.String(200))
    garantoraddress1  = db.Column(db.String(200))
    garantoraddress2  = db.Column(db.String(200))
    garantornumber1  = db.Column(db.String(200))
    garantornumber2  = db.Column(db.String(200))
    date = db.Column(db.DateTime,default = datetime.utcnow)
db.create_all()


#home page
@app.route('/')
def home():
    value = 1
    data = account.query.filter_by(id=value).first()
    if data:
    #data = account.query.order_by(account.id)
        return render_template('index.html', data=data)

#peer2peer page
@app.route('/peer')
def peer():
    return render_template('peer2peer.html')

#loan tracker page
@app.route('/track', methods=['POST'])
def track():
    id = request.form['id']
    data = account.query.filter_by(id=id).first()
    if data:
        return render_template('loantracker.html', data=data)
    else:
        return 'sorry an error occured'

#question action voc
@app.route('/question', methods=['POST'])
def question():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    put = open('review_data.txt', 'w')
    put.write(name)
    put.write(email)
    put.write(message)
    put.close()
    return 'you review was submited successfuly, and is been reviewed by our experts'

#aboutp2p page
@app.route('/aboutp2p')
def about():
    return render_template('aboutp2p.html')

#voice of the customer page
@app.route('/voice')
def voice():
    return render_template('VoiceOfTheCustomer.html')

# notification page
@app.route('/notify', methods=['POST'])
def notify():
    id = request.form['id']
    data = account.query.filter_by(id=id).first()
    return render_template('notification.html', data=data)

#upload page
@app.route("/upload")
def upload():
    return render_template("upload.html")

# switch button to login page
@app.route("/switch", methods=["POST"])
def switch():
    return render_template('login.html')

#login action
@app.route("/login", methods=["POST"])
def login():
    name = request.form['name']
    password = request.form['password']

    if name == "user1" and password == "user1":
        value = 2
        data = account.query.filter_by(id=value).first()
        if data:
        #data = account.query.order_by(account.id)
            return render_template('index.html', data=data)
    elif name == "user2" and password == "user2":
        value = 3
        data = account.query.filter_by(id=value).first()
        if data:
        #data = account.query.order_by(account.id)
            return render_template('index.html', data=data)
    else:
        return 'no such user'

   
# request loan button to page
@app.route("/loan", methods=['POST'])
def loan():
    data = account.query.order_by(account.id)
    return render_template('P2P request.html', data=data)

#request loan 
@app.route('/askmoneyback', methods=['POST'])
def ask():
    id = request.form['id']

    update = account.query.get_or_404(id)
    update.message = request.form['message']
    db.session.commit()

    return 'message was sent successfully'
    
#loan request action page
@app.route("/loanrequest", methods=['POST'])
def loanrequest():
    id = request.form['id']
    
    update = account.query.get_or_404(id)
    update.loanname = request.form['name']
    update.loanemail = request.form['email']
    update.loannumber = request.form['number']    
    update.loanaddress = request.form['address']
    update.loanemployment = request.form['employment']
    update.loansalary = request.form['salary']
    update.loanamount = request.form['loanamount']
    update.loanperiod = request.form['period']
    update.loanaccountnumber = request.form['accountnumber']
    update.garantorname1 = request.form['garantorname1']
    update.garantoraddress1 = request.form['garantoraddress1']
    update.garantornumber1 = request.form['garantornumber1']
    update.garantorname2 = request.form['garantorname2']
    update.garantoraddress2 = request.form['garantoraddress2']
    update.garantornumber2 = request.form['garantornumber2']

    db.session.commit()
    return 'successful'

#make transfer of money
@app.route('/transfer',methods=['POST'])
def transfer():
    accountnumber = request.form['accountnumber']
    amount = request.form['amount']
    x = int(amount)
    
    #credit alert
    id = request.form['id']
    credit = account.query.get_or_404(id)
    credit.accountbalance
    credit.accountbalance += x

    #debit alert
    myid = request.form['myid']
    debit = account.query.get_or_404(myid)
    debit.accountbalance
    debit.accountbalance -= x
    db.session.commit()

    return 'successful'

@app.route("/add", methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    birthdate = request.form['birthdate']
    address = request.form['address']
    accountbalance = request.form['accountbalance']
    employment = request.form['employment']
    salary = request.form['salary']
    loan = request.form['loan']
    period = request.form['period']
    accountnumber = request.form['accountnumber']
    
    upload = account(name=name,email=email,birthdate=birthdate,address=address,accountbalance=accountbalance,employment=employment,salary=salary,loan=loan,period=period,accountnumber=accountnumber)
    db.session.add(upload)
    db.session.commit()

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)