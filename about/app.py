import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
module_path = os.path.join(currentdir, 'module')
sys.path.append(module_path)

from flask import Flask, render_template, send_from_directory, jsonify, request
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect
from forms import ContactForm
from config import ProductionConfig 
from generator import TemporalUUIDGenerator

app = Flask(__name__)
# Configuración de la aplicación
app.config.from_object(ProductionConfig)
# Configuración de la extensión Mail
mail = Mail(app)
# uuid generator
uuid_generator = TemporalUUIDGenerator()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static/img', 'favicon.ico')

@app.route('/app.bundle.js')
def app_bundle():
    return send_from_directory('static/js', 'app.bundle.js')
@app.route('/custom.js')
def custom_js():
    return send_from_directory('static/js', 'custom.js')

@app.route('/')
def about():
    try:
        uuid_generator.cleanup_uuids()
    except:
        print("Error al limpiar uuids")
    finally:
        uuid = uuid_generator.generate_uuid(lifespan_minutes=25)
        uuid = uuid_generator.get_uuids()
    print(uuid.keys())
    costumer_uuids = list(uuid.keys())
    print(costumer_uuids[-1])
    form = ContactForm()
    uuid_vault = list(uuid_generator.get_uuids().keys())
    print(f'vault box : {uuid_vault}')
    return render_template('about.html', form=form, uuid=costumer_uuids[-1])

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    form = ContactForm()
    uuid = request.headers.get('X-UUID')
    print(f'Value from frontend : {uuid}')
    uuid_vault = list(uuid_generator.get_uuids().keys())
    print(f'vault box : {uuid_vault}')
    print(f'form is valid : {form.validate_on_submit()}')
    if uuid in uuid_vault and form.validate_on_submit() is True:
        message = form.message.data
        if form.subject.data == None:
            form.subject.data = 'Consulta'
        msg = Message(form.subject.data, sender='322kuroneko2@gmail.com', recipients=['322kuroneko@gmail.com'])
        msg.body = message + '\n' + "from: " + form.email.data + '\n' + "First Name: " + form.first_name.data + '\n' + "Last Name: " + form.last_name.data + '\n' + "Country: " + form.country.data
        mail.send(msg)
        return jsonify({'success' : True})
    else:
        return jsonify({'success' : False})

if __name__ == '__main__':
    app.run()
