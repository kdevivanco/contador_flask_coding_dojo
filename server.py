
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter']+=1
    se_counter = session['counter']

    return render_template("index.html",se_counter=se_counter)

@app.route('/click', methods=['POST'])
def increment():
    if request.method == 'POST':
        if 'click' in request.form and request.form['click'] == 'click':
            print('click')
            
        elif 'doubleclick' in request.form and request.form['doubleclick'] == 'doubleclick':
            print('doubleclick')
            session['counter'] +=1
        
        
    return redirect('/')

@app.route('/userch', methods=['POST'])
def userch():
    session['counter'] += int(request.form['user_choice'])-1 #le resto 1 porque al refresh ya le suma uno
    return redirect('/')


@app.route('/destroypage', methods=['POST'])
def destroy():
    if request.form['refresh'] == 'refresh':
            print('refresh')
            session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)