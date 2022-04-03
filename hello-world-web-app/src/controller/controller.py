from flask import Flask, Response



app = Flask(__name__)



@app.route('/hello')
def metrics():
    return "hello world!"



@app.route('/health')
def health():
    return "OK"



if __name__ == "__main__":
    app.run()
