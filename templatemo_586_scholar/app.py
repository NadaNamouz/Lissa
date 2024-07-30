from flask import Flask, render_template, redirect, request, session, url_for, jsonify
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDkOa607l4wYh9BcaAt8LdBuU8CL7wK6N0",
    'authDomain': "case-studies---lissan.firebaseapp.com",
    'databaseURL': "https://case-studies---lissan-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "case-studies---lissan",
    'storageBucket': "case-studies---lissan.appspot.com",
    'messagingSenderId': "904275628053",
    'appId': "1:904275628053:web:f6b945dd1ead37fa6bbe1c",
    'databaseURL': "https://case-studies---lissan-default-rtdb.europe-west1.firebasedatabase.app/"
}

app = Flask(__name__, template_folder='templates', static_folder='assets')
app.config['SECRET_KEY'] = '123456'

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


# The CODE

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if session["user"] != None:
            feedback = request.form['feedback']
            uid = session['user']['localId']

            ref = db.child("users").child(uid).get().val()

            firstname = ref['firstname']
            lastname = ref['lastname']

            UserInfo = {'firstname': firstname, 'lastname': lastname, 'feedback': feedback}
            db.child('feedbacks').child(uid).set(UserInfo)
            return render_template("index.html")
        else:
            return render_template('login.html')

    return render_template ("index.html")
  
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET' and session["user"] == None:
        return render_template("signup.html")
    elif request.method == 'POST':
        try:
            print("hello world")
            email = request.form['email']
            password = request.form['password']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            phone = request.form['phone']
            age = request.form['age']
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            uid = user['localId']
            UserInfo = {'firstname': firstname, 'lastname': lastname, 'phone': phone, 'age':age}
            db.child('users').child(uid).set(UserInfo)
            return render_template("index.html")
        except:
            excist = True
            return render_template("signup.html", excist = excist)
    else:
        return render_template("index.html")

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET' and session["user"] == None:
        return render_template("login.html")       
    elif request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
    else:
        return redirect(url_for('index'))


@app.route('/signout')
def signout():
    session['user']=None
    auth.current_user = None
    print("signed out user")
    return redirect(url_for('index'))


@app.route('/jobs')
def jobs():
    if request.method == "GET" and session["user"] != None:
        return render_template('jobs.html')
    else:
        return render_template('login.html')



@app.route('/feedback',methods=['GET', 'POST'])
def feedback():
    print("im in feedback route")
    if request.method == "POST":
        if session["user"] != None:
            feedback = request.form['feedback']
            uid = user['localId']
            UserInfo = {'firstname': firstname, 'lastname': lastname, 'feedback': feedback}
            db.child('feedbacks').child(uid).set(UserInfo)
            return render_template("index.html")
        else:
            return render_template('login.html')
    


@app.route('/practice')
def practice():
    return render_template('practice.html')

if __name__ == '__main__':
    app.run(debug=True ,port=3000)
