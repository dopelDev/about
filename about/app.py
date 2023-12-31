from flask import Flask, render_template, send_from_directory, jsonify
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect, generate_csrf
from wtforms import form
from module.forms import ContactForm
from module.config import ProductionConfig

app = Flask(__name__)
# Configuración de la aplicación
app.config.from_object(ProductionConfig)
csrf = CSRFProtect(app)
# Configuración de la extensión Mail
mail = Mail(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/img', 'favicon.ico')

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    print(form)
    return "OK" 

#    if form.validate_on_submit():
#        message = form.message.data
#        if form.subject.data == None:
#            form.subject.data = 'Consulta'
#        msg = Message(form.subject.data, sender='322kuroneko2@gmail.com', recipients=['322kuroneko@gmail.com'])
#        msg.body = message + '\n' + "from: " + form.email.data + '\n' + "First Name: " + form.first_name.data + '\n' + "Last Name: " + form.last_name.data + '\n' + "Country: " + form.country.data
#        mail.send(msg)
#        return jsonify({'success' : True, 'csrf_token' : generate_csrf()})
#    else:
#        return jsonify({'success' : False, 'csrf_token' : generate_csrf()})

if __name__ == '__main__':
    app.run(port=8181, host='0.0.0.0')
