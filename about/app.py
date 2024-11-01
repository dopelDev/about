import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
module_path = os.path.join(currentdir, 'module')
sys.path.append(module_path)

from flask import Flask, render_template, send_from_directory, jsonify, request
from flask_mail import Mail, Message

app = Flask(__name__)
# Configuración de la aplicación
from forms import ContactForm
from config import ProductionConfig 
from generator import TemporalUUIDGenerator
import redis

redis_vault = redis.Redis(host='about_oldieRedis', port=6379, db=0)

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
    uuid = uuid_generator.generate_uuid(lifespan_minutes=5)
    uuid = uuid_generator.get_uuids()
    print(uuid.keys())
    uuids_from_redis = redis_vault.get('uuids')
    print(f'from redis: {uuids_from_redis}')
    form = ContactForm()
    print(f'vault box : {uuids_from_redis}')
    return render_template('about.html', form=form, uuid=uuids_from_redis)

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    form = ContactForm()
    uuid = request.headers.get('X-UUID')
    print(f'Value from frontend : {uuid}')
    uuid_vault = redis_vault.get('uuids')
    print(f'vault box : {uuid_vault}')
    print(f'user uuid : {uuid}')
    print(f'form is valid : {form.validate_on_submit()}')
    print(f'Value from frontend : {uuid}')
    if uuid == str(uuid_vault) and form.validate_on_submit() is True:
        message = form.message.data
        msg = Message(form.subject.data, sender='322kuroneko2@gmail.com', recipients=['322kuroneko@gmail.com'])
        msg.body = message + '\n' + "from: " + form.email.data + '\n' + "First Name: " + form.first_name.data + '\n' + "Last Name: " + form.last_name.data + '\n' + "Country: " + form.country.data
        mail.send(msg)
        print(f'mail has been sent : {mail}')
        return jsonify({'success' : True})
    else:
        return jsonify({'success' : False})

if __name__ == '__main__':
    app.run()
