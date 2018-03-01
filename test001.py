from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello():
    #return "<html><body><h1>Hello World</h1></body></html>"
    return render_template('hello.html')
    
#@app.route('/members')
#def members():
#   return "Members"

@app.route('/members/<string:name>/')
def getMember(name):
    #return "namaeha "+ name + "です。"
    return render_template('nametest.html',name=name)

@app.route('/init001/<string:init001>/')
def getMember2(init001):
    return render_template('init001.html',init001=init001)

if __name__ == "__main__":
    app.run(debug= True,port=80)