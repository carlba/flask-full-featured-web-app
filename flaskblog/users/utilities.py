import os
import secrets

from PIL import Image
from flask import url_for, current_app
from flask_mail import Message

from flaskblog import mail


def save_picture(form_picture_data):
    random_hex = secrets.token_hex(8)
    _, extension = os.path.splitext(form_picture_data.filename)
    new_picture_filename = f'{random_hex}{extension}'
    # TODO: Can saving the file be done without manual path handling?
    picture_path = os.path.join(current_app.root_path, 'static/profile_pictures', new_picture_filename)

    # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
    output_size = (125, 125)
    image = Image.open(form_picture_data)
    image.thumbnail(output_size)
    image.save(picture_path)

    return new_picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request', sender=current_app.config['MAIL_USERNAME'],
                      recipients=[user.email])
    # The _external keyword argument makes sure that an absolute url is generated.
    message.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)} 

If you did not make this request just ignore this email and nothing will change.    
    '''
    mail.send(message)

