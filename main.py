from flask import Flask

app = Flask(name)

@app.route('/')
def hello_world():
    return 'Hello,Bu 1650700964'

if name == 'main':
    app.run(debug=True,port=80
