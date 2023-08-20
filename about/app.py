from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8989, host='0.0.0.0')
