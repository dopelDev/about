from flask import Flask, render_template, send_from_directory, request
from module.forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/img', 'favicon.ico')

@app.route('/')
def about():
    form = ContactForm()
    return render_template('about.html', form=form)

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():

    return "Aun no se"

if __name__ == '__main__':
    app.run(debug=True, port=8989, host='0.0.0.0')
