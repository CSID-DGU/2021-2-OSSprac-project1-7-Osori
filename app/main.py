from flask import Flask, render_template, request

app = Flask(__name__)
data = dict()

@app.route('/')
def student():
   return render_template('main.html', data = data)

@app.route('/detail', methods = ['POST', 'GET'])
def detail():
   if request.method == 'POST':
      data['Name'] = request.form.get('Name')
      data['StudentNumber'] = request.form.get('StudentNumber')
      data['Gender'] = request.form.get('Gender')
      data['Major'] = request.form.get('Major')
      return render_template("detail.html",data = data)

if __name__ == '__main__': 
    app.run(host="0.0.0.0", debug=True, port=80)


