from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/ANISH")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/data/',methods =['POST'])
def data():
    if request.method  == 'POST':
        form_data = request.form
        return  form_data


if __name__== "__main__":
    app.run(debug=True) 