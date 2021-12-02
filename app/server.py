from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('main.html')


@app.route('/login', methods = ['POST', 'GET'])
def login():
   error = None
   if request.method =='POST'
   if request.form['username'] != 'ossp' or request.form['password'] != 'ossp1234' :
      error = 'Incorrect authentication credentials! Please try again'
   else :
      return render_template('application_form.html')
   
   return render_template('login.html', error = error)

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
   uname= request.form.get('uname')
   umajor= request.form.get('umajor')
   grade= request.form.get('grade')
   
   return render_template('submit.html',umajor=umajor, grade=grade, uname=uname)

if __name__ == '__main__': 
    app.run(host="0.0.0.0", debug=True, port=80)

   