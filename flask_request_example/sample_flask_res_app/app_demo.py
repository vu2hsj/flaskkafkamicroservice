from flask import Flask

app = Flask(__name__)

@app.route("/test")
def index():
    return "Congratulations, it's a web app!"


if __name__ == '__main__':
    # run app in debug mode on port 9000
    app.run(debug=True, host="0.0.0.0",port=9000)
