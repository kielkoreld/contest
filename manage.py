from flask import Flask, render_template, request
menu = []
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/create/', methods = ['GET', 'POST'])
def create():
    if(request.method == 'GET'):
        return render_template("index.html")
    elif(request.method == 'POST'):
        name = request.form['name']
        count = int(request.form['count'])
        setting = int(request.form['setting'])
        newmenu = {"name":name, "count":count, "setting":setting}
        menu.append(newmenu)
        return render_template("index.html", menu = menu)
app.run(debug=True)