from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", color= "blue", num= 3)

@app.route('/play/<int:num>')
def diff_num(num):
    return render_template("index.html", color= "blue", num= num)

@app.route('/play/<int:num>/<string:col>')
def diff_num_col(num, col):
    return render_template("index.html", color= col, num= num)

if __name__=='__main__':
    app.run(debug=True)