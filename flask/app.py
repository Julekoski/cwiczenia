from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
 return 'Hello, World!'

@app.route('/Test')
def Test():
 return '<h1><b>Testujemy sobie serwer</b></h1>'
   

@app.route('/Obrazek')
def Obrazek():
 return '<h1>Dolomity</h1><img src="https://img.freepik.com/free-photo/beautiful-shot-grassy-hills-covered-trees-near-mountains-dolomites-italy_181624-24400.jpg?t=st=1732016953~exp=1732020553~hmac=a9b967f60792dd27d25167d2cd83823a8ec8c1ad3b366d15cda9f0767f0757b7&w=996"></img>'


@app.route('/modulo/<liczba>')
def modulo(liczba):
    if int(liczba)%2==0 or int(liczba)%3==0 or int(liczba)%5==0:
        return f'<b>Liczba jest podzielna przez 2,3 lub 5</b>'
    else:
        return f'<b>Liczba nie jest podzielna przez 2,3 lub 5</b>'
   


@app.route('/about/<name>')
def name1(name):
    return render_template('about.html', name= name )
 