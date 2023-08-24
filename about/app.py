from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/img', 'favicon.ico')

@app.route('/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=8989, host='0.0.0.0')
