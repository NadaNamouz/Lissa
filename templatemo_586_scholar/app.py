from flask import Flask, render_template, redirect, request, session, url_for, jsonify
import pyrebase

firebaseConfig = {
  apiKey: "AIzaSyDkOa607l4wYh9BcaAt8LdBuU8CL7wK6N0",
  authDomain: "case-studies---lissan.firebaseapp.com",
  databaseURL: "https://case-studies---lissan-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "case-studies---lissan",
  storageBucket: "case-studies---lissan.appspot.com",
  messagingSenderId: "904275628053",
  appId: "1:904275628053:web:f6b945dd1ead37fa6bbe1c"
}


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '123456'

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


@app.route('/signup', methods=['GET','POST'])
def signup():
  return render_template('signup.html')

@app.route('/login', methods=['GET','POST'])
def logi():
  return render_template('login.html')

@app.route('/index', methods=['GET','POST'])
def index():
  return render_template('index.html')

'''
@app.route('/practice', methods=['GET','POST'])
def practice():
  return render_template('practice.html')

@app.route('/meetups', methods=['GET','POST'])
def meetups():
  return render_template('meetups.html')

@app.route('/jobs', methods=['GET','POST'])
def jobs():
  return render_template('Jobs.html')

@app.route('/community', methods=['GET','POST'])
def community():
  return render_template('community.html')

@app.route('/chats', methods=['GET','POST'])
def chats():
  return render_template('chats.html')

@app.route('/conncect', methods=['GET','POST'])
def connect():
  return render_template('connect.html')
'''

if __name__ == '__main__':
    app.run(debug=True)
