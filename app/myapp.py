from flask import Flask, render_template
app = Flask(__name__)

from views import *

"""
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signups.html')

"""

if __name__ == "__main__":
    app.run(debug = True)

