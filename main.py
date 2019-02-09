from flask import Flask, request, render_template
from send_email import send_email

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        send_email(email, height)
        print(email, height)
    return render_template("success.html")

if __name__ == '__main__':
    app.debug = True
    app.run()