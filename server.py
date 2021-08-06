from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    
app.secret_key = 'Mellon'


@app.route('/')  
def index():
    if 'count' not in session:
        session['count'] = 0
    
    session['count'] += 1
    if session['count'] == 1:
        return render_template("index.html") 
    elif session['count'] == 10:
        session.clear()
        return render_template("index.html") 
    else: 
        return render_template("index.html") 

@app.route('/destroy_session', methods=['POST'])  
def refresh():
    session.clear()
    return redirect("/") 

@app.route('/count', methods=['POST'])  
def update_counter():
    session['count'] += 1
    return redirect("/") 
    
if __name__=="__main__":    
    app.run(debug=True)   