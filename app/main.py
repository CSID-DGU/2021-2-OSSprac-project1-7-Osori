from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('main.html')

@app.route('/detail', methods = ['POST', 'GET'])
def detail():
   if request.method == 'POST':
      detail = dict()
      detail['Name'] = request.form.get('Name')
      detail['StudentNumber'] = request.form.get('StudentNumber')
      detail['Gender'] = request.form.get('Gender')
      detail['Major'] = request.form.get('Major')
      return render_template("detail.html",detail = detail)

if __name__ == '__main__': 
    app.run(host="52.78.156.130", debug=True, port=80）


