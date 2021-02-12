from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''Beautiful 
        MIND '''

if __name__ == '__main__' :
    app.run(debug=True)
    # app.run(debug=True)