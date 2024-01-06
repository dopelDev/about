from flask import Flask, render_template, send_from_directory, jsonify
from flask_mail import Mail, Message
from module.forms import ContactForm
from module.config import DevelopmentConfig

app = Flask(__name__)
# Configuración de la aplicación
app.config.from_object(DevelopmentConfig)
# Configuración de la extensión Mail
mail = Mail(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/img', 'favicon.ico')

@app.route('/')
def about():
    form = ContactForm()
    return render_template('about.html', form=form)

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    form = ContactForm()
    if form.validate_on_submit():
        print(form.first_name.data)
        message = form.message.data
        if form.subject.data == None:
            form.subject.data = 'Consulta'
        msg = Message(form.subject.data, sender='322kuroneko2@gmail.com', recipients=['322kuroneko@gmail.com'])
        msg.body = message + '\n' + "from: " + form.email.data + '\n' + "Nombre: " + form.first_name.data + '\n' + "Apellido: " + form.last_name.data + '\n' + "Country: " + form.country.data
        mail.send(msg)
        return  jsonify(form.data)
    else:
        return "No se ha enviado el formulario"

if __name__ == '__main__':
    app.run(debug=True, port=8989, host='0.0.0.0')
