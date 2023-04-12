from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "BANKAI"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1

    return render_template('index.html')

@app.route('/counter', methods=['POST'])
def counter():
    session['count'] += 1

    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)


