from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def checkerboard():
    return render_template("index.html",row=8,col=8, color1="#769656", color2="#eeeed2" )

@app.route('/<int:x>')
def change_column(x):
    return render_template("index.html",row=8,col=x, color1="#769656", color2="#eeeed2" )

@app.route('/<int:x>/<int:y>')
def change_size(x,y):
    return render_template("index.html",row=x,col=y, color1="#769656", color2="#eeeed2" )

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def change_board(x,y,color1,color2):
    return render_template("index.html",row=x,col=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)